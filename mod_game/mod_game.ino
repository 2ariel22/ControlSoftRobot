#include <Servo.h>
#include <BluetoothSerial.h>


const int servoPins[] = {9, 10, 6, 5, 3}; // Pines PWM del Arduino Uno
Servo servos[5];
BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("brazo_BT");

  for (int i = 0; i < 5; i++) {
    servos[i].attach(servoPins[i]);
  }
}

void loop() {
  if (SerialBT.available() >= 17) {
    int x = SerialBT.readStringUntil(',').toInt();
    int y = SerialBT.readStringUntil(',').toInt();
    int z = SerialBT.readStringUntil(',').toInt();
    int r = SerialBT.readStringUntil(',').toInt();
    int s5 = SerialBT.readStringUntil('\n').toInt();

    servos[0].write(x);
    servos[1].write(y);
    servos[2].write(z);
    servos[3].write(r);
    servos[4].write(s5);
  }
}

