#include <Thread.h>

#define pot A0
#define pot2 A1

const int solLed = 6;
const int sagLed = 7;

bool solSinyal, sagSinyal, far, geri, dortlu;

char message;

Thread threadDortlu= Thread();
Thread threadSolSinyal = Thread();
Thread threadSagSinyal = Thread();
Thread threadSendData = Thread();


float data[10];
float hiz, direksiyon, button;


void send_data(){
  
  hiz = analogRead(pot);
  direksiyon = analogRead(pot2);

  // Serial.println(hiz);
  // Serial.println(direksiyon);

  
  data[0] = map(hiz, 0, 1023, 0, 120);
  data[1] = map(direksiyon, 0, 1023, -100, 100);
  data[2] = 0;
  data[3] = map(hiz, 0, 1023, 0, 100);
  data[4] = 0;
  // Serial.println(data[2]);

  send(&data[0],&data[1],&data[2],&data[3],&data[4]);
}

void send(float* data1, float* data2, float* data3, float* data4, float* data5){

  byte* byteData1 = (byte*)(data1);
  byte* byteData2 = (byte*)(data2);
  byte* byteData3 = (byte*)(data3);
  byte* byteData4 = (byte*)(data4);
  byte* byteData5 = (byte*)(data5);
  byte buf[20] = {
    byteData1[0], byteData1[1], byteData1[2], byteData1[3],
    byteData2[0], byteData2[1], byteData2[2], byteData2[3],
    byteData3[0], byteData3[1], byteData3[2], byteData3[3],
    byteData4[0], byteData4[1], byteData4[2], byteData4[3],
    byteData5[0], byteData5[1], byteData5[2], byteData5[3]
    };
  Serial.write(buf, 20);
}

void sol_sinyal(){
  static bool solLedStatus = false;
  solLedStatus = !solLedStatus;

  digitalWrite(solLed, solLedStatus); 
}

void sag_sinyal(){
  static bool sagLedStatus = false;
  sagLedStatus = !sagLedStatus;

  digitalWrite(sagLed, sagLedStatus); 
}

void dortlu_sinyal(){
  static bool ledStatus = false;
  ledStatus = !ledStatus;
  
  digitalWrite(sagLed, ledStatus); 
  digitalWrite(solLed, ledStatus); 
}

void setup() {
  Serial.begin(9600);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  
  pinMode(solLed, OUTPUT);
  pinMode(sagLed, OUTPUT);

  digitalWrite(solLed,LOW);
  digitalWrite(sagLed,LOW);
  
  threadDortlu.onRun(dortlu_sinyal);
  threadDortlu.setInterval(700);

  threadSolSinyal.onRun(sol_sinyal);
  threadSolSinyal.setInterval(700);

  threadSagSinyal.onRun(sag_sinyal);
  threadSagSinyal.setInterval(700);

  threadSendData.onRun(send_data);
  threadSendData.setInterval(100);

}

void loop() {
  message=Serial.read();  
  
  if (message == '1'){
    sagSinyal = false;
    dortlu = false;
    digitalWrite(sagLed,LOW);
    digitalWrite(solLed,LOW);
    
    solSinyal = !solSinyal;
  }
  else if ( message == '2'){
    solSinyal = false;
    dortlu = false;
    digitalWrite(sagLed,LOW);
    digitalWrite(solLed,LOW);
    
    sagSinyal = !sagSinyal;
  }
  else if ( message == '3'){
    sagSinyal = false;
    solSinyal = false;
    digitalWrite(sagLed,LOW);
    digitalWrite(solLed,LOW);
    
    dortlu= !dortlu;
  }
  
  if(threadSolSinyal.shouldRun() && solSinyal)
    threadSolSinyal.run();

  if(threadSagSinyal.shouldRun() && sagSinyal)
    threadSagSinyal.run();
    
  if(threadDortlu.shouldRun() && dortlu)
    threadDortlu.run();    
    
  if(threadSendData.shouldRun())
    threadSendData.run();    
}
