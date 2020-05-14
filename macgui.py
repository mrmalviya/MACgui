from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import subprocess
import argparse
import re
import os
import uuid
import threading
from random import choice, randint
from support_mac import *

class Ui_MacChanger(object):


    def setupUi(self, MacChanger):
        MacChanger.setObjectName("MacChanger")
        MacChanger.resize(1092, 519)
        MacChanger.setFixedSize(1092,519)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MacChanger.sizePolicy().hasHeightForWidth())
        MacChanger.setSizePolicy(sizePolicy)
        MacChanger.setMinimumSize(QtCore.QSize(0, 0))
        MacChanger.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MacChanger)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1101, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 1031, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(800, 40, 321, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 200, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 361, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setGeometry(QtCore.QRect(520, 180, 41, 39))
        self.lineEdit_a.setText("")
        self.lineEdit_a.setMaxLength(2)
        self.lineEdit_a.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.lineEdit_b = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_b.setGeometry(QtCore.QRect(580, 180, 41, 39))
        self.lineEdit_b.setText("")
        self.lineEdit_b.setMaxLength(2)
        self.lineEdit_b.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.lineEdit_c = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_c.setGeometry(QtCore.QRect(640, 180, 41, 39))
        self.lineEdit_c.setText("")
        self.lineEdit_c.setMaxLength(2)
        self.lineEdit_c.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_c.setObjectName("lineEdit_c")
        self.lineEdit_d = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_d.setGeometry(QtCore.QRect(700, 180, 41, 39))
        self.lineEdit_d.setText("")
        self.lineEdit_d.setMaxLength(2)
        self.lineEdit_d.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.lineEdit_e = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_e.setGeometry(QtCore.QRect(760, 180, 41, 39))
        self.lineEdit_e.setText("")
        self.lineEdit_e.setMaxLength(2)
        self.lineEdit_e.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_e.setObjectName("lineEdit_e")
        self.lineEdit_f = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f.setGeometry(QtCore.QRect(820, 180, 41, 39))
        self.lineEdit_f.setText("")
        self.lineEdit_f.setMaxLength(2)
        self.lineEdit_f.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_f.setObjectName("lineEdit_f")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 420, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start_point)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 260, 301, 41))
        self.label_5.setObjectName("label_5")
        self.comboBox_interface = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_interface.setGeometry(QtCore.QRect(220, 110, 171, 41))
        self.comboBox_interface.setStyleSheet("color:rgb(0,0,0)")
        self.comboBox_interface.setObjectName("comboBox_interface")
        self.comboBox_interface.addItem("")
        self.comboBox_interface.addItem("")
        self.comboBox_interface.addItem("")
        self.comboBox_options = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_options.setGeometry(QtCore.QRect(460, 110, 451, 41))
        self.comboBox_options.setObjectName("comboBox_options")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.lineEdit_current = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_current.setGeometry(QtCore.QRect(460, 260, 451, 39))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_current.setFont(font)
        self.lineEdit_current.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_current.setReadOnly(True)
        self.lineEdit_current.setObjectName("lineEdit_current")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 320, 301, 41))
        self.label_6.setObjectName("label_6")
        self.lineEdit_new = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_new.setGeometry(QtCore.QRect(460, 320, 451, 39))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_new.setFont(font)
        self.lineEdit_new.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_new.setReadOnly(True)
        self.lineEdit_new.setObjectName("lineEdit_new")
        MacChanger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MacChanger)
        self.statusbar.setObjectName("statusbar")
        MacChanger.setStatusBar(self.statusbar)

        self.retranslateUi(MacChanger)
        QtCore.QMetaObject.connectSlotsByName(MacChanger)




    def retranslateUi(self, MacChanger):
        _translate = QtCore.QCoreApplication.translate
        MacChanger.setWindowTitle(_translate("MacChanger", "Mac-Changer (GUI)"))
        self.label.setText(_translate("MacChanger", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Mac-Changer</span></p></body></html>"))
        self.label_2.setText(_translate("MacChanger", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#bbb413;\">[+] By MR.Malviya</span></p></body></html>"))
        self.label_3.setText(_translate("MacChanger", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#21c621;\">Interface</span></p></body></html>"))
        self.label_4.setText(_translate("MacChanger", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#21bf21;\">Enter Custom MAC </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">(if selected)*</span></p></body></html>"))
        self.pushButton.setText(_translate("MacChanger", "CHANGE"))
        self.label_5.setText(_translate("MacChanger", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#21bf21;\">Old MAC Address</span></p></body></html>"))
        List=network_list()
        k=0  
        for i in List:
            self.comboBox_interface.setItemText(k, _translate("MacChanger", str(i)))
            k=k+1
        self.comboBox_options.setItemText(0, _translate("MacChanger", "Print Current Mac"))
        self.comboBox_options.setItemText(1, _translate("MacChanger", "Don\'t change the vendor bytes"))
        self.comboBox_options.setItemText(2, _translate("MacChanger", "Reset to original"))
        self.comboBox_options.setItemText(3, _translate("MacChanger", "Set fully random MAC"))
        self.comboBox_options.setItemText(4, _translate("MacChanger", "Custom MAC"))
        self.comboBox_options.setItemText(5, _translate("MacChanger", "random vendor MAC of the same kind"))
        self.comboBox_options.setItemText(6, _translate("MacChanger", "Change MAC periodically"))
        c_mac_f="XX:XX:XX:XX:XX:XX"
        self.lineEdit_current.setText(_translate("MacChanger", c_mac_f))
        self.label_6.setText(_translate("MacChanger", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#21bf21;\">New MAC Address</span></p></body></html>"))
        self.lineEdit_new.setText(_translate("MacChanger", c_mac_f))
 
    def perd(self):
        _translate = QtCore.QCoreApplication.translate
        temp=1
        try:
            while True:
                try:
                    if temp==1:
                        self.lineEdit_current.setText(_translate("MacChanger",current_mac(str(self.comboBox_interface.currentText()))))
                        temp=0
                    per(str(self.comboBox_interface.currentText()))
                    self.lineEdit_new.setText(_translate("MacChanger",current_mac(str(self.comboBox_interface.currentText()))))
                    QtGui.QGuiApplication.processEvents()
                except KeyboardInterrupt:
                     break   
        except KeyboardInterrupt:
                  msgbox(":))!!","Congrats ditto pokemon found :) just kidding BYE :)")
                  exit()
                  
              
               

    def start_point(self):
        _translate = QtCore.QCoreApplication.translate
        if  os.getuid() == 0:
            c_mac=current_mac(str(self.comboBox_interface.currentText()))
            self.lineEdit_current.setText(_translate("MacChanger", c_mac))
            QtGui.QGuiApplication.processEvents()
            if self.comboBox_options.currentIndex()==4:
                a=str(self.lineEdit_a.text())
                b=str(self.lineEdit_b.text())
                c=str(self.lineEdit_c.text())
                d=str(self.lineEdit_d.text())
                e=str(self.lineEdit_e.text())
                f=str(self.lineEdit_f.text())
                build_custom_mac=a+":"+b+":"+c+":"+d+":"+e+":"+f
                customm(str(self.comboBox_interface.currentText()),build_custom_mac)

            else:
                if self.comboBox_options.currentIndex()==6:
                    msgbox("Okie!!","Set to periodic mode.{Duration 5 min.} press ctrl+c in to exit")
                    try:
                      t1 = threading.Thread(target=self.perd, args=())
                      t1.start()
                    except:
                          msgbox("Error!!","unable to start periodic mode. try to run macter.py")
                          
                    
                         
                else:    
                    optionss(str(self.comboBox_options.currentIndex()),str(self.comboBox_interface.currentText()))
                    c_mac=current_mac(str(self.comboBox_interface.currentText()))
                    self.lineEdit_new.setText(_translate("MacChanger", c_mac)) 
                    QtGui.QGuiApplication.processEvents() 
        else:
            if str(self.comboBox_options.currentIndex())!="0":
                msgbox("Opps!!","Are You Root?")
            else:
                c_mac=current_mac(str(self.comboBox_interface.currentText()))
                self.lineEdit_new.setText(_translate("MacChanger", c_mac))
                c_mac=current_mac(str(self.comboBox_interface.currentText()))
                self.lineEdit_current.setText(_translate("MacChanger", c_mac))
    

     
                    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MacChanger = QtWidgets.QMainWindow()
    ui = Ui_MacChanger()
    ui.setupUi(MacChanger)
    MacChanger.show()
    sys.exit(app.exec_())
