# RFM9x Lora Radio - Arduino to Raspberry Pi Transmission

Bathouse project at Valencia College

This includes the Adafruit libraries of known functionality as well as additional scripts with examples.

## Pin Configuration

Pin configuration for [Raspberry Pi][pischema_page] and [Arduino][arduinoschema_page]:

![N|Solid](https://cdn-learn.adafruit.com/assets/assets/000/091/522/original/raspberry_pi_rfm9x_bb_2.png)

![N|Solid](https://cdn-learn.adafruit.com/assets/assets/000/040/615/large1024/adafruit_products_rfm69_bb.png)

### Raspberry Setup

```sh
$ sudo pip3 install --upgrade setuptools
$ sudo raspi-config
```

On Interfacing Options enable I2C And SPI

```sh
$ pip3 install RPI.GPIO
$ pip3 install adafruit-blinka
```

Run blinkatest.py to verify functionality

```sh
$ sudo pip3 install adafruit-circuitpython-rfm9x
```

Run radiotest.py and if it passes it will be ready for send and receive scripts.

[pischema_page]: https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/raspberry-pi-wiring
[arduinoschema_page]: https://learn.adafruit.com/adafruit-rfm69hcw-and-rfm96-rfm95-rfm98-lora-packet-padio-breakouts/arduino-wiring
