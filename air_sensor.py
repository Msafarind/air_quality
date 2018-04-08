import json
import mhz19b
import bme280

if __name__ == '__main__':
	air_quality = {}

	mhz19b = mhz19b.mhz19b()
	data = mhz19b.read_co2()
	for key in data.keys():
		air_quality[key] = data[key]

	bme280 = bme280.bme280()
	data = bme280.readData()
	for key in data.keys():
		air_quality[key] = data[key]

	print json.dumps(air_quality)



