# Collecting the data

In order to actually make use of this data it would be really cool to store it. There are endless ways to do this in various types of databases in more or less complex ways.

One way to do this though, bringing us in the devopsy realm, is with [influxdb](https://www.influxdata.com), [telegraf](https://www.influxdata.com/time-series-platform/telegraf/) and [grafana](https://grafana.com) (we describe this part later in the second [visualization module](../data-visualization/2-grafana.md)), following steps from this [tutorial](https://www.terminalbytes.com/temperature-using-raspberry-pi-grafana/) with some modifications as of course things are updated super fast in this day and age.

InfluxDb is a time series database thus ideal for collecting sensor data and other metrics like CPU and Memory Usage. Writing directly to influxdb is a bit more work that we will circumvent by writing to a log file from which we will read via telegraf.

First of all we will uncomment the lines of code in our `send-pubnub.py` script that refer to logging. This means that we will log the measurements and at the same time keep sending them to pubnub. We will log them into a log file which we specify. (Its also important to check that this log file is added to .gitignore)

Create a new folder for the logs on your RaspberryPi run the following command:

```bash
mkdir -p /home/pi/logs/weather/
```

Code to uncomment:

```python
import logging
logging.basicConfig(filename='/home/pi/logs/weather/temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)

#and later

print("publish timetoken: %d" % envelope.result.timetoken)
#logging
logging.info('Temp={0:0.1f} C and Humidity={1:0.1f} %'.format(t, h))
#wait 5 mins
```

You can deploy this now on the rasperry pi and restart the supervisor process:

```bash
sudo service supervisor restart data-collector
```

## InfluxDb and telegraf intallation

Installation steps on the Raspberry Pi.

```bash
wget -qO- https://repos.influxdata.com/influxdb.key | sudo tee /etc/apt/sources.list.d/influxdb.list test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt-get update && sudo apt-get install influxdb
sudo service influxdb start

#verify influxdb is running with the following command.
sudo service influxdb status
```

For telegraf we need to find the suitable version and [download](https://github.com/influxdata/telegraf/releases) it, something with armhf for Debian.

By running

```bash
cat /etc/os-release
```

we know that the Linux distribution installed on the RPi is Debian.

```bash
wget telegraf_1.12.2-1_armhf.deb

sudo dpkg -i telegraf_1.12.2-1_armhf.deb
```

## Log parsing

Telegraf parses log data via grok, which is a powerful parser used by all sorts of monitoring applications, thankfully there are online [debuggers](https://grokdebug.herokuapp.com).

To run this telegraf:

```bash
nohub telegraf --config temperature-logging.conf
```

use nohub to run in the background

# Checking out the data

If it all works we should be able to look at the data. <b>If localhost:8086 renders a 404 then it means InfluxDb works.</b>

From command line run:

```bash
influx
> show databases
> use temperature
> show measurements
> select * from room_temperature_humidity
> exit
```

To export data from influx you can run:

```bash
influx -database 'temperature' -execute 'SELECT * FROM measurements' -format csv > test.csv
```

It will be exported to a file called `test.csv`.
