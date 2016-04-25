#!/usr/bin/env python
#
#   Dell Networking Proprietary Script
#       Ver 1.0
#
#   Change History:
#       Ver 1.0
#           - Read dynamically learned MAC address on a port-security enabled port and install it as static MAC
#           - Please execute "python macRestrict.py -h" for usage details.
#
from collections import defaultdict
import pexpect
import getpass
import os
import sys
import re
import time
import optparse
import socket
import re



def main():
    '''
    Script establishes an expect session to the specified switch and takes the following actions:
		1. Gets a list of interfaces that have port-security enabled with dynamic MAC address limit of 1
        2. Identifies the dynamically learned MAC address and VLAN information for each such interface
        3. Installs the dynamic MAC address as a static MAC address
        4. Sets port-security dynamic MAC address learning limit to 0
        5. Saves the configuration
   
    '''
    # Supported options
    #parser = optparse.OptionParser(usage='%prog [options]')
    #parser.add_option('-i', help='Switch IP', dest='host', type='str', default=None, action='store')
    #parser.add_option('-u', help='User', dest='user', type='str', default=None, action='store')
    #parser.add_option('-p', help='Password',  dest='password', type='str', default=None, action='store')
    #parser.add_option('-e', help='Enable Password', dest='enPassword', type='str', default=None, action='store')

    # Get user options
    #(opts, args) = parser.parse_args()

    # TODO: REPLACE WITH OPTION PARSE USING EXAMPLE ABOVE
    # Switch parameters
    host = '10.11.146.29'
    user = 'admin'
    password = 'powerconnect'
    enPassword = 'password'

    # Telnet to host
    child = None
    try:
        child = login_host(host, user, password, '')
    except:
        pass
 
    # Check if login was successful
    if not child:
	sys.exit()

    # Wait for # prompt
    #child.logfile = sys.stdout
    promptList = ['#', '>']
    i = child.expect(promptList)
    print("Connected to %s..." %  child.before)

    # Enter enable mode if not already in that mode
    if i == 1:
    	if send_cmd(child, 'ena', 'Password:') == -1:
            sys.exit()

        if send_cmd(child, enPassword, '#') == -1:
            sys.exit()

    # Configure Terminal Mode
    sysData = send_cmd(child, 'terminal length 0', '#')

    # Get interface data
    intfData = get_intf_data(child)

    # Install the dynamically learned MAC as static MAC
    cfg_static_mac(child, intfData)

    # TODO: ADD CODE TO CHECK WHAT PORTS HAVE PORT_SECURITY ENABLED AND THE CORRESPONDING STATIC MAC

    # End session
    send_cmd(child, 'exit')
    send_cmd(child, 'exit')
    
    


def login_host(host, user, password, command):
    '''
    Telnet to specified switch
    '''
    child = pexpect.spawn('telnet %s' % (host))

    # Enable logging to STDOUT
    child.logfile = sys.stdout

    i = child.expect([pexpect.TIMEOUT, 'User:'])
    if i == 0: # Timeout
    	print("ERROR! Could not telnet to host. Error %s, %s" % (child.before, child.after))
        return None
    child.sendline(user)

    i = child.expect([pexpect.TIMEOUT, 'Password:'])
    if i == 0: # Timeout
    	print("ERROR! Could not telnet to host. Error %s, %s" % (child.before, child.after))
        return None
    child.sendline(password)

    # Disable logging to STDOUT
    #child.logfile = None

    return(child)



def send_cmd(child, cmd, resp=None, tout=30):
    '''
    Send specified command to switch and wait if a valid response is expected
    '''
    try:
        child.sendline(cmd + '\r')
        if resp:
            child.expect(resp, timeout=tout)
    except:
        print("\tResponse timed out. Closing connection...")
        # Try to close connection gracefully
        try:
            child.sendline('exit\r')
            child.expect('#', timeout=1)
            child.sendline('exit\r')
            child.expect(pexpect.EOF, timeout=1)
        except:
            pass

        child.close()
        sys.exit()

    return(child.before)



