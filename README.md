# air_quality
acquire air quality data from sensors using raspberry pi

# PRE-REQUESTIES
- install libraries
```
sudo apt-get install python-serial python-smbus python-pip
```
```
sudo pip install smbus2
```
- enable i2c
```
sudo raspi-config nonint do_i2c 0
```

# USAGE
```
sudo python air_sensor.py 
```
# OUTPUT EXAMPLE
```
{"pressure": {"sensor": "BME280", "unit": "hPa", "value": 1016.6021547924195}, "co2": {"sensor": "MH-Z19B", "unit": "ppm", "value": 1244}, "temperature": {"sensor": "BME280", "unit": "celsius", "value": 26.80997100791428}, "humidity": {"sensor": "BME280", "unit": "%", "value": 40.38159699446065}}
```
