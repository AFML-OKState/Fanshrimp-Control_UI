int En = 3;

volatile long Ct = 0;
int dt = 100;
float est = 0;
float avg = 0;

void setup() {
  Serial.begin(115200);

  pinMode(En, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(En), Count, CHANGE);
}

void loop() {

  for(int i = 0; i < 5; i++){
    avg += measure();
  }
  avg = avg/5;
  Serial.println(avg);
  avg = 0;

}

float measure(){
  Ct = 0;
  interrupts();
  delay(dt);
  noInterrupts();
  est = (float(1000/3)*float(Ct))/float(dt);
  return est;
}

void Count(){
  Ct++;
}
