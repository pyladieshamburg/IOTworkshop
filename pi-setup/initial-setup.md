## Setting up the your brand new Raspberry Pi

There are two ways to setup a new Raspberry Pi. With connection to peripherals (monitor, keyboard, mouse) or headless.
The first step of flashing an image of Raspian OS onto an SD card is the same for both ways.

In this workshop we try the headless setup and use the desktop one as backup.
Both approaches are described in our [Getting Started with Raspberry Pi](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/pisetup/raspberry-pi-setup.md)

Or on this [Headless setup blog](https://desertbot.io/blog/headless-raspberry-pi-4-ssh-wifi-setup)

### Steps to follow

- Download the operating system image provided by [RaspberryPi](https://www.raspberrypi.org/downloads/raspbian/), get the Buster with desktop or the lite one.
- Follow the [installation instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) using the belanaEtcher tool.
- Enable ssh and setup wifi (by adding the ssh file and the wpa_supplicant.conf file .. see blogs)
- Put card in the RaspberryPi .. and pray it works.. if not there might be an error or we need to try desktop setup
- Discover the IP, as a lot of pis will be connected to wifi here we cannot use the hostname so here try to discover it via ip search described in the pyladies repo.. or we do this one at a time
- Change the hostname of your raspberry pi
- Update software

## Linking to your Github account

On the raspberry pi create a private/public key pair:

```bash
ssh-keygen -t rsa
```

(enter through everything with empty password).

Your public key is created in .ssh/id_rsa.pub which you can print with the cat command:

```bash
cat .ssh/id_rsa.pub
```

Copy the output and add it to your github account under settings/SSH and GPG keys. Like this you can access your github repos from the raspberry pi without having to login all the time.
