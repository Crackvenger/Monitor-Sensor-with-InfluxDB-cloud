import time
import board
import adafruit_ahtx0
import adafruit_bh1750

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)
light = adafruit_bh1750.BH1750(i2c)

#for i in range(4):
   # print("\nTemperature: %0.1f C" % sensor.temperature)
   # print("Humidity: %0.1f %%" % sensor.relative_humidity)
   # print(f"light: {light.lux:.2f}")
    #time.sleep(2)