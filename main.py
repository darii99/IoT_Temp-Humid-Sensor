# main.py 
from machine import Pin, reset
import utime as time
from dht import DHT11, InvalidChecksum, InvalidPulseCount
import network
import socket
from time import sleep


# Wi-Fi credentials
ssid = '---'
password = '---'

def flashLed():
    print("Led is live!")
    led = Pin(15, Pin.OUT)
    led.value(1)

def getTempAndHumid():
    pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    return sensor.temperature, sensor.humidity

# HTML code
def webpage(temperature, humidity):
    html = """
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
                    <style>
                        #block {
                            margin: 10px;
                            padding:30px;
                            background-color: #f1f1f1;
                            /* target color: #FFD200;*/
                        }
                        #heading {
                            background-color: #e96ab8;
                        }
                    </style>
                    <script>
                        function setTempColor() {
                          var value = document.getElementById("temp").innerText;
                          console.log(parseFloat(value))
                          if (parseFloat(value) >= 25){
                            document.getElementById("temp").style.backgroundColor = 'red';
                          }else{
                            document.getElementById("temp").style.backgroundColor = 'green';
                          }
                        }
                        
                        function setHumidColor() {
                            var value = document.getElementById("humid").innerText;
                            console.log(parseFloat(value))
                            if (parseFloat(value) >= 60){
                              document.getElementById("humid").style.backgroundColor = 'red';
                            }else{
                              document.getElementById("humid").style.backgroundColor = 'green';
                            }
                          }



                        </script>
                </html>
            """.replace("TEMP_PLACEHOLDER", str(temperature)).replace("HUMID_PLACEHOLDER", str(humidity))
    return html
    
    
# Web server    
def serve(connection):
    #Start a web server
    try:
        html = None
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            print(request)
            try:
                temp, humid = getTempAndHumid()
                html = webpage(temp, humid)
            except InvalidPulseCount:
                html = webpage(0,0)
            except InvalidChecksum:
                html = webpage(0,0)
            client.send(html)
            client.close()
    except KeyboardInterrupt:
        if client:
            client.close()
        if connection:
            connection.close()
        machine.reset()


# Connect to Wi-Fi
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    return wlan.ifconfig()[0]


def open_socket(ip):
    # Open a socket
    BIND_SUCCESS = False
    address = (ip, 80) # Tupel object - kort och gott en lista
    connection = socket.socket()
    while not BIND_SUCCESS:
        try:
            connection.bind(address)
            connection.listen(1)
            print(connection)
            BIND_SUCCESS = True
        except OSError as err:
            if err.errno == 98:
                print(f"Address{address} in use, trying again in 10 seconds")
                sleep(10)
            else:
                print(f"Unknown Error: {err.errno}\n{err}")
            
    return connection
    
    
# What is actually running when the raspberry turns on
flashLed()
ip = connect()
connection = open_socket(ip)
serve(connection)
reset()


