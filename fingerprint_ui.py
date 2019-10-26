# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fingerprint.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Finger import Finger
import time
import requests



class Ui_MainWindow(object):
    def __init__(self,comport,bdrate):
        self.comport = [
                '/dev/ttyUSB0',
                '/dev/ttyUSB1',
                '/dev/ttyUSB2',
                '/dev/ttyUSB4',
                '/dev/ttyUSB5',
                '/dev/ttyUSB6',
                'COM0',
                'COM1',
                'COM3',
                'COM4',
                'COM6',
            ]
        self.bdrate = [
            
                '57600',
                '9600',
          
            ]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnsendttermina = QtWidgets.QPushButton(self.centralwidget)
        self.btnsendttermina.setGeometry(QtCore.QRect(180, 500, 171, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnsendttermina.setFont(font)
        self.btnsendttermina.setAutoDefault(True)
        self.btnsendttermina.setDefault(False)
        self.btnsendttermina.setFlat(False)
        self.btnsendttermina.setObjectName("btnsendttermina")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 360, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 130, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 210, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.linelocation = QtWidgets.QLineEdit(self.centralwidget)
        self.linelocation.setGeometry(QtCore.QRect(50, 240, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.linelocation.setFont(font)
        self.linelocation.setObjectName("linelocation")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 210, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 280, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.linepoid = QtWidgets.QLineEdit(self.centralwidget)
        self.linepoid.setGeometry(QtCore.QRect(50, 320, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.linepoid.setFont(font)
        self.linepoid.setObjectName("linepoid")
        self.lineamount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineamount.setGeometry(QtCore.QRect(50, 390, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineamount.setFont(font)
        self.lineamount.setObjectName("lineamount")
        self.btnclear = QtWidgets.QPushButton(self.centralwidget)
        self.btnclear.setGeometry(QtCore.QRect(470, 150, 131, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnclear.setFont(font)
        self.btnclear.setObjectName("btnclear")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 120, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(710, 120, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.linefrom = QtWidgets.QLineEdit(self.centralwidget)
        self.linefrom.setGeometry(QtCore.QRect(620, 150, 41, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.linefrom.setFont(font)
        self.linefrom.setObjectName("linefrom")
        self.lineto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineto.setGeometry(QtCore.QRect(700, 150, 41, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineto.setFont(font)
        self.lineto.setObjectName("lineto")
        self.txtmessage = QtWidgets.QTextEdit(self.centralwidget)
        self.txtmessage.setGeometry(QtCore.QRect(460, 220, 291, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtmessage.setFont(font)
        self.txtmessage.setObjectName("txtmessage")
        self.btnenrol = QtWidgets.QPushButton(self.centralwidget)
        self.btnenrol.setGeometry(QtCore.QRect(400, 500, 151, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnenrol.setFont(font)
        self.btnenrol.setObjectName("btnenrol")
        self.lineaccno = QtWidgets.QLineEdit(self.centralwidget)
        self.lineaccno.setGeometry(QtCore.QRect(50, 170, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineaccno.setFont(font)
        self.lineaccno.setObjectName("lineaccno")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineport = QtWidgets.QComboBox(self.centralwidget)
        self.lineport.setGeometry(QtCore.QRect(270, 160, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineport.setFont(font)
        self.lineport.setProperty("currentText", "")
        self.lineport.setObjectName("lineport")
        self.linebrate = QtWidgets.QComboBox(self.centralwidget)
        self.linebrate.setGeometry(QtCore.QRect(270, 250, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.linebrate.setFont(font)
        self.linebrate.setObjectName("linebrate")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(300, 340, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineamount_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineamount_2.setGeometry(QtCore.QRect(50, 450, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineamount_2.setFont(font)
        self.lineamount_2.setInputMask("")
        self.lineamount_2.setObjectName("lineamount_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(80, 430, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnsendttermina.setText(_translate("MainWindow", "Send  to Terminal"))
        self.label.setText(_translate("MainWindow", "Amount"))
        self.label_2.setText(_translate("MainWindow", "Fingerprint settings"))
        self.label_3.setText(_translate("MainWindow", "Port"))
        self.label_4.setText(_translate("MainWindow", "b-rate"))
        self.label_5.setText(_translate("MainWindow", "Pos Information"))
        self.label_6.setText(_translate("MainWindow", "Location"))
        self.label_7.setText(_translate("MainWindow", "Pos ID"))
        self.btnclear.setText(_translate("MainWindow", "Clear fingerprints"))
        self.label_8.setText(_translate("MainWindow", "From"))
        self.label_9.setText(_translate("MainWindow", "To"))
        self.btnenrol.setText(_translate("MainWindow", "Enrol Fingerprint"))
        self.label_10.setText(_translate("MainWindow", "Account No"))
        self.label_11.setText(_translate("MainWindow", "POS TERMINAL"))
        self.label_12.setText(_translate("MainWindow", "RV 307 "))
        self.label_13.setText(_translate("MainWindow", "Password"))
        self.lineamount_2.setStyleSheet('lineedit-password-character: 9679')
        self.btnsendttermina.clicked.connect(self.on_click)
        self.btnclear.clicked.connect(self.delete)
        self.lineport.addItems(self.comport)
        self.linebrate.addItems(self.bdrate)

    def on_click(self):
        self.txtmessage.clear

        port = str(self.lineport.currentText())
        ttl = str(self.linebrate.currentText())

        if(self.lineaccno.text() == "" or self.linelocation.text() == "" or self.lineamount.text() == "" or self.linepoid.text() == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText('Fill in all Pos Information fields')
            msg.setWindowTitle("Error")
            msg.exec_()
        else :
            #before fingerprint is scanned authenticate details
            payload = {'username': self.lineaccno.text() ,'password':self.lineamount_2.text()}
            # r = requests.post("http://localhost/fingerprint/public/reports/pyapi", data=payload)
            r = requests.post("http://localhost/fingerprint/public/clients/loginapi", data=payload)
            result = r.json()
            if(result["save"]== 'true'):


                if(port != "" and ttl != ""):
                    # try :
                    f=Finger(port,ttl,self.linelocation.text() ,self.linepoid.text(),self.lineamount.text(),self.lineaccno.text())  

                    self.txtmessage.clear
                    self.txtmessage.setText("Scan finger print")
                    time.sleep(2)
                    
                    # print("MainWindow")
                    
                    
                    

                    
                    if (str(f.match) != "-1"):
                      

                        self.txtmessage.setText("Finger value:"+str(f.match()))
                        # msg = QtWidgets.QMessageBox()
                        # msg.setIcon(QtWidgets.QMessageBox.Information)
                        # msg.setText("Success")
                        # msg.setInformativeText('Fingerprint verified')
                        # msg.setWindowTitle("Finger Found at:"+str(f.match()))
                        # msg.exec_()
                    # except Exception as err:
                    #     self.txtmessage.setText("Error Encountered \n"+str(err))
                elif (self.linelocation.text() ==  ""):
                    self.txtmessage.setText("Enter Location")
                elif (self.linepoid.text() ==  ""):
                    self.txtmessage.setText("Enter Pos ID")
                elif (self.lineamount.text() ==  ""):
                    self.txtmessage.setText("Enter Amount")

                else:
                    self.txtmessage.setText("fill in com port and baud rate clear\n eg /dev/ttyUSB0 ")

            elif (result["save"]== 'false'):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Error")
                msg.setInformativeText('Invalid pin or account number')
                msg.setWindowTitle("Login error")
                msg.exec_()


    def delete(self):
        port = str(self.lineport.currentText())
        ttl = str(self.lineport.currentText())
        
        try :
            f=Finger(port,ttl,0,0,0,0)  
            if self.linefrom.text() != "" and self.lineto.text() != "" :
                fid=self.linefrom.text()
                n=self.lineto.text()
                f.delete(fid,n)
                self.txtmessage.setText(" Fingerprint(s) Successfully Deleted ")
            else :
                self.txtmessage.setText("fill in from and to sections to clear")

        except Exception as err:
                self.txtmessage.setText("Error Encountered \n"+str(err))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(0,0)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())