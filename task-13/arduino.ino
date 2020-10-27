long duration;
int distance;

int sensorPin = 7;
int motorPin = 4;
int ledPin = 3;
void setup()
{
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  pinMode(motorPin,OUTPUT);
}

void loop()
{
  pinMode(sensorPin, OUTPUT);
  digitalWrite(sensorPin, LOW);
  delay(2);
  digitalWrite(sensorPin, HIGH);
  delay(5);
  digitalWrite(sensorPin, LOW);
  pinMode(sensorPin, INPUT);
  duration = pulseIn(sensorPin, HIGH);
  distance = duration/ 29 / 2;
  
  if (distance > 100){
    digitalWrite(ledPin, LOW);
  	digitalWrite(motorPin, HIGH);
  }
  else {
  	digitalWrite(motorPin, LOW);
  	digitalWrite(ledPin, HIGH);
  }
  delay(100); // Wait for 1000 millisecond(s)
}