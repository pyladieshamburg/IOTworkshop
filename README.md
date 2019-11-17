# IOT weather sensor tutorial 🌡️

### Description

Python is a versatile language which is being used everywhere, even in space! :rocket: For hobby IOT projects it is a great language to get familar with working with hardware while not having to be concerned with learning the syntax of a lower level language.

In this tutorial, we'll get hands on experience setting up a raspberry Pi, adding wifi settings to it and connecting to it via ssh. We will buld together a weather station by connecting a temperature sensor, then collect and log the sensor data. Next we will store the data in Influxdb and create our own Grafana dashboard to visualise the collected weather data!

Our focus will be on the building blocks necessary to set up a IOT project, setting up the hardware and debugging it. We will also learn how to use Python to collect data from hardware.

All new skills will be acquired through practical exercises. Each section will start with an explaination of the concept and then allow time for the participants to complete the implementation.

A laptop and charger is required for this workshop, the user must also have admin rights to be able to install further software required to connect to the Raspberry Pi. Participants will also ideally have a GitHub account created ahead of the tutorial and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.

*For live sessions of this workshop we will do the set up of the Raspberry Pi and software installation ahead of the workshop and only go over how this is done, this process is also completely documented below if you are following along from home*

### Audience

This tutorial is aimed at beginners to IOT projects and working with hardware. Some Python knowledge is useful but also not essential. Participants should however be familiar with using the terminal.

Participants will walk out of this tutorial with their own mini weather station IOT project, an overview of how to plan out their own project and inspiration of what further steps can be taken to expand this project. Participants will also have an understanding of how Python is used for Data collection, logging and how to visualise this data via a dashboard.

### Outline

* #### Introduction to working with hardware & Set up (45 minutes)
  - Explanation of project (high level)
  - Overview of hardware being used
  - Raspberry Pi set up & connecting it to a computer via WiFi
  - Exercise 1 *(Connecting the Pi to your computer via ssh)*
  
* #### Setting up a sensor & collecting data (40 minutes)
  - Set up a DHT22 temperature & humidity sensor
  - Writing Python for IOT projects
  - Exercise 2 *(Complete code in Python script to collect data from the sensor & log it)*
  
* #### Storing Data with InduxDB (30 minutes)
  - Collect Data and store it in InduxDB
  - Data Structures
  - Exercise 3 *(Setting up InduxDB)*

* #### Visualising Data with Grafana (30 minutes)
  - Dashboards & monitoring data
  - Building a dashboard with Grafana
  - Getting Data
  - Exercise 4 *(Create your own Dashboard)*
  
* #### Continueously collecting Data (20 minutes)
  - IOT projects dependacies (power, wifi, script running)
  - Running scripts in the background with Supervisor
  - Exercise 5 *(Complete code is script to run process with Supervisor)*

* #### Conclusion (15 minutes)
  - Summary of what was covered
  - Posible next steps
  - Inspirational project - watering your plants with Python!

Exercises will involve completing scripts and running the set up to see the expected results from the hardware.

### Introduction to hardware & Set up

Checkout the [Project Overview](PyLadiesIoTworkshop.pdf)!!

Hardware we will use in this workshop:
-Raspberry Pi 4, or 3 or 3b
-Power supply
-Micro SD card with 4-16 GB
-Micro SD to usb adapter
-Circuit breadboard
-DHT22 sensor from Adafruit with 10ohm resistor
-3 connecting wires

If you are not attending one of our live sessions where we have recieved sponsorship for hardware you can find these items to purchase online, here is a list of places you may find [them](hardware-shopping-list.md)

For setting up the raspberry Pi follow the instructions in [0_pi-setup](pi-setup/initial-setup.md)

### Setting up a sensor & collecting data

For setting up the sensor follow the instructions in [1_sensor-setup](sensor-setup/humidity-sensor-setup.md)

### Storing Data with InduxDB

For collecting data locally on the rpi follow instruction in [data-collecting-v2](data-collecting/2-influxdb.md).

### Visualising Data with Grafana

For installing and seting up a grafana dashboard follow the instructions in [data-visualization-v2](data-visualization/2-grafana.md).

### Continueously collecting Data

## Extras

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

Because we found a few typos we reccomend you do this when you are at home after the workshop, so you have the latest changes :smile: If you find a Typo or place where the documentation or code can be improved please feel free to open a PR :heart:
