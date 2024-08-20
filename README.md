# IoT_Temp-Humid-Sensor 
An IoT Temperature and Humidity Sensor Project in the summer course '24 "Introduction to Applied IoT" at Linnaeus University.

Name and student credentials: *Darina Larsen, dl222sg*


## **Overview**
In this project I chose to make a temperature and humidity sensor using the MCU Raspberry Pico Pi WH and the temperature sensor DH11 by connecting them on a breadboard and then programming their behaviour with Micropython language on Thonny IDE. The idea of the project is to also be able to see the output on a website by connecting the MCU wirelessly to WiFi.

The estimation of the time required to complete this project is approximately three weeks (taking research, setup, coding etc. into consideration).


## **Objective**

The reason I chose this project is because I will spend the majority of the summer working while leaving my pet at home alone, and I would like to be able to see the alterations in temperature and humidity in the apartment. I already have an AC and a fan that I can turn on and off through an app, and by seeing the data provided through this project, I can have a better understanding for when I should turn them on or off remotely. In this way I can avoid letting my pet either freeze or be warm by guessing which alternative is better.


## **Material**

The materials that were used in this project are:

|                        Material                       |               Description                            |             Picture              |  
|-------------------------------------------------------|------------------------------------------------------|----------------------------------|
| MCU Raspberry Pico Pi WH                              | A microcontrol board with a RP2040 chip, dual-core arm cortex-M0+ processor, clocks running up to 133 MHz, 264kB SRAM and 2,4GHz wireless LAN.Has 26 multifunction GPIO pins with 3 analogue inputs.         | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/a29e61f7-13b2-43e9-a9fc-bdfd4debf6dd) |                                          |                                                       |                                                      |
| Temperature and Humidity Sensor DHT11 )               | A digital temperature and humidity sensor with working voltage 3.5 - 5.5V. Measuring temperature range is 0°C - 50°C and measure humidity range is 20% - 90% (at 25°C). It has three pins: DOUT (Digital output), GND (Ground) and VCC (3.3 - 5.5V).                    | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/a8da6718-4b31-4d2a-9194-597bd6adec4e) |
| Solderless Breadboard 840 tie-points                  | A reusable breadbord used for making temporary electrical connections without requiring soldering. Has 840 contact points.| ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/71c7084e-f105-4083-a11d-133e4f550344) |
| 5 Jumper wires, Male-to-Male                          | Electrical wires with connector pins at each end (male), used to connect two points in a circuit.    |![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/f1e15408-91c2-446b-a80e-50240ce85694) |
| USB-cable connection type A to micro-USB              | USB-cable type A to micro-USB used to connect the MCU to the computer, making it possible to program it.   | ![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/740fd029-0f84-40cd-8125-90abec621afb) |


All these parts were included in the Start Kit at <https://www.electrokit.com/lnu-starter> at a cost of 399 SEK.

## **Computer Setup**

### Choice of IDE ###
Thonny IDE

### Step-by-step Guide ###
When setting everything up, I started by installing *Node.js* and *Thonny IDE*.  Afterwards, the firmware needed to be updated, so I downloaded the micropython firmware (a uf2-file) at <https://micropython.org/download/RPI_PICO_W/> before connecting the Raspberry Pi Pico to the micro-USB. Next step was to connect the other end of the USB cable (type A) into the computer while holding the MCU's BOOTSEL-key down on the board. When the Raspberry Pi Pico appeared as an USB drive, the downloaded uf2-file was then dragged into its storage drive in the file system. As it got successfully imported, the board disconnected automatically from the computer (this is when the firmware has been successfully flashed). The USB cable was then unplugged and plugged back in order to confirm that the board is ready. The following step was to access the MicroPython REPL. This was done by launching Thonny and clicking on *Tools* -> *Options* -> *Interpreter* -> choosing "MicroPython (Raspberry Pi Pico)" from the list and ensuring that the correct port is selected (or by auto-detecting the port). After finishing these steps, the MicroPython REPL prompt was seen in the Shell area at the bottom of Thonny IDE. (These steps are how flashing is done in MicroPython.)

When getting started with the code, libraries were created by clicking on *File* -> *New* in Thonny. There *main.py* and *dht.py*, the libraries that later got to be used in this project, were created. For more details regarding the code, please read ***The Code*** section under. Besides the code, a simple website template was created by using HTML, which in turn would be put into the code. This makes the output data from the temperature and humidity sensor more straightforward. 

Next step was to activate the VPN function on my home router in order to access the data remotely. In my router's case, it was enough to log into it and activate a button called "VPN". This created a certificate which I in turn forwarded into my mobile's VPN app "Open VPN". This created a connection between my mobile phone and the router.

## **Putting everything together**

The connection of the electronics are as shown in the picture: 
- Pico's port 40 (VBUS) is connected through a jumper wire to the breadboard's "power rail", and out of the power rail connect another jumper wire to the sensor DHT11's VCC pin.
- Pico's port 38 (GND) is connected through a jumper wire to the breadboard's "ground rail", and out of the ground rail connect another jumper wire to the sensor's GND pin.
- Pico's port 32 (GP27) is connected directly to the sensor's signal pin through one single jumper wire.


![image](https://github.com/darii99/IoT_Temp-Humid-Sensor/assets/85901578/41c8ccfe-7137-4c0b-bbcc-30c507be153a)

The DHT11 operates at 3.3V to 5V, and the Pico's VBUS (port 40) provides 5V, which is suitable for powering the sensor. Optionally, a 5kΩ pull-up resistor can be added between the sensor's signal pin and VCC for stability (according to DHT11's datasheet). This setup is ideal for development. However, if for production, soldering sonnections to a PCB should be considered for durability.

  
## **Platform**

The chosen platform is Windows with Thonny IDE: Windows was selected due to personal familiarity and Thonny IDE because of its built-in support for MicroPython, which made the development for the Pico straightforward. The development was done with local installations on Windows and by using Thonny IDE, which allowed a direct interaction with the hardware. For scaling from local to production, one idea would be to start locally on Windows with Thonny IDE and later on transition to Linux systems for larger deployments (since Linux is preferred for larger deployments due to its stability, extensive development tools and strong remote management capabilities).
In terms of functionality, Thonny IDE on Windows supports coding, debugging and also uploading code to the Raspberry Pi Pico. The local setup also allows for immediate hardware interaction between the computer and the Pico.



## **The code**

Core functions in the code:

### **main.py**  
This library sets up the IoT system on the Raspberry Pi Pico to measure temperature and humidity using the DHT11 sensor, and serves the data through a local web server. Here are some code snippets:


Wi-Fi Connection (connects the device to a Wi-Fi network)
```
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        sleep(1)
    return wlan.ifconfig()[0]
```

Sensor Data Reading (Reads temperature and humidity using the DHT11 sensor)
```
def getTempAndHumid():
    pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    return sensor.temperature, sensor.humidity
```

HTML Page Generation (dynamically generates a webpage displaying temperature and humidity)
```
def webpage(temperature, humidity):
    html = """<html>Temperature: TEMP_PLACEHOLDER, Humidity: HUMID_PLACEHOLDER</html>"""
    return html.replace("TEMP_PLACEHOLDER", str(temperature)).replace("HUMID_PLACEHOLDER", str(humidity))
```

Web Server (handles client requests, providing sensor data)
```
def serve(connection):
    while True:
        client = connection.accept()[0]
        temp, humid = getTempAndHumid()
        client.send(webpage(temp, humid))
        client.close()
```
Moreover, the library includes a website functionality which generates the HTML page and uses JavaScript to change colors based on the values. The HTML template dynamically adjusts the text color to red or green depending on the temperature (≥25°C) or humidity (≥60%).

Here is a code snippet of the HTML body:
```
<!DOCTYPE html>
                    <html>
                    <body id="block" onload="setTempColor(), setHumidColor()">
                        <h1 id="heading">Fluffis Comfy Keeper</h1>
                        <div style="clear: both">
                            <h2 style="float: left">Temperature is: </h2>
                            <h2 id="temp" style="float: left">TEMP_PLACEHOLDER</h2>
                        </div>
                        <div style="clear: both">
                            <h2 style="float: left">Humidity is: </h2>
                            <h2 id="humid" style="float: left">HUMID_PLACEHOLDER</h2>
                        </div>
                    </body>
```

The DHT11 sensor is initialised on GPIO pin 27, then the temperature and humidity is read every two seconds. The exceptions "InvalidPulseCount" and "InvalidChecksum" are caught and handled.        

### **dht.py**  
The dht.py library contains the DHT11 driver code. It handles the sensor initialisation, data reading and checksum verification. It reads temperature and humidity from the DHT11 using pulse counting and data conversion.


The core functionalities here are:
1. Initialisation (sets up the sensor)
2. Measurement (gathers data if enough time has passed)
3. Pulse capture (reads pulse transitions from the sensor)
4. Data conversion (converts pulses into temperature and humidity bytes)
5. Checksum validation (ensures valid data using a checksum)


- Initialisation

The DHT111 sensor is initialised by setting up the pin, "_last_measure" stores the last measurement timestamp, while "_temperature" and "_humidity" are initialised with invalid values (-1).

Code snippet of the initialisation:
```
class DHT11:
    def __init__(self, pin):
        self._pin = pin
        self._last_measure = utime.ticks_us()
        self._temperature = -1
        self._humidity = -1
```


- Send Initialisation Signal

This part prepares the sensor for data transmission. After the pin is set as output, a high signal is sent to the sensor for 50ms. According to the DHT11 datasheet, 50ms of high signal is required in order to start the signal which instructs the sensor to change from low-power mode to tunning mode. This enables it to receive commands and transmit the data. After the high signal, the pin is then pulled low for 18ms, which initialises the data transmission process from the sensor to the Pico. According to the datasheet, this low signal must be at least 18ms.

```
def _send_init_signal(self):
    self._pin.init(Pin.OUT, Pin.PULL_DOWN)            # Sets pin as output with pull-down resistor enabled
    self._pin.value(1)                                
    utime.sleep_ms(50)                                # Sends a high signal for 50ms to initialise the sensor, required according to datasheet
    self._pin.value(0)
    utime.sleep_ms(18)                                # Pulls the pin low for 18ms to signal the start of data transmission, required according to datasheet
```


- Measuring the Temperature and Humidity
  
Here the DHT11 sensor is measuring the temperature and humidity and updating their value every 2s. 

```
def measure(self):
    if utime.ticks_diff(utime.ticks_us(), self._last_measure) < MIN_INTERVAL_US:
        return
    self._send_init_signal()
    pulses = self._capture_pulses()
    buffer = self._convert_pulses_to_buffer(pulses)
    self._verify_checksum(buffer)
```  


- Capture Pulses

The purpose of this function is to capture the timing of the pulses sent by the sensor. It records the time between the signal transitions (low to high and hight to low). It returns the recorded pulse timings, and if the number of pulses is incorrect, it raises an error.
```
def _capture_pulses(self):
    pin = self._pin
    transitions = bytearray(EXPECTED_PULSES)
    # Captures transitions and timestamps
    return transitions[4:]
```


- Data Conversion 

This is a function that converts the captured pulse timings into a data buffer (temperature and humidity bytes). The functionalities here are that the pulses are converted into a binary representation and that it splits the binary data into five bytes (for temperature, humidity and checksum).

```
def _convert_pulses_to_buffer(self, pulses):
    binary = sum(1 << (len(pulses)-1-idx) for idx, p in enumerate(pulses[::2]) if p > HIGH_LEVEL)
    return array.array("B", [(binary >> (i * 8)) & 0xFF for i in range(4, -1, -1)])
```  


- Checksum Validation

The purpose of this function is to ensure the data integrity by verifying the checksum. The functionalities are that the first four bytes of the buffer are being computed, then the computed checksum is being compared with the fifth byte. If they do not match, it raises an error.

```
def _verify_checksum(self, buffer):
    if sum(buffer[0:4]) & 0xFF != buffer[4]:
        raise InvalidChecksum()
```



## **Transmitting the data/connectivity**

Data from the DHT11 sensor is transmitted using an HTTP server on the Raspberry Pi Pico. The server listens for incoming HTTP requests, gathers sensor data, formats it into an HTML page, and sends it back to the client (a web browser).

Steps to Transmit the Data:
Wi-Fi Connection:
The Raspberry Pi Pico connects to the local Wi-Fi network via a router and is secured with OpenVPN through a phone, ensuring remote access with a VPN certificate.

Handling Client Requests:
A socket server listens on port 80. When the client (a web browser) sends an HTTP GET request, the Pico retrieves temperature and humidity data from the DHT11 sensor.

Formatting and Sending the Data:
The sensor data is formatted into an HTML page, including temperature and humidity readings. The background color changes based on the values (green or red). This HTML response is sent back to the client via HTTP.

Protocols Used:

Wireless Protocol: Wi-Fi for local network communication. OpenVPN is employed for secure remote access, allowing access to the Pico from outside the local network. 
Transport Protocol: HTTP is used for data transmission between the Pico and the client (web browser).  
Transmission Frequency: The data is transmitted on-demand, i.e. only when the client requests it. Each request triggers the Pico to send the latest sensor readings.


## **Presenting the data**

- Dashboard Construction

The project does not include a traditional dashboard or database for long-term data storage. Instead, it focuses on real-time data presentation.

Real-Time HTML Page:
The Pico serves a live HTML page showing the current temperature and humidity from the DHT11 sensor. JavaScript dynamically updates the page, changing background colors based on sensor readings.


- Data Preservation and Storage  
Database Storage:
There is no database or long-term storage. Data is available only during the web page session and is updated with each request.


- Data Saving Frequency:  
No data is saved to a database; it is only displayed in real-time.




Here are some screenshots showing example data:

![image](https://github.com/user-attachments/assets/a3fa7841-3764-4d3f-96f4-721c6ef24df7)
![image](https://github.com/user-attachments/assets/931104dd-cd43-40b9-bc3b-15d1f86b0b2f)
![image](https://github.com/user-attachments/assets/9d2a7a82-93c3-4239-bfd8-cab1a4f52e49)



## **Finalizing the design**

- Picture of the final project


![thumbnail_20240819_181829](https://github.com/user-attachments/assets/92bed838-2eed-449c-9edc-e1e035030dca)


- Screen recordings demonstrating access to the HTML page via Wi-Fi and OpenVPN.

https://github.com/user-attachments/assets/7ccdfa5c-cbc2-41a3-b265-a1c2b3188837

https://github.com/user-attachments/assets/81bbeb51-18e5-4859-8695-73398094e4e8


- Final Thoughts

The project works well for real-time monitoring, giving me the temperature and humidity data I needed. The core functions are all in place and working fine.

If I had more time, I’d focus on adding a dashboard and database to store the historical data. I’d also spend more time refining the website design to make it look and feel more "polished" and user-friendly.

Overall, it’s a solid start, but there’s room for improvement in data storage and design.

