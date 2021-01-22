
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure RFM9x LoRa Radio
CS = DigitalInOut(board.D18)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

while True:
    # Attempt to set up the RFM9x Module
    try:
        rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
        print("success")
    except RuntimeError as error:
        # Thrown on version mismatch
        print('RFM9x Error: ', error)

    time.sleep(0.9)
