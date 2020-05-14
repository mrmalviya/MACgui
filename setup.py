import sys
import platform
import argparse
import re
import os

import time
                                                                                                                       
go=True
try:
	import subprocess
	print()
	subprocess.call(["sudo " +" apt-get " +"install " +"net-tools"], shell=True)
	subprocess.call(["sudo " +" apt-get " +"install " +"macchanger"], shell=True)
	subprocess.call(["sudo " +" apt-get " +"install " +"python3-pyqt5"], shell=True)
except ImportError:
	print("\t\t[-]subprocess not Installed!!!")
	go=False
time.sleep(1)


print("\t==================================")
go=True
if sys.version_info >= (3, 0):
	print("\t\t[+] Python3+ found")
	
else:
	print("\t\t[-] Required python version>=3")
	go=False
time.sleep(1)
try:
	from PyQt5 import QtCore, QtGui, QtWidgets
	print("\t\t[+]pyqt5  Found!!!")
except ImportError:
	print("\t\t[-]pyqt5 not Installed!!!")
	go=False
time.sleep(1)
try:
	import subprocess
	print("\t\t[+]subprocess  Found!!!")
except ImportError:
	print("\t\t[-]subprocess not Installed!!!")
	go=False
time.sleep(1)

try:
	import fcntl, socket, struct
	print("\t\t[+]fcntl  Found!!!")
	time.sleep(1)
	print("\t\t[+]socket  Found!!!")
	time.sleep(1)
	print("\t\t[+]struct  Found!!!")
except ImportError:
	print("\t\t[-]fcntl,socket,struct not found!!!")
	go=False

if go==True:
	print("\t\t[+]Done!! run macchanger.py using python3")
	print()
time.sleep(1)
	
