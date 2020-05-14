from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import platform
import subprocess
import argparse
import re,uuid
import os
import uuid
import time
from random import choice, randint
from macgui import *
import fcntl, socket, struct
gui=Ui_MacChanger()

def msgbox(title,detail):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(detail)
        msg.exec_()

def current_mac(inter):
	    try:
	        a=subprocess.check_output(["macchanger"+" -s "+inter], shell=True)
	        m=a.decode("utf-8")
	        m=m.split("\n")
	        a=m[0].split('MAC')
	        return str(a[1])
	    except:
	    	return "Unable to fetch current_mac address"

def getaddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    return ':'.join('%02x' % b for b in info[18:24])            
	            


def network_list():
        try:
        	return os.listdir('/sys/class/net/') 
        except:
        	msgbox("Oops!!","Unable to list system interfaces.")
        	error_=["error","error","error"]
        	return error_


        


def optionss(index_op,interface):
        FNULL = open(os.devnull, 'w')
        try:
            subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
        except:
            msgbox("Oops!!","Process is Busy.")
            exit()

        if index_op=="1":
            subprocess.call(["macchanger " +" -e " + interface], shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
            subprocess.call(["ifconfig " + str(interface) + " up"], shell=True) 
            msgbox("Gotchha!!","MAC address has been changed successfully.")
        if index_op=="2":
            subprocess.call(["macchanger " +" -p " + interface], shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
            subprocess.call(["ifconfig " + str(interface) + " up"], shell=True) 
            msgbox("Gotchha!!","MAC address reset successfully.")   
        if index_op=="3":
            subprocess.call(["macchanger " +" -r " + interface], shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
            subprocess.call(["ifconfig " + str(interface) + " up"], shell=True) 
            msgbox("Gotchha!!","MAC address has been changed successfully .")     

        if index_op=="5":
            subprocess.call(["macchanger " +" -a " + interface], shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
            subprocess.call(["ifconfig " + str(interface) + " up"], shell=True) 
            msgbox("Gotchha!!","MAC address has been changed successfully .")   


def customm(interface,cmac):
        fail=False
        subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
        try:
        	a=subprocess.check_output(["macchanger " +" -m " + cmac +" "+interface], shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
        except:
        	msgbox("Oops!!","Invalid MAC Address.")
        	fail=True
        subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)
        if fail==False:
        	msgbox("Gotchha!!","MAC address has been changed successfully .")

def per(inter):
	once=True
#	while True:
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
		time.sleep(10)
	except KeyboardInterrupt:
		print("Exitting. . . . . BYE :)")
		exit()


