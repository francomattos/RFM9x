
#include <SPI.h>
#include <RH_RF95.h>

// Sets Pins
#define RFM95_CS 4
#define RFM95_RST 2
#define RFM95_INT 3

// Sets Frequency
#define RF95_FREQ 915.0

// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

#define LED 13

void setup()
{
  pinMode(LED, OUTPUT);
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  while (!Serial)
    ;
  Serial.begin(9600);
  delay(100);

  Serial.println("Arduino LoRa Test Begin");

  // Manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  // Checks initialization
  while (!rf95.init())
  {
    Serial.println("LoRa radio init failed");
    while (1)
      ;
  }
  Serial.println("LoRa radio init OK!");

  // Sets frequency and checks if it works, if works displays set frequency
  if (!rf95.setFrequency(RF95_FREQ))
  {
    Serial.println("setFrequency failed");
    while (1)
      ;
  }
  Serial.print("Set Freq to: ");
  Serial.println(RF95_FREQ);

  // Sets transmit power to 23dB
  rf95.setTxPower(23, false);
}

// Send "Hi There!" every 3 seconds
void loop()
{
  Serial.println("Sending Message: Hi There!");
  digitalWrite(LED, HIGH);
  uint8_t data[] = "Hi There!";
  rf95.send(data, sizeof(data));
  rf95.waitPacketSent();
  digitalWrite(LED, LOW);
  delay(3000);
}
