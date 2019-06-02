const int sensorPin = A0;
const int ledPin = 13;

int sensorValue = 0;
int sensorMin = 1023;
int sensorMax = 0;

void setup() {
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, HIGH);

    while(millis()<5000) {
        sensorValue = analogRead(sensorPin);
        if (sensorValue > sensorMax) {
            sensorMax = sensorValue;
        }
        if (sensorValue < sensorMin) {
            sensorMin = sensorValue;
        }
    }
    digitalWrite(ledPin, LOW);
}

void loop() {
    sensorValue = analogRead(sensorPin);
    sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);
    sensorValue = constrain(sensorValue, 0, 255);
    Serial.println(sensorValue);
    analogWrite(ledPin, 255-sensorValue);
}