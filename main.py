# main.py -- put your code here!

from machine import Pin
import utime as time
from dht import DHT11, InvalidChecksum

while True:
    time.sleep(5)
    pin = machine.Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))