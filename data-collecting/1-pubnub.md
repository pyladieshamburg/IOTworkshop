### PubNub

In order to get some results really fast we are starting with a visual approach and with 3rd party tools, like PubNub which is a data stream network. We can publish the sensor readings there and then read them in nice static dashboards. For this we will follow some of the steps in their [blog](https://www.pubnub.com/blog/raspberry-pi-humidity-temperature-sensor-dashboard-dht-22-sensor/), but the code is refering to older versions so we got the updated one.

So let's [make free PubNub accounts](https://dashboard.pubnub.com/signup?).

After creating your account add a new key, you can choose a personalized name for your key, but it's necessary to enable the following configurations:

![config_pubnub](pubnub-config-page.png)

How it works: we publish data from the sensor readings to pubnub channels and by subscribing to these channels we can read the data from anywhere else.

![PubNub](https://www.pubnub.com/static/images/old/pubnub-galaxy.gif)

On the raspberry pi install pubnub:

```bash
sudo pip3 install pubnub
```

## Configuration

You should now either clone or fork this repo.

**To clone the repo:**

```bash
# using SSH
git clone git@github.com:pyladieshamburg/IOTworkshop.git
```

**To fork the repo:**

You should see a small button written "Fork" in the home page of this repository (https://github.com/pyladieshamburg/IOTworkshop).

**Configuring the PubNub settings:**

Create a new file anywhere you want called `pubnub.ini` with your settings, using the template format. The template format is this:

```
[DEFAULT]
subscribe_key = my_sub_...
publish_key = my_pub_...
```

You should add your sub and pub keys that you can find in the PubNub website exactly how the template states. Do not add any quotes or change it in any way.

Update the html file with your subscriber key. The html file has two lines that needs to be changed, it's necessary that you add your sub keys there.

As we are only publishing weather data we will leave this now in html in plain sight. Do not do this with any other data.

**Adding the information to your RaspberryPi:**

Add this Github directory to your Raspberry. You can either clone it again in your Rasp or just copy and paste your current directory there.

Copy the `pubnub.ini` to your RaspberryPi, it will not be part of the repo.

The `pubnub.ini` contain sensitive information and you might want to leave it out of the internet not uploading it to your git repository. To do that it's necessary to create a `.gitignore` file inside your Github repository. Open the file and write `pubnub.ini` in it. And that's it! This file tells git which files it should ignore and pretend that are not there, as the name suggests.

**Run the publisher:**

```bash
python3 send-pubnub.py
```

This will publish data every 5 minutes.

Pro tip: you can change the update frequency by changing the `time.sleep(300)` function. 300 here stands for 300 seconds.



## Running continuously

If we now close the python repl, or disconnect from the raspberry pi our python command will die. So how do we do this that it doesn't?

There are several tools for this and we will look now at [supervisor](https://uctrl.dev/raspberry-pi-iot-setup/).
And more info on what we can do with it at this [blog](https://medium.com/@jayden.chua/use-supervisor-to-run-your-python-tests-13e91171d6d3).

Following the instructions, install supervisor and update the config (using [user pi](https://www.makeuseof.com/tag/raspbian-default-password/)).

```
bash
sudo vim /etc/supervisor/conf.d/data-collector.conf

[program:data-collector]
command=python3 send-pubnub.py
directory=/home/pi/repos/iotworkshop/starting-small
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

If you want you can also add the supervisor gui, by editing the config.
