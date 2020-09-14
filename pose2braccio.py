#!/usr/bin/env python3
import serial, time
ser = serial.Serial('COM5')
ser.baudrate = 115200

f = open("path.txt", "r")
for x in f:
   xS = x.strip()
   if (xS.startswith("//")):
      continue
   xSr = xS.replace("(",'').replace(")",'').replace("CMD",'').replace(" ",'');
   xSrA = xSr.split(",")
   #print(xSrA)
   time.sleep(int(xSrA.pop()) / 1000)
   xSrAs = "P" + ",".join(xSrA) + "\n"
   print("Sequence: " + xSrAs)
   ser.write(str.encode(xSrAs))