def is_validIP(address):
    '''
    Check if IP Address is valid
    '''
    try:
        addr= socket.inet_pton(socket.AF_INET, address)
    except:
        return False
    return True


def get_intf_data(child):
    '''
    Get port-security configuration, dynamic MAC learning limit, and dynamically learned MAC address for each interface of the switch
    '''
    # Enable logging to STDOUT
    child.logfile = sys.stdout

    # Get interfaces and the dynamic MAC addresses learned on each interface
    intfData = defaultdict(dict)
    sysData = send_cmd(child, 'show port-security all', '#')
    for line in sysData.splitlines():
	if 'abled' not in line:
	    continue

	# Get tokens
	data = line.split()

	# Get information
	intf = data[0]
	intfData[intf]['portSec']    = data[1]
	intfData[intf]['dynMACCnt']  = int(data[2])
	intfData[intf]['statMACCnt'] = int(data[3])
        intfData[intf]['dynMAC']     = None

        # If port-security is enabled on the interface, get the dynamically learned MAC address
        if (intfData[intf]['portSec'] == 'Enabled') and (intfData[intf]['dynMACCnt'] == 1):
	    (intfData[intf]['dynMAC'], intfData[intf]['vlan']) = get_dynamic_mac(child, intf)

    # Disable logging to STDOUT
    #child.logfile = None

    return(intfData)


def get_dynamic_mac(child, intf):
    '''
    Get dynamic learned MAC address and corresponding VLAN on port-security enabled interface
    '''
    # Enable logging to STDOUT
    child.logfile = sys.stdout

    sysData = send_cmd(child, 'show port-security dynamic %s' % intf, '#')
    for line in sysData.splitlines():
        # We can process only one MAC per interface
        if 'Number' in line:
            data = line.split(':')
            if int(data[1]) != 1:
                return(None, None)

        # Now get the MAC address (format is ABCD.1234.5678)
        pattern = re.compile("([0-9a-fA-F]{4}[.]){2}[0-9a-fA-F]{4}")
        if re.search(pattern, line):
            data = line.split()
	    return(data[0], int(data[1]))

    # Disable logging to STDOUT
    #child.logfile = None

    return(None, None)



def cfg_static_mac(child, intfData):
    '''
    On ports with port-security enabled, configure dynamically learned MAC as static MAC and change dynamic learning limit to 0
    '''
    # Enable logging to STDOUT
    child.logfile = sys.stdout

    # Enter config mode
    sysData = send_cmd(child, 'config', '#')

    # For each interface that has port-security enabled and a dynamic MAC address, install the MAC as static
    configUpdated = False
    for intf, data in intfData.iteritems():
        # Nothing to be done if the interface doesn't have a dynamic MAC address
        if not data['dynMAC']:
            continue

        # Debug
	print('Interface: %s, portSec %s, dynamicMACCnt %d, MAC %s, VLAN %d' % (intf, data['portSec'], data['dynMACCnt'], data['dynMAC'], data['vlan']))

        # Enter interface context
    	sysData = send_cmd(child, 'interface %s' % intf, '#')

        # Configure static MAC
    	sysData = send_cmd(child, 'switchport port-security mac-address %s vlan %d' % (data['dynMAC'], data['vlan']), '#')
            
        # Stop dynamic MAC learning
    	sysData = send_cmd(child, 'switchport port-security dynamic 0', '#')
        
        # Flag that write is necessary
        configUpdated = True

    # Exit config mode
    sysData = send_cmd(child, 'end', '#')

    # Save configuration
    if configUpdated:
        sysData = send_cmd(child, 'write', '(y/n)')
        sysData = send_cmd(child, 'y', '#')
    
    # Disable logging to STDOUT
    #child.logfile = None

if __name__ == '__main__':
    main()
