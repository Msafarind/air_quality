# air_quality
acquire air quality data from sensors using raspberry pi

# THIS IS ...

# SUPPORTED SENSORS
- BME280
   - temperature
   - humidity
   - pressure
- MH-Z19B
   - co2

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
{
   "co2" : {
      "unit" : "ppm",
      "sensor" : "MH-Z19B",
      "value" : 1471
   },
   "pressure" : {
      "sensor" : "BME280",
      "unit" : "hPa",
      "value" : 1016.78853362804
   },
   "humidity" : {
      "sensor" : "BME280",
      "unit" : "%",
      "value" : 44.0666633123459
   },
   "temperature" : {
      "value" : 26.8403380069882,
      "unit" : "celsius",
      "sensor" : "BME280"
   }
}
```
