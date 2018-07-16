import json
import mhz19b
import bme280

if __name__ == '__main__':
	air_quality = {}

	mhz19b = mhz19b.mhz19b()
	data = mhz19b.read_co2()
	for key in data.keys():
		air_quality[key] = data[key]
	# print json.dumps(air_quality)

	bme280 = bme280.bme280()
	data = bme280.readData()
	for key in data.keys():
		air_quality[key] = data[key]

	if "temperature" in air_quality.keys() and "humidity" in air_quality.keys():
		t = air_quality["temperature"]["value"]
		H = air_quality["humidity"]["value"]
		discomfort_index = 0.81 * t + 0.01 * H * (0.99 * t - 14.3) + 46.3
		air_quality["discomfort_index"] = {"value" : discomfort_index, "unit":None}

	print json.dumps(air_quality)



