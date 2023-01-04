# Raspberry Pi Pico RP2040 I2C Demo for Matrix Orbital Displays
A very quick RP2040 demo using the onboard temperature probe to display the temperature on an I2C Matrix Orbital Display using Python

Browse our I2C LCD, I2C TFT, I2C VFD products:
[**https://www.matrixorbital.com/communication-protocol/i2c**](https://www.matrixorbital.com/communication-protocol/i2c)

## Hardware & Software

[**OK162-12, 2x16 I2C OLED Display:**](https://www.matrixorbital.com/ok162-12) this demo should work on all Matrix Orbital Alpha-Numeric displays

[**Raspberry Pi Pico RP2040:**](https://www.raspberrypi.com/products/raspberry-pi-pico/) Flexible Microcontroller Board

[**BBC:**](https://www.matrixorbital.com/bbc-breadboard-cable) 4 pin leads to a 4 pin friction lock 2.54mm

[**Thonny:**](https://thonny.org/) An integrated development environment for Python that is designed for beginners

## Connecting the Hardware

<img src=WireDiagram.png></img>

Connect a Pi Pico RP2040 to a Matrix Orbital I2C Display:
RP2020 --> Display
1. Connect PIN 40 VBUS to PIN 1 VIN
2. Connect PIN 2 I2C0 SCL to PIN 2 SCL
3. Connect PIN 1 I2C0 SDA to PIN 3 SDA 
4. Connect PIN 38 GND to PIN 4 GND

On power up, you should see "Matrix Orbital" on the display

## Running the Code

What you will see on the screen when working correctly (the Line 2 numbers will be different):

Line 1: Temperature:

Line 2: 14.468C 46.243F

<img src=Project_running.jpg></img>

WEB https://www.matrixorbital.com

SUPPORT https://www.lcdforums.com/forums/viewforum.php?f=1
