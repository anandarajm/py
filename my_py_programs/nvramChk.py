#!/usr/bin/env python
#
#   Dell-Force10 Proprietary Script
#       Ver 1.0
#
#   Change History:
#       Ver 1.0
#           - Check if specified hosts have suspect SDMMC card
#           - Please execute "python nvramChk.py -h" for usage details.
#
import pexpect
import getpass
import os
import sys
import re
import time
import optparse
import socket

def ssh_command (user, host, password, command):
    #ssh_newkey = 'Are you sure you want to continue connecting'
    ssh_newkey = 'Are you sure you want to continue connecting (yes/no)?'
    child = pexpect.spawn('ssh -l %s %s %s' % (user, host, command))
    #child.logfile = sys.stdout
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
    if i == 0: # Timeout
        print "ERROR! SSH could not login. Here is what SSH said: "
        print child.before, child.after
        return None
    if i == 1: # SSH does not have the public key. Just accept it.
        child.sendline ('yes')
        #child.expect ('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout
            print "ERROR! SSH could not login. Here is what SSH said: "
            print child.before, child.after
            return None
    child.sendline(password)
    #child.logfile = None
    return child

def main():
    # Supported options
    parser = optparse.OptionParser(usage='%prog [options]')
    parser.add_option('-f', help='Specify file containing IP Addresses', dest='hostFile', default=None, action='store')
    
    # Get user options
    (opts, args) = parser.parse_args()

    # Read hosts from file, if one was provided
    hostList = []
    if opts.hostFile is not None:
        try:
            fd = open(opts.hostFile)
	    for line in fd:
	        if line:
	            hostList += line.split()
            fd.close()
        except:
            print("Failed to open File %s!" % (opts.hostFile))

    # If we don't have a valid list of hosts, ask for one
    if len(hostList) <= 0:
        host = raw_input("Enter Chassis IP address: ")
        hostList.append(host)

    # Check hosts
    hostList = [host for host in hostList if is_validIP(host)]
    print hostList
    
    # Get username, password, etc
    user     = raw_input("Enter username: ")
    password = getpass.getpass()
    #user = 'admin'
    #password = 'admin'
    
    # Check hosts for suspect NVRAM
    hostData = {}
    print hostList
    for host in hostList:
        # Initialize
        hostData[host] = {'s60': 'No', 'name' : '', 'sno' : '', 'nv' : 'Unknown', 'raw' : '', 'op': False}
        print "-" * 140
        
        # SSH to host
        print "Connecting to %s..." % host
        child = None
        try:
            child = ssh_command (user, host, password, '')
        except:
            pass
        
        if not child:
            print "Failed to SSH into %s. Skipping..." % host
            print "-" * 140
            continue

        # Wait for # prompt
        #child.logfile = sys.stdout
        promptList = ['#', '>']
        i = child.expect(promptList)
        hostData[host]['name'] = child.before.splitlines()[-1]
        print "Connected to %s..." % hostData[host]['name']

        # Enter enable mode if not already in that mode
        if i == 1:
            if send_f10cmd(child, 'ena', 'Password: ') == -1:
                continue
            
            if send_f10cmd(child, 'force10', '#') == -1:
                continue

        # Enter config mode
        print "\tEntering configuration mode..."
        if send_f10cmd(child, 'conf', '#') == -1:
            continue

        # Enter restricted mode
        if send_f10cmd(child, 'ena res f', '#') == -1:
            continue

        # Exit from config mode
        if send_f10cmd(child, 'end', '#') == -1:
            continue

        # Get switch information
        sysData = send_f10cmd(child, 'show system stack-unit 0 | no-more', '#')
        if sysData == -1:
            continue

        # Process
        for line in sysData.splitlines():
            # Check if S60
            if 'Current Type' in line and 'S60' in line:
                hostData[host]['s60'] = 'Yes'
                continue
            
            # Get serial number
            if 'Serial' in line:
                hostData[host]['sno'] = line.split(":")[-1].lstrip()
                continue
        
        # Check if we actually connected to an S60
        if hostData[host]['s60'] == 'No':
            print "%s is not an S60. Exiting..." % hostData[host]['name']
            send_f10cmd(child, 'exit', pexpect.EOF)
            print "-" * 140
            continue
        
        # Magic
        if send_f10cmd(child, 'f10-1231 f abracadabra31', '#') == -1:
            continue

        # Attach to CP
        #child.logfile = sys.stdout
        #print "\tAttaching to debug shell..."
        #if send_f10cmd(child, 'attach cp') == -1:
        #    continue
        #if send_f10cmd(child, 'root', 'Password:') == -1:
        #    continue
        #if send_f10cmd(child, 'abracadabra31', 'SStk-0 # ') == -1:
        #    continue

        # Get data
        print "\tReading dmesg data..."
        #dmesgData = send_f10cmd(child, 'dmesg', 'SStk-0 # ', 60)
        #if dmesgData == -1:
        #    continue
        dmesgData = send_f10cmd(child, 'remote-exec cp \'dmesg\'', hostData[host]['name'], 120)
        if dmesgData == -1:
            continue

        if send_f10cmd(child, '', '#') == -1:
            continue

        if send_f10cmd(child, '', '#') == -1:
            continue
        
        if send_f10cmd(child, 'exit', '#') == -1:
            continue

        # Exit
        print "Exiting %s..." % hostData[host]['name']
        send_f10cmd(child, 'exit', pexpect.EOF)

        # Wait
        time.sleep(1)

        # Parse dmesg
        for line in dmesgData.splitlines():
            if "MID:" in line:
                hostData[host]['raw'] = line
                temp = line.split()
                if len(temp) > 7:
                    mid = int(temp[5], 16)
                    oid = int(temp[7], 16)
                    hostData[host]['nv'] = 'Yes' if mid == 0x45 and oid == 0x24 else 'No'
    
        print "-" * 140
        hostData[host]['op'] = True
        
    # Print summary report:
    print
    print
    print
    print "*" * 140
    print "Summary Report"
    print "=" * 140
    print "IP               SwitchName            S60    SerialNumber          Suspect   Comments"
    print "=" * 140
    for k, v in hostData.iteritems():
        if v['s60'] == 'Yes':
            nstr = v['nv']
            rstr = 'Connection timed out' if not v['op'] else v['raw']
        else:
            nstr = ''
            rstr = ''
        print "%-15s  %-20s  %-5s  %-20s  %-8s  %s" % (k, v['name'], v['s60'], v['sno'], nstr, rstr)
    print "*" * 140
    print
    print
    print

def send_f10cmd(child, cmd, resp=None, tout=30):
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
        return -1

    return child.before

def is_validIP(address):
    try:
        addr= socket.inet_pton(socket.AF_INET, address)
    except:
        return False
    return True

if __name__ == '__main__':
    main()
