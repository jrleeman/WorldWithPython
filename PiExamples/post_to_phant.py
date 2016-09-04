import bme280
import time
from phant import Phant

p = Phant(publicKey='WGglMj2LaoCYmGynvnlQ',
          fields=['temperature', 'pressure', 'humidity'],
          privateKey='XR6X1MA9ZDurW0j8b8aR')

while True:
    temperature, pressure, humidity = bme280.readBME280All()
    p.log(temperature, pressure, humidity)
    print temperature, pressure, humidity
    time.sleep(10)
