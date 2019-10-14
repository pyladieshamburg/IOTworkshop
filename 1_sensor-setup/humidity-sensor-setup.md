# Setting up and reading sensor data

For collecting the data from DHT22 sensor we will follow our previous efforts to [set up the DHT11](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/sensorsetup/reading-sensor-data-from-pi.md) and this [blog](https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/)

## Preparing your Raspberry Pi for Python

We have a fresh operating system and we need to install the tools and libraries we need on it.

Log in and run these commands:

Python 3 and pip in case they are missing

```bash
$ sudo apt-get update
$ sudo apt-get install python3-dev python3-setuptools build-essential
$ sudo apt-get install python3-pip
```

Git: we will need this for sure for when we get lots of code

```bash
$ sudo apt-get install git-core
```

Python Packages

```bash
$ python3 -m pip install --upgrade pip setuptools wheel
$ sudo pip3 install Adafruit_DHT
```

Vim or nano: unless you want to explore the ssh connection capabilities of your favored code editor.

```bash
$ sudo apt-get install vim
```

A recommended minimal configuration to be put in a file named .vimrc in your Raspberry Pi's home directory would be :

```
$ vim .vimrc

set nocompatible
set tabstop=4
set shiftwidth=4
set expandtab
set number
syntax on
```

to change tabstop and shiftwidth to taste (e.g. you might prefer two instead of the given four spaces)

Open a python3 repl (type python3 in command line) and type:

```python
import sys
import Adafruit_DHT

sensor = 22
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f}'.format(temperature, humidity))
```

This basically will work when we hook up the sensor, by connecting it to pin 4 and the sensor has to be a DHT 22.

## The Hardware part

> Before you do anything with the sensors you need to cut off Raspberry Pi power! Otherwise, there is a risk that you will damage sensor or even Raspberry Py during installation.

The 40 GPIO pins above the Raspberry Pi logo an important connection point of our Raspberry Pi to the outside world.
The GPIO pins allow us to control electric circuits from the Raspberry Pi.
We thereby can control all kinds of devices and, in particular, receive data from sensors.

![Raspberry Pins](https://www.rs-online.com/designspark/rel-assets/dsauto/temp/uploaded/githubpin.JPG)

What are all those pins?

There are two 3.3V pins in **yellow** and two 5V pins in **red**.
**Black** are the eight ground pins.
The other pins in blue, green, pink and orange are all general purpose pins that can be used for both input or output.
The non-orange ones of the pins can also communicate with special interfaces using the appropriate protocols, on top of their general purpose.
The two grey ones are reserved for other special use cases that aren't of our concern here.

For the sensor setup, we'll be using pins number 2 (5V), 6 (GND) and 7 (GPIO4).
We'll connect pin 2 (5V) to the sensor's positive pole and pin 4 (GND) to its negative pole, thus forming the basis for an electric circuit.
Pin 7 (GPIO4) will connect to the sensor's signal pin so that we can get readings.
Between the sensors positive pole and the signal pin we will also add the resistor.

The resulting circuit should look similar to this:

![Circuit diagram](http://www.circuitbasics.com/wp-content/uploads/2015/12/How-to-Setup-the-DHT11-on-the-Raspberry-Pi-Four-pin-DHT11-Wiring-Diagram.png)

Note that we could have chosen any other 3.3/5V pin instead of pin 2, any other ground pin instead of pin 4, and any other general purpose pin instead of pin 7.

And in case you wondered how the cables make a connection to the right sensor pins just by us plugging them in the same vertical row on the bread board:
all 5 hole vertical rows that we see on the bread board are connected with metal stripes.
This is how a board looks like from the bottom with the cover removed:

![Breadboard under the hood](https://cdn.sparkfun.com/r/600-600/assets/e/7/7/e/c/5175c500ce395f5a49000004.jpg)

For more details, see [https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all).

Now if you run the python code you should see some data rolling in!
