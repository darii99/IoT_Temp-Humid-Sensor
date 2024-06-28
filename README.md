# IoT_Temp-Humid-Sensor 
An IoT Temperature and Humidity Sensor Project in the summer course '24 "Introduction to Applied IoT" at Linnaeus University.

Name and student credentials: *Darina Larsen, dl222sg*


## **Overview**
In this project I chose to make a temperature and humidity sensor using the MCU Raspberry Pico Pi WH and the temperature sensor DH11 by connecting them on a breadboard and then programming their behaviour with Micropython language on Thonny. The idea of the project is to also be able to see the output on a website by connecting the MCU wirelessly to WiFi.

The estimation of the time required to complete this project is approximately a week (taking research, setup, coding etc. into consideration)


## **Objective**

The reason I chose this project is because I will spend the majority of the summer working while leaving my pet at home alone, and I would like to be able to see the alterations in temperature and humidity in the apartment. I already have an AC and a fan that I can turn on and off through an app, and by seeing the data provided through this project, I can have a better understanding for when I should turn them on or off remotely. In this way I can avoid letting my pet either freeze or be warm by guessing what alternative is better.


## **Material**

The materials that were used in this project are:

|                        Material                       |               Description                            |             Picture              |  
|-------------------------------------------------------|------------------------------------------------------|----------------------------------|
| MCU Raspberry Pico Pi WH (41019114)                   | A microcontrol board with a RP2040 chip, dual-core arm cortex-M0+ processor, clocks running up to 133 MHz, 264kB SRAM and 2,4GHz wireless LAN.Has 26 multifunction GPIO pins with 3 analogue inputs.         | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/a29e61f7-13b2-43e9-a9fc-bdfd4debf6dd) |                                          |                                                       |                                                      |
| Temperature and Humidity Sensor DHT11 (41015728)      | A digital temperature and humidity sensor with working voltage 3.5 - 5.5V. Measuring temperature range is 0°C - 50°C and measure humidity range is 20% - 90% (at 25°C). It has three pins: DOUT (Digital output), GND (Ground) and VCC (3.3 - 5.5V).                    | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/a8da6718-4b31-4d2a-9194-597bd6adec4e) |
| Solderless Breadboard 840 tie-points (10160840)       | A reusable breadbord used for making temporary electrical connections without requiring soldering. Has 840 contact points.| ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/71c7084e-f105-4083-a11d-133e4f550344) |
| 5 Jumper wires, Male-to-Male (41012684)               | Electrical wires with connector pins at each end (male), used to connect two points in a circuit.    |![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/f1e15408-91c2-446b-a80e-50240ce85694) |
| USB-cable connection type A to micro-USB (41003290)   | USB-cable type A to micro-USB used to connect the MCU to the computer, making it possible to program it.   | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/740fd029-0f84-40cd-8125-90abec621afb)

All these parts were included in the Start Kit at <https://www.electrokit.com/lnu-starter> at a cost of 399 SEK.

## **Computer Setup**

### Choice of IDE ###
Thonny IDE

### Step-by-step Guide ###
When setting everything up, I started by installing *Node.js* and *Thonny IDE*.  Afterwards, the firmware needed to be updated, so I downloaded the micropython firmware (a uf2-file) at <https://micropython.org/download/RPI_PICO_W/> before connecting the Raspberry Pi Pico to the micro-USB. Next step was to connect the other end of the USB cable (type A) into the computer while holding the MCU's BOOTSEL-key down on the board. When the Raspberry Pi Pico appeared as an USB drive, the downloaded uf2-file was then dragged into its storage drive in the file system. As it got successfully imported, the board disconnected automatically from the computer (this is when the firmware has been successfully flashed). The USB cable was then unplugged and plugged back in order to confirm that the board is ready. The following step was to access the MicroPython REPL. This was done by launching Thonny and clicking on *Tools* -> *Options* -> *Interpreter* -> choosing "MicroPython (Raspberry Pi Pico)" from the list and ensuring that the correct port is selected (or by auto-detecting the port). After finishing these steps, the MicroPython REPL prompt were seen in the Shell area at the bottom of Thonny IDE. (These steps are how flashing is done in MicroPython.)
When getting started with the code, libraries were created by clicking on *File* -> *New* in Thonny. There *main.py* and *dht.py*, the libraries that later got to be used in this project, were created.

## **Putting everything together**


## **Platform**


## **The code**


## **Transmitting the data/connectivity**


## **Presenting the data**


## **Finalizing the design**
