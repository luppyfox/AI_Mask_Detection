// Motor A

int dir1PinA = 2;

int dir2PinA = 3;

int speedPinA = 11; //   เพื่อให้ PWM สามารถควบคุมความเร็วมอเตอร์
int pwm = 127;

void setup()
{
  Serial.begin(9600);

  //กำหนด ขา เพื่อใช้ในการควบคุมการทำงานของ  Motor ผ่านทาง L298N

  pinMode(dir1PinA, OUTPUT);

  pinMode(dir2PinA, OUTPUT);

  pinMode(speedPinA, OUTPUT);

}

void loop()
{

  // Motor A

  analogWrite(speedPinA, pwm); //ตั้งค่าความเร็ว PWM ผ่านตัวแปร ค่าต่ำลง มอเตอร์จะหมุนช้าลง

  SdigitalWrite(dir1PinA, LOW);

  digitalWrite(dir2PinA, HIGH);
  delay(500);
  analogWrite(speedPinA, 0);
  digitalWrite(dir1PinA, 0);
  digitalWrite(dir2PinA, 0);
  delay(5000);
  analogWrite(speedPinA, pwm
             );
  digitalWrite(dir1PinA, 1);
  digitalWrite(dir2PinA, 0);
  delay(500);
  analogWrite(speedPinA, 0);
  digitalWrite(dir1PinA, 0);
  digitalWrite(dir2PinA, 0);
  delay(5000);
}
