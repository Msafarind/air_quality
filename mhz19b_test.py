import sys
import mhz19b
import json

if __name__ == '__main__':
  mhz19b = mhz19b.mhz19b()
  value = mhz19b.read_co2()
  if not value == None:
    print json.dumps( value )
