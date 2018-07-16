# coding: utf-8
#
# originally from 
# https://qiita.com/UedaTakeyuki/items/c5226960a7328155635f
# 
# about MH-Z19B
# http://www.winsen-sensor.com/d/files/infrared-gas-sensor/mh-z19b-co2-ver1_0.pdf
# 
# # enable serial on your raspberry pi before use
# sudo raspi-config nonint do_serial 0
import serial
import time
import subprocess
class mhz19b():
  tty = 'ttyS0'

  # def __init__(self, *args):
  #     super(mh-z19b, self).__init__(*args))
  def __init__(self, tty='ttyS0'):
    self.tty = tty

  def read_co2(self):
    stop_getty  = 'sudo systemctl stop serial-getty@' + self.tty + '.service'
    start_getty = 'sudo systemctl start serial-getty@' + self.tty + '.service'
    try:
      subprocess.call(stop_getty, stdout=subprocess.PIPE, shell=True)
      ser = serial.Serial('/dev/' + self.tty ,
                          baudrate=9600,
                          bytesize=serial.EIGHTBITS,
                          parity=serial.PARITY_NONE,
                          stopbits=serial.STOPBITS_ONE,
                          timeout=1.0)
      while 1:
        result=ser.write("\xff\x01\x86\x00\x00\x00\x00\x00\x79")
        s=ser.read(9)
        if s[0] == "\xff" and s[1] == "\x86":
          return {'co2': {"value":ord(s[2])*256 + ord(s[3]), 'unit':'ppm', 'sensor':'MH-Z19B'}}
        break
    except:
      return {}
      print ("failed to read co2 value. maybe lacks permission to read/write serial")
    finally:
        subprocess.call(start_getty, stdout=subprocess.PIPE, shell=True)

  # ZERO POINT CALIBRATION
  def zero_point_calibration(self, force=False):
    stop_getty  = 'sudo systemctl stop serial-getty@' + self.tty + '.service'
    start_getty = 'sudo systemctl start serial-getty@' + self.tty + '.service'
    try:
      subprocess.call(stop_getty, stdout=subprocess.PIPE, shell=True)
      ser = serial.Serial('/dev/' + self.tty ,
                          baudrate=9600,
                          bytesize=serial.EIGHTBITS,
                          parity=serial.PARITY_NONE,
                          stopbits=serial.STOPBITS_ONE,
                          timeout=1.0)
      result=ser.write("\xff\x01\x87\x00\x00\x00\x00\x00\x78")
      s=ser.read(9)
    finally:
      subprocess.call(start_getty, stdout=subprocess.PIPE, shell=True)

  def get_checksum(self, packets):
    packets = bytearray([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
    packets = bytearray([0xFF, 0x01, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
    checksum = (0xFF - ((packets[1]+packets[2]+packets[3]+packets[4]+packets[5]+packets[6]+packets[7])% 256))+1
    return checksum
