## Setting up the your brand new Raspberry Pi

There are two ways to setup a new Raspberry Pi. With connection to peripherals (monitor, keyboard, mouse) or headless.
The first step of flashing an image of Raspian OS onto an SD card is the same for both ways.

In this workshop we try the headless setup and use the desktop one as backup.
Both approaches are described in our [Getting Started with Raspberry Pi](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/pisetup/raspberry-pi-setup.md)

Or on this [Headless setup blog](https://desertbot.io/blog/headless-raspberry-pi-4-ssh-wifi-setup)

### Steps to follow

- Download the operating system image provided by [RaspberryPi](https://www.raspberrypi.org/downloads/raspbian/), get the Buster with desktop or the lite one.
- Follow the [installation instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) using the belanaEtcher tool.
- Enable ssh and setup wifi: write empty ssh file and updated [wpa_supplicant.conf])(wpa_supplicant.conf) into the boot folder
- Put card in the RaspberryPi .. and pray it works.. if not there might be an error or we need to try desktop setup
- If this is your only raspberry pi in your network then you might be able to it via it's hostname:

```bash
$ ssh-keygen -R raspberrypi.local #this might throw a warning.. ignore
$ ssh pi@raspberrypi.local #password is raspberry
```

- Discover the IP, as a lot of pis will be connected to wifi here we cannot use the hostname so here try to discover it via ip search. First you need to get your local IP either from checking your network information or via the command:

```bash
$ ifconfig
```

With this ip run nmap (you might need to install it locally first):

```bash
$ nmap -sn 192.168.0.5/24
```

- Connect to your raspberry pi

```bash
$ ssh pi@IP #password is raspberry if this is your pi
```

- Change the hostname of your raspberry pi

```bash
#once connected run this to change the host
$ sudo raspi-config # go to network something then select change network (mouse won't work here, it will reboot after this)
#connect again
$ ssh pi@newname.local
$ sudo raspi-config # now change password
$ sudo reboot
```

- Update software

```bash
$ sudo apt-get update -y
$ sudo apt-get upgrade -y
```

## Linking to your Github account

On the raspberry pi create a private/public key pair:

```bash
$ ssh-keygen -t rsa
```

(enter through everything with empty password).

Your public key is created in .ssh/id_rsa.pub which you can print with the cat command:

```bash
$ cat .ssh/id_rsa.pub
```

Copy the output and add it to your github account under settings/SSH and GPG keys. Like this you can access your github repos from the raspberry pi without having to login all the time.

# Liniking your local machine to your raspberry pi

In order to log on to the raspberry pi without having to always type in the password you can repeat the above step from your local machine...

so now run

```bash
$ ssh-keygen -t rsa
```

and then, still on your local machine, run:

```
$ ssh-copy-id pi@newname.local #use your hostname here, and this will prompt for password
```
