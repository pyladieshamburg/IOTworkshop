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

For setting up the raspberry Pi follow the instructions in [0_pi-setup](pi-setup/initial-setup.md)
For setting up the sensor follow the instructions in [1_sensor-setup](sensor-setup/humidity-sensor-setup.md)

### Part 1

For sending data to pubnub and visualize it, follow the instructions for data collection in [data-collecting-v1](data-collecting/1-pubnub.md).

For visualizing the data and setting up a static website check the instructions in [data-visualization-v1](data-visualization/1-pubnub-viz.md).

### Part 2

For collecting data locally on the rpi follow instruction in [data-collecting-v2](data-collecting/2-influxdb.md).
For installing and seting up a grafana dashboard follow the instructions in [data-visualization-v2](data-visualization/2-grafana.md).

### A few useful Git commands

During the workshop we made individual forks of the PyLadies Hamburg version of this repo. Changes made to the original version will not automatically be updated in our forks. To update our fork we can use the following commands to pull from the "upstream" repo.

```bash
# set the upstream
git remote add upstream https://github.com/pyladieshamburg/IOTworkshop.git
# to check this run
git remote -v
# the output should look like this
> origin    https://github.com/<YOUR_USERNAME>/IOTworkshop.git (fetch)
> origin    https://github.com/<YOUR_USERNAME>/IOTworkshop.git (push)
> upstream  https://github.com/pyladieshamburg/IOTworkshop.git (fetch)
> upstream  https://github.com/pyladieshamburg/IOTworkshop.git (push)
# origin is your fork, upstream is the original pyladieshamburg version
# fetch upstream
git fetch upstream
# merge changes from upstream to our fork
git merge upstream/master
# note if you have changes to your fork you have not yet commited you may be asked to commit or stash them.
# to stash run
git stash
# once you have successfully merged the upstream following the instructions above you can get those change back with
git stash pop
```

Because we found a few typos we reccomend you do this when you are at home after the workshop, so you have the latest changes :smile:

# Visual Checklist

Checkout the [Checklist](PyLadiesIoTworkshop.pdf)!!
