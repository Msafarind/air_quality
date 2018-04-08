import bme280
import json

bme280.get_calib_param()
if __name__ == '__main__':
	try:
		print json.dumps( bme280.readData() )
	except KeyboardInterrupt:
		pass
