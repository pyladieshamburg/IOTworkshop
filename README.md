# IOT weather sensor workshop

In this workshop we will learn how to do many things! Set up a raspberry Pi, add wifi settings to it and connect with ssh, connect a temperature sensor, send data to an online time series called PubNub, set up a simple website with visualisation. Then go more complex and store the data in Influxdb and crate a Grafana dashboard.

Tools you need for this workshop:

- Raspberry Pi 4, or 3 or 3b
- Power supply
- Micro SD card with 4-16 GB
- Micro SD to usb adapter
- Circuit breadboard
- DHT22 sensor from Adafruit with 10ohm resistor
- 3 connecting wires

For setting up the raspberry Pi follow the instructions in [pi-setup](pi-setup/initial-setup.md)
For setting up the sensor follow the instructions in [pi-setup](sensor-setup/humidity-sensor-setup.md)

### Part 1

For sending data to pubnub and visualize it, follow the instructions for data collection in [data-collecting-v1](data-collecting/1-pubnub.md).

For visualizing the data and setting up a static website check the instructions in [data-visualization-v1](data-visualization/1-pubnub-viz.md).

### Part 2

For collecting data locally on the rpi follow instruction in [data-collecting-v2](data-collecting/2-influxdb.md).
For installing and seting up a grafana dashboard follow the instructions in [data-visualization-v2](data-visualization/2-grafana.md).
