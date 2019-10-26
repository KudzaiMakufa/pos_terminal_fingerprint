import struct as st
import serial as ser
import time,sys
from PIL import Image
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
head=[0xef01,0xffffffff,0x01]
class FingerPrint():
    def __init__(self,ttl,port):
        self.s=ser.Serial(ttl,port);
    def pack(self,data):
       a=sum(head[-1:]+data)
       pack_str='!HIB'+'B'*len(data)+'H'
       l=head+data+[a]
       d=st.pack(pack_str,*l)
       return d
    def unpack(self,data):
       ret=[]
       print(data)
       ret.extend(st.pack('!H',data[4]))
       return ret[1]
    def readpac(self,):
        time.sleep(1)
        w=self.s.inWaiting()
        ret=[]
        if(w>=9):
           sd=self.s.read(9)
           ret.extend(st.unpack('!HIBH',sd))
           ln=ret[-1]
           time.sleep(1)
           w=self.s.inWaiting()
           if w>=ln:
              sd=self.s.read(ln)
              form='!'+'B'*(ln-2)+'H'
              ret.extend(st.unpack(form,sd))
           return ret
    def writepac(self,data):
       d=self.pack(data)
       #print(repr(d))
       self.s.write(d)
    def getimg(self):
       data=[0x00,0x03,0x01]
       self.writepac(data)
       d=self.readpac()
       x=list(d)[4]
       if(x==0):
          print("Fingerprint Taken")
       elif(x==2):
          print("No Finger Found")
    def genchar(self,v):
        if v==1:
            data=[0x00,0x04,0x02,0x01]
        else:
            data=[0x00,0x04,0x02,0x02]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          return 0
          #print("Converted to Charfile")
        elif(x==6):
          print("Fingerprint Corrupt")
        else:
            print(x)
    def regmodel(self):
        data=[0x00,0x03,0x05]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Model Registered")
          return 1
        elif x==10:
          print("No File in Charbuffer")
          return 0
        else:
            print(x)
            return 0
    def store(self,fid):
        data=[0x00,0x06,0x06,0x01,0x00,int(fid)]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Fingerprint Stored at:-"+fid)
        else:
            print(x)
    def search():
        data=[0x00,0x08,0x04,0x01,0x00,0x00,0x00,0x10]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          #print("Fingerprint Found:-")
          #print("ID:")
          #print(list(d)[6])
          msg = QtWidgets.QMessageBox()
          msg.setIcon(QtWidgets.QMessageBox.Information)
          msg.setText("Fingerprint Matched")
          msg.setInformativeText('Authenticated')
          msg.setWindowTitle("")
          msg.exec_()
          return list(d)[6]
        elif x==9:

            print("No Match Found")
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Fingerprint not found")
            msg.setInformativeText('Alert Send')
            msg.setWindowTitle("")
            msg.exec_()

            #print(d)
            return -1
        else:
            print(x)
            print(d)
            return -1
    def searchapi(self,location ,amount ,posid,account_no):
        data=[0x00,0x08,0x04,0x01,0x00,0x00,0x00,0x10]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          #print("Fingerprint Found:-")
          #print("ID:")
          #print(list(d)[6])
          msg = QtWidgets.QMessageBox()
          msg.setIcon(QtWidgets.QMessageBox.Information)
          msg.setText("Fingerprint Matched")
          msg.setInformativeText('Authenticated')
          msg.setWindowTitle("")
          msg.exec_()
          return list(d)[6]
        elif x==9:
            #update to 
            print("No Match Found")
          

            try:
              
              #check for unusual activity

              #activity= requests.post("http://www.pksystems.co.zw/fingerprint/public/reports/analyze", data=payload)
            
              payload = {'location': location ,'merchant_id':posid,'card_no':amount,'city':location ,'account_number':account_no}
             # r = requests.post("http://localhost/fingerprint/public/reports/pyapi", data=payload)
              r = requests.post("http://localhost/fingerprint/public/reports/pyapi", data=payload)
              result = r.json()

              if(result["save"]== 'true'):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Fingerprint not found")
                msg.setInformativeText('Alert Send to Client')
                msg.setWindowTitle("")
                msg.exec_()
              elif (result["save"]== 'false'):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Behaviour normal")
                msg.setInformativeText('False alarm .Sending OTP via email')
                msg.setWindowTitle("")
                msg.exec_()
              elif (result["save"]== 'notexist'):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Invalid account number")
                msg.setInformativeText('Register on portal')
                msg.setWindowTitle("")
                msg.exec_()
              else :
                print(0);


              print (result["save"])



            except Exception as err :
              print("test"+str(err))
              if(str(err) == 'Extra data: line 1 column 5 (char 4)'):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Fingerprint not found")
                msg.setInformativeText('Alert Send to Client')
                msg.setWindowTitle("")
                msg.exec_()
              else :
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Warning")
                msg.setInformativeText("Error \n"+str(err))
                msg.setWindowTitle("")
                msg.exec_()

             
              
            
            #print(d)
            return -1
        else:
            print(x)
            print(d)
            return -1
    def delete(self,fid,n):
        data=[0x00,0x07,0x0c,0x00,int(fid),0x00,int(n)]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          msg = QtWidgets.QMessageBox()
          msg.setIcon(QtWidgets.QMessageBox.Information)
          msg.setText("Success")
          msg.setInformativeText(str(n)+" Fingerprint(s) deleted")
          msg.setWindowTitle("")
          msg.exec_()
         

        else:
            print(x)
    def empty(self):
        data=[0x00,0x03,0x0d]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("All Fingerprint Deleted")
        else:
            print(x)
    def upimg(self):
        data=[0x00,0x03,0x0a]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Ready to transfer")
          d=self.readpac()
          print(list(d)[10:])
          return str(d)
        else:
            print("Failed")
            print(x)
    def tz(self):
        data=[0x00,0x04,0x02,0x01]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          return 0
          #print("Charfile Created")
        elif x==21:
            print("Failed")
        else:
            print(x)
    def upchar(self):
        data=[0x00,0x04,0x08,0x01]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Charfile Ready")
          d=self.readpac()
          #print(list(d[5:]))
          print(len(list(d[5:])))
          im=Image.frombytes('L',(16,16),str(d[5:]))
          im.show()
        elif x==21:
            print("Failed")
        else:
            print(x)
    def setaddress(self):
        data=[0x00,0x07,0x15,0xff,0xff,0xff,0xff]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
