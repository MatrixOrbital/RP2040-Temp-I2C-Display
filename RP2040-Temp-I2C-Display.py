# A simple Read and Display the temperature from the Pi Pico R2040
# to an I2C Matrix Orbital display
#
# By Matrix Orbital
#
# WEB
# https:#www.matrixorbital.com
# SUPPORT
# https:#www.lcdforums.com/forums/viewforum.php?f=1
#
# -------------------------------------------------------------
# Connect a Pi Pico RP2040 to a Matrix Orbital I2C Display:
# RP2020 --> Display
# 1. Connect PIN 40 VBUS to PIN 1 VIN
# 2. Connect PIN 2 I2C0 SCL to PIN 2 SCL
# 3. Connect PIN 1 I2C0 SDA to PIN 3 SDA 
# 4. Connect PIN 38 GND to PIN 4 GND
#
# On power up, you should see "Matrix Orbital" on the display
#--------------------------------------------------------------
#
# RP2040 configuration
from machine import ADC # ADC class provides an interface to analog-to-digital convertors
from machine import I2C # I2C class provides a two-wire serial protocol
import time #functions for handling time-related tasks

sdaPIN=machine.Pin(0) # Set Pin 0 to SDA
sclPIN=machine.Pin(1) # Set pin 1 to SCL
i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
i2c_address = 0

# Scan the I2C bus to look for the display
print('Scanning i2c bus')
devices = i2c.scan()
if len(devices) == 0:
 print("No i2c device found !") # Display not found, check your connection and I2C pull-ups
else:
 print('i2c devices found:',len(devices))
 for device in devices:
     print("Decimal address: ",device," | Hexa address: ",hex(device))
     if device == 0x28: # Default address is 0x28 for Matrix Orbital I2C displays
         print("Matrix Orbital I2C Display detected")
         i2c_address = device
         i2c.writeto(i2c_address,bytearray(b'\xfe\x58')) # Clear Screen

adc = machine.ADC(4)

# Main loop, read, convert, display temperature
while True:
    ADC_voltage = adc.read_u16() * (3.3 / (65535))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    temp_fahrenheit=32+(1.8*temperature_celcius)
    message = "Temperature:\n{:.3f}C {:.3f}F".format(temperature_celcius,temp_fahrenheit)
    print(message) # Print data on the display
    if i2c_address != 0:
        i2c.writeto(i2c_address,bytearray(b'\xfe\x48')) # Return the cursor home
        i2c.writeto(i2c_address,message)
    time.sleep_ms(500) # Delays 500ms