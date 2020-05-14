import subprocess
import optparse
import time
import re
from os import system
from support_mac import *
system('clear')
print(" __       __   ______    ______       ________  ________  _______     ")      
time.sleep(0.3)
print("|  \     /  \ /      \  /      \     |        \|        \|       \ ") 
time.sleep(0.3)    
print("| $$\   /  $$|  $$$$$$\|  $$$$$$\     \$$$$$$$$| $$$$$$$$| $$$$$$$\ ")
time.sleep(0.3)    
print("| $$$\ /  $$$| $$__| $$| $$   \$$______ | $$   | $$__    | $$__| $$ ")
time.sleep(0.3)    
print("| $$$$\  $$$$| $$    $$| $$     |      \| $$   | $$  \   | $$    $$ ")
time.sleep(0.3)    
print("| $$\$$ $$ $$| $$$$$$$$| $$   __ \$$$$$$| $$   | $$$$$   | $$$$$$$\ ")
time.sleep(0.3)    
print("| $$ \$$$| $$| $$  | $$| $$__/  \       | $$   | $$_____ | $$  | $$ __ ")
time.sleep(0.3)
print("| $$  \$ | $$| $$  | $$ \$$    $$       | $$   | $$     \| $$  | $$|  \ ")
time.sleep(0.3)
print(" \$$      \$$ \$$   \$$  \$$$$$$         \$$    \$$$$$$$$ \$$   \$$ \$$")
time.sleep(0.3)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]    A Tool By MrMalviya")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+] Periodic MAC changer")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]   run macgui.py for GUI ")

def per(inter,tim):
	once=True
	if os.getuid() != 0:
		print("Are you Root ?")
		time.sleep(1)
		exit()
	while True:
		try:
			if once==True:
				print("Current MAC Address : "+current_mac(inter))
				once=False
			try:
				subprocess.call(["ifconfig " + str(inter) + " down"], shell=True)
			except:
				print("Process is Busy")
				exit()
			try:
				FNULL = open(os.devnull, 'w')
				subprocess.call(["macchanger " +" -r " + str(inter)], shell=True ,stdout=FNULL, stderr=subprocess.STDOUT)
			except:
				print("Unable To Change MAC.")
			try:
				subprocess.call(["ifconfig " + str(inter) + " up"], shell=True) 
			except:
				print("Process is Busy")
			print("Current MAC Address : "+current_mac(inter))
			time.sleep(tim)
		except KeyboardInterrupt:
			print("Exitting. . . . . BYE :)")
			exit()

def call():
	tim=int(input("Enter Time Duration  (in seconds. ) "))
	print("Enter Interface From Following :")
	list=network_list()
	for i in list:
		print("[*] "+i) 
	inter=input(">>>")
	if inter not in list:
		
		system('clear')
		print("Wrong Interface (select again)")
		call()
	print("-------------------------------")
	print("Interface :\t"+inter)
	print("Time Duration :\t"+str(tim))
	print("-------------------------------")
	per(str(inter),tim)


try:
	call()
except:
	print("Exitting . . .  BYE :)")
	exit()

                                                                      


