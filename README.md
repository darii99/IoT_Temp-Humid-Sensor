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
| MCU Raspberry Pico Pi WH                              | A microcontrol board with a RP2040 chip, dual-core arm cortex-M0+ processor, clocks running up to 133 MHz, 264kB SRAM and 2,4GHz wireless LAN.Has 26 multifunction GPIO pins with 3 analogue inputs.         | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/a29e61f7-13b2-43e9-a9fc-bdfd4debf6dd) |                                          |                                                       |                                                      |
| Temperature and Humidity Sensor DHT11 )               | A digital temperature and humidity sensor with working voltage 3.5 - 5.5V. Measuring temperature range is 0°C - 50°C and measure humidity range is 20% - 90% (at 25°C). It has three pins: DOUT (Digital output), GND (Ground) and VCC (3.3 - 5.5V).                    | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/a8da6718-4b31-4d2a-9194-597bd6adec4e) |
| Solderless Breadboard 840 tie-points                  | A reusable breadbord used for making temporary electrical connections without requiring soldering. Has 840 contact points.| ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/71c7084e-f105-4083-a11d-133e4f550344) |
| 5 Jumper wires, Male-to-Male                          | Electrical wires with connector pins at each end (male), used to connect two points in a circuit.    |![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/f1e15408-91c2-446b-a80e-50240ce85694) |
| USB-cable connection type A to micro-USB              | USB-cable type A to micro-USB used to connect the MCU to the computer, making it possible to program it.   | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/740fd029-0f84-40cd-8125-90abec621afb)

All these parts were included in the Start Kit at <https://www.electrokit.com/lnu-starter> at a cost of 399 SEK.

## **Computer Setup**

### Choice of IDE ###
Thonny IDE

### Step-by-step Guide ###
When setting everything up, I started by installing *Node.js* and *Thonny IDE*.  Afterwards, the firmware needed to be updated, so I downloaded the micropython firmware (a uf2-file) at <https://micropython.org/download/RPI_PICO_W/> before connecting the Raspberry Pi Pico to the micro-USB. Next step was to connect the other end of the USB cable (type A) into the computer while holding the MCU's BOOTSEL-key down on the board. When the Raspberry Pi Pico appeared as an USB drive, the downloaded uf2-file was then dragged into its storage drive in the file system. As it got successfully imported, the board disconnected automatically from the computer (this is when the firmware has been successfully flashed). The USB cable was then unplugged and plugged back in order to confirm that the board is ready. The following step was to access the MicroPython REPL. This was done by launching Thonny and clicking on *Tools* -> *Options* -> *Interpreter* -> choosing "MicroPython (Raspberry Pi Pico)" from the list and ensuring that the correct port is selected (or by auto-detecting the port). After finishing these steps, the MicroPython REPL prompt were seen in the Shell area at the bottom of Thonny IDE. (These steps are how flashing is done in MicroPython.)
When getting started with the code, libraries were created by clicking on *File* -> *New* in Thonny. There *main.py* and *dht.py*, the libraries that later got to be used in this project, were created.

## **Putting everything together**

The connection of the electronics are as shown in the picture: 
- The Pico's port 40 (VBUS) is connected through a jumper wire to the breadboard's "power rail", and out of the power rail connect another jumper wire to the sensor DHT11's VCC pin.
- The Pico's port 39 (GND) is connected through a jumper wire to the breadboard's "ground rail", and out of the ground rail connect another jumper wire to the sensor's GND pin.
- Pico's port 32 (GP27) is connected directly to the sensor's signal pin through one single jumper wire.


![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/41c8ccfe-7137-4c0b-bbcc-30c507be153a)

The DHT11 operates at 3.3V to 5V, and the Pico's VBUS (port 40) provides 5V, which is suitable for powering the sensor. Optionally, a 5kΩ pull-up resistor can be added between the sensor's signal pin and VCC for stability (according to DHT11's datasheet). This setup is ideal for development. However, if for production, soldering sonnections to a PCB should be considered for durability.

  
## **Platform**

The chosen platform is Windows with Thonny IDE: Windows was selected due to personal familiarity and Thonny IDE because of its built-in support for MicroPython, which made the development for the Pico straightforward. The development was done with local installations on Windows and by using Thonny IDE, which allowed a direct interaction with the hardware. For scaling from local to production, one idea would be to start locally on Windows with Thonny IDE and later on transition to Linux systems for larger deployments.
In terms of functionality, Thonny IDE on Windows supports coding, debugging and also uploading code to the Raspberry Pi Pico. The local setup also allows for immediate hardware interaction between the computer and the Pico.

## **The code**


## **Transmitting the data/connectivity**


## **Presenting the data**


## **Finalizing the design**
