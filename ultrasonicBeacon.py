import time
import serial
import re
ser = serial.Serial(port='/dev/ttyACM0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
WINDOW = 5
LEGNTH = 50


def readSerial():
  sensorList1 = []
  sensorList2 = []
  x=ser.readline()
  data = x.decode()
  results = re.split('[+ \r \n]',data)
  try:
    sensorList1.append(int (results[0]))
    sensorList2.append(int (results[1]))
  except ValueError:
    print ("********")
    
  sensorList1 = sensorList1[-1*LEGNTH:]
  sensorList2 = sensorList2[-1*LEGNTH:]
  
  return sensorList1, sensorList2


def main ():
  while(True):
    sensorList1, sensorList2 = readSerial()
    print (sensorList1)
    print (sensorList2)
  
main ()
  
