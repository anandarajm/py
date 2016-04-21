#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import subprocess

def ssh_command (user, host, password, command):
	#ssh_newkey = 'Are you sure you want to continue connecting'
	ssh_newkey = 'Are you sure you want to continue connecting (yes/no)?'
	print 'ssh -l %s %s %s' % (user, host, command)
	child = pexpect.spawn('ssh -l %s %s %s' % (user, host, command))
	child.logfile = sys.stdout
	i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'Password: '])
	print child.before, child.after
	if i == 0: 
		print "ERROR! SSH could not login. Here is what SSH said: "
		print child.before, child.after
		return None
	if i == 1: # SSH does not have the public key. Just accept it.
		child.sendline ('yes')
		child.expect ('Password: ')
		i = child.expect([pexpect.TIMEOUT, 'password: '])
		if i == 0: # Timeout
			print "ERROR! SSH could not login. Here is what SSH said: "
			print child.before, child.after
			return None
	child.sendline(password)
	#child.logfile = None
	print child.before
	return child
	
def main():
	# TODO: REPLACE WITH OPTION PARSE USING EXAMPLE ABOVE
	# Switch parameters
	host = '172.16.105.13'
	user = 'root'
	password = 'dellnfv'

	# SSH to host
	print "Connecting to %s..." %host
	child = None
	try:
		child = ssh_command (user, host, password, '')
	except:
		pass

	if not child:
		sys.exit()

	# Wait for # prompt
	child.logfile = open("C:\Users\anandaraj_maharajan\Documents\Python_program\sshtoesxi.log","w")
	promptList = ['#', '>',']']
	i = child.expect(promptList)
	send_f10cmd(child, 'cd /etc/init.d', ']')
	send_f10cmd(child, '/etc/init.d/DCUI status', ']')
	send_f10cmd(child, '/etc/init.d/ESXShell status', ']')
	send_f10cmd(child, '/etc/init.d/SSH status', ']')
	send_f10cmd(child, '/etc/init.d/cdp status', ']')
	send_f10cmd(child, '/etc/init.d/clomd status', ']')
	send_f10cmd(child, '/etc/init.d/cmmdsd status', ']')
	send_f10cmd(child, '/etc/init.d/dcbd status', ']')
	send_f10cmd(child, '/etc/init.d/ddecomd status', ']')
	send_f10cmd(child, '/etc/init.d/epd status', ']')
	send_f10cmd(child, '/etc/init.d/hostd status', ']')
	send_f10cmd(child, '/etc/init.d/iofiltervpd status', ']')
	send_f10cmd(child, '/etc/init.d/lacp status', ']')
	send_f10cmd(child, '/etc/init.d/lbtd status', ']')
	send_f10cmd(child, '/etc/init.d/llcolord status', ']')
	send_f10cmd(child, '/etc/init.d/lwsmd status', ']')
	send_f10cmd(child, '/etc/init.d/memscrubd status', ']')
	send_f10cmd(child, '/etc/init.d/netcpad status', ']')
	send_f10cmd(child, '/etc/init.d/nfcd status', ']')
	send_f10cmd(child, '/etc/init.d/nfsgssd status', ']')
	send_f10cmd(child, '/etc/init.d/nscd status', ']')
	send_f10cmd(child, '/etc/init.d/ntpd status', ']')
	send_f10cmd(child, '/etc/init.d/osfsd status', ']')
	send_f10cmd(child, '/etc/init.d/pcscd status', ']')
	send_f10cmd(child, '/etc/init.d/rabbitmqproxy status', ']')
	send_f10cmd(child, '/etc/init.d/rhttpproxy status', ']')
	send_f10cmd(child, '/etc/init.d/sdrsInjector status', ']')
	send_f10cmd(child, '/etc/init.d/sensord status', ']')
	send_f10cmd(child, '/etc/init.d/sfcbd status', ']')
	send_f10cmd(child, '/etc/init.d/sfcbd-watchdog status', ']')
	send_f10cmd(child, '/etc/init.d/slpd status', ']')
	send_f10cmd(child, '/etc/init.d/smartd status', ']')
	send_f10cmd(child, '/etc/init.d/snmpd status', ']')
	send_f10cmd(child, '/etc/init.d/storageRM status', ']')
	send_f10cmd(child, '/etc/init.d/swapobjd status', ']')
	send_f10cmd(child, '/etc/init.d/usbarbitrator status', ']')
	send_f10cmd(child, '/etc/init.d/vShield-Stateful-Firewall status', ']')
	send_f10cmd(child, '/etc/init.d/vmfstraced status', ']')
	send_f10cmd(child, '/etc/init.d/vmsyslogd status', ']')
	send_f10cmd(child, '/etc/init.d/vmtoolsd status', ']')
	send_f10cmd(child, '/etc/init.d/vmware-fdm status', ']')
	send_f10cmd(child, '/etc/init.d/vobd status', ']')
	send_f10cmd(child, '/etc/init.d/vprobed status', ']')
	send_f10cmd(child, '/etc/init.d/vpxa status', ']')
	send_f10cmd(child, '/etc/init.d/vsanObserver status', ']')
	send_f10cmd(child, '/etc/init.d/vsandevicemonitord status', ']')
	send_f10cmd(child, '/etc/init.d/vsantraced status', ']')
	send_f10cmd(child, '/etc/init.d/vsanvpd status', ']')
	send_f10cmd(child, '/etc/init.d/vvold status', ']')
	send_f10cmd(child, '/etc/init.d/vxlan-vib status', ']')
	send_f10cmd(child, '/etc/init.d/wsman status', ']')
	send_f10cmd(child, '/etc/init.d/xorg status', ']')
def send_f10cmd(child, cmd, resp=None, tout=30):
    try:
        child.sendline(cmd + '\r')
	child.delaybeforesend = 1
        if resp:
			child.expect(resp, timeout=tout)
			child.logfile = sys.stdout
			print child.before , child.after
				
    except:
        print("\tResponse timed out. Closing connection...")
        # Try to close connection gracefully
        try:
			child.sendline('exit\r')
			child.expect('#', timeout=1)
			print child.before
			child.sendline('exit\r')
			child.expect(pexpect.EOF, timeout=1)
			print child.before
        except:
            pass
        child.close()
        return -1
	
    return child.before

if __name__ == '__main__':
    main()
