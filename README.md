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
