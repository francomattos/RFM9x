import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import RFM9x
import adafruit_rfm9x

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
CS = DigitalInOut(board.D18)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
rfm9x.enable_crc = True
# It is important to set CRC to true, turned off by default
prev_packet = None

while True:
    packet = None

    # Check for packet RX
    packet = rfm9x.receive()
    if packet is None:
        time.sleep(0.1)
    else:
        # Display the packet text and RSSI
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        print("Received: {}".format(packet_text))
        time.sleep(1)
