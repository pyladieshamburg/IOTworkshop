# Grafana

Grafana must be one of the best inventions. It is being used by a lot of companies to have their monitoring dashboards done with Grafana, and we can also use it for hobby projects.

## Installation

So let's install it on the Raspberry Pi. Check for versions [here](https://grafana.com/grafana/download?platform=arm)

In case of apt-get erros check this [page](https://chrisjean.com/fix-apt-get-update-the-following-signatures-couldnt-be-verified-because-the-public-key-is-not-available/)

```bash
wget https://dl.grafana.com/oss/release/grafana_6.2.2_armhf.deb
sudo dpkg -i grafana_6.2.2_armhf.deb

sudo apt-get update
sudo apt-get install grafana


#and then

sudo service grafana-server start

#to have grafana start at boot time
sudo update-rc.d grafana-server defaults
```

## Setting up the dashboard

Go to http://RASPBERRY_IP:3000/ and login using the default username and password — admin, admin.

Add a new InfluxDb datasource with temperature as database.

and do some panels, you can create graphs and gauges and check many more.
