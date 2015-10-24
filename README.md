# Air quality sensor data cleaner

A data parser written in Python to select only the data when the Carbon Monoxide sensor is just about to turn off its heater.

It also reduces the accuracy of the location data to 3 decimal places (100 metres), and averages the sensor data at those locations.

There's also the ability to output Particles data using the parser, which takes all data collected while the Carbon Monoxide heater is on - as the Particle sensor is noisy when the CO sensor is off.

## Input/output

The script takes a CSV file called `latest.csv` and outputs a file `latest-clean.csv`

The fields that the file expects are:

`deviceid, timestamp, latitude, longitude, humidity, temperature, particles, carbonmonoxide, heaterOn`

Where the `deviceid` is set to `1` for Simon's data, and `2` for Damien's data.

## Other parts of this project

* The Arduino sensor sketch: <https://github.com/sighmon/bike_air_quality_sensors>
* The iOS app: <https://github.com/sighmon/BikeAirQualitySensorsiOS>
* The Android app: <https://github.com/33d/bike-air-sensor-logger>