import os
import time
import sys
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException
import Adafruit_DHT as dht
import configparser

#import logging
#logging.basicConfig(filename='/home/pi/logs/weather/temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO) 


config = configparser.ConfigParser()
config.read('pubnub.ini')

pnconfig = PNConfiguration()
 
pnconfig.subscribe_key = config['DEFAULT']['subscribe_key']
pnconfig.publish_key = config['DEFAULT']['publish_key']

pubnub = PubNub(pnconfig)

pubnub.subscribe().channels('tempeon').execute()
pubnub.subscribe().channels('humeon').execute()

def callback(message):
    print(message)

while True:
    try:
        h,t = dht.read_retry(dht.DHT11, 4)
        envelope = pubnub.publish().channel('tempeon').message({
                'x': time.time(),
                'temperature_celsius': t}).sync()
        print("publish timetoken: %d" % envelope.result.timetoken)
        envelope2 = pubnub.publish().channel('humeon').message({
                'x': time.time(),
                'humidity': h
            }).sync()
        print("publish timetoken: %d" % envelope.result.timetoken)
        #logging
        #logging.info('Temp={0:0.1f} C and Humidity={1:0.1f} %'.format(t, h)) 
        #wait 5 mins
        time.sleep(300)
    except PubNubException as e:
        handle_exception(e)

