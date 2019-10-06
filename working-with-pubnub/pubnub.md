### PubNub

In order to get some results really fast we are starting with a visual approach and with 3rd party tools, like PubNub which is a data stream network. We can publish the sensor readings there and then read them in nice static dashboards. For this we will follow some of the steps in their [blog](https://www.pubnub.com/blog/raspberry-pi-humidity-temperature-sensor-dashboard-dht-22-sensor/), but the code is refering to older versions so we got the updated one.

So let's make free PubNub accounts, with the free accounts we can access about 7 days of data in the past, this should be fine for showcasing this.

How it works: we publish data from the sensor readings to pubnub channels and by subscribing to these channels we can read the data from anywhere else.

![PubNub](https://www.pubnub.com/static/images/old/pubnub-galaxy.gif)

On the raspberry pi install pubnub:

```bash
sudo pip3 install pubnub
```

## Configuration

You should now fork this repo.

On your pubnub account create a new key set where you specify 7 days of storage. Create your pubnub.ini with your settings, using the template format. Update the html file with your subscriber key. As we are only publishing weather data we will leave this now in html in plain sight. Do not do this with any other data.

Clone your forked repo to your Raspberry Pi.

Copy the pubnub.ini to your raspberry pi, it will not be part of the repo.

Run the publisher:

```bash
python3 send-pubnub.py
```

You can now locally open the (dashboard)[humidity-and-temperature.html]
