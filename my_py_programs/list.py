import string

fh=open('.\processes.txt','r')
process=[]
new_proc=[]

for line in fh:
	process.append(line.rstrip())


for word in process:
	new_proc.append("send_f10cmd(child, '/etc/init.d/%s status', ']')" %word)
for word in process:
	new_proc.append("/etc/init.d/%s status" %word)
for element in new_proc:
	print element
	
#send_f10cmd(child, '/etc/init.d/DCUI status', ']')