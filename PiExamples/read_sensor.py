import bme280
import time


while True:
    temperature, pressure, humidity = bme280.readBME280All()
    print temperature, pressure, humidity
    time.sleep(10)
