### PubNub

In order to get some results really fast we are starting with a visual approach and with 3rd party tools, like PubNub which is a data stream network. We can publish the sensor readings there and then read them in nice static dashboards. For this we will follow some of the steps in their [blog](https://www.pubnub.com/blog/raspberry-pi-humidity-temperature-sensor-dashboard-dht-22-sensor/), but the code is refering to older versions so we got the updated one.

So let's [make free PubNub accounts](https://dashboard.pubnub.com/signup?), with the free accounts we can access about 7 days of data in the past, this should be fine for showcasing this.

How it works: we publish data from the sensor readings to pubnub channels and by subscribing to these channels we can read the data from anywhere else.

![PubNub](https://www.pubnub.com/static/images/old/pubnub-galaxy.gif)

On the raspberry pi install pubnub:

```bash
sudo pip3 install pubnub
```

## Configuration

You should now fork this repo.

```bash
# using SSH
git clone git@github.com:pyladieshamburg/IOTworkshop.git
```

On your pubnub account create a new key set where you specify 7 days of storage. Create your pubnub.ini with your settings, using the template format (template file is in this directory among with others: [pubnub_template.ini](./pubnub_template.ini)). Later (in visualization section) you will need to update the html file with your subscriber key. As we are only publishing weather data we will leave this now in html in plain sight. Do not do this with any other data.

Clone your forked repo to your Raspberry Pi.

Copy the pubnub.ini to your raspberry pi, it will not be part of the repo.

Run the publisher:

```bash
python3 send-pubnub.py
```

This will publish data every 5 minutes.


## Running continuously

If we now close the python repl, or disconnect from the raspberry pi our python command will die. So how do we do this that it doesn't?

There are several tools for this and we will look now at [supervisor](https://uctrl.dev/raspberry-pi-iot-setup/).
And more info on what we can do with it at this [blog](https://medium.com/@jayden.chua/use-supervisor-to-run-your-python-tests-13e91171d6d3).

First you need to install supervisor on your RaspberryPi with the following command
```
$ sudo apt-get install supervisor
```
Now you can create the config in the following path with the content shown below (using [user pi](https://www.makeuseof.com/tag/raspbian-default-password/)).

> If you cloned repo not to the home directory (`~/` which is really `/home/pi`) don't forget to edit the path in the config below!

```
bash
sudo vim /etc/supervisor/conf.d/data-collector.conf

[program:data-collector]
command=python3 send-pubnub.py
directory=/home/pi/IOTworkshop/data-collecting
autostart=true
autorestart=true
user=pi
```

Starting the service from cli:

```bash
sudo supervisorctl
```

```bash
supervisor > reread
supervisor > add data-collector
supervisor > status
```

If you want you can also add the supervisor gui, by editing the config (just follow instructions from blog-post mentioned before).
