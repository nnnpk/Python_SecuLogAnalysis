import time
import subprocess
from threading import Timer

###################################################################################
################################# USER INPUTS #####################################
###################################################################################

#Number of Attempts Allowed 
NumberofAtt=int(raw_input("Please enter the number of attempts allowed before blcoking"))

#Blocking Time
BlockingTime=int(raw_input("How long do you want to block the IP for? Enter in secnods"))

#Target log file
targetfile = raw_input("please enter the log file directory and name")

###################################################################################
################################ SCRIPT ###########################################
###################################################################################

#track the log file, equivalent of tail -F
def follow(thefile):
	thefile.seek(0,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

#split each line to a list, and get the IP address from the list
def getip(line):
	elementslist= []
	elements = line.split()
	for element in elements:
		elementslist.append(element)
	#print elementslist
	return elementslist[10]
	#print elementslist[10]


#track the secure log
#f = open("/var/log/secure")
f = open(str(targetfile))
lines = follow(f)

#creating dictionary for count of each IP
ipcount = {}


#count each IP address, when there is a attemption with wrong password
for i in lines:
	if (i.find('Failed password')!=-1):
		print i
		ipaddr=getip(i)
		if ipaddr in ipcount:
			ipcount[ipaddr]+= 1
		else:
			ipcount[ipaddr] = 1
		print "This IP has reached "+str(ipcount[ipaddr])+" Attempts"
		
		#if attemption number exceeds the limit, block the ip, but also unblock it after a period of time
		if ipcount[ipaddr] >= NumberofAtt:
			print "More than "+str(NumberofAtt)+" attempts, IP is blocked"
			ipcount[ipaddr] = 0;
			subprocess.call('iptables -A INPUT -s '+ipaddr+' -j DROP',shell=True)
			def release_ip():
				subprocess.call('iptables -D INPUT -s '+ipaddr+' -j DROP',shell=True)

			t= Timer(BlockingTime,release_ip)
			t.start()
	#clear the count if user got the right password
	elif (i.find('Accepted password') !=-1):
		ipaddr=getip(i)
		ipcount[ipaddr] = 0
	else:
		continue
	



