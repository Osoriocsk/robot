🚗 Smart 4WD ESP32 Car

A multifunctional autonomous 4-wheel drive robotic car powered by ESP32. This project integrates motor control, servo control, line tracking, light following, battery monitoring, buzzer alerts, and animated LED matrix emotions.

📋 Features
🚙 Mobility
Independent control of 4 DC motors
Forward, backward, left, and right movement
Speed control using PCA9685 PWM driver
👀 Emotion Display

8x8 LED matrix animations including:

Rotating eyes
Blinking eyes
Smiling face
Crying face
Wheel animations
Static emotional expressions
🌞 Light Following Mode

The vehicle can detect changes in ambient light and automatically:

Move toward stronger light sources
Change movement direction based on light intensity
Display corresponding emotions
🛣️ Line Tracking Mode

Using infrared tracking sensors, the robot can:

Follow predefined paths
Correct direction automatically
Stop when the track is lost
🎯 Servo Control

Two servos can be controlled independently:

Servo 1: 0°–180°
Servo 2: 80°–180°
🔊 Buzzer System

Supports:

Alarm mode
Variable frequency tones
Alert sequences
🔋 Battery Monitoring

Real-time battery voltage monitoring using ESP32 ADC calibration.

🛠 Hardware Requirements
ESP32 Development Board
Freenove 4WD Smart Car Chassis
PCA9685 PWM Driver
PCF8574 I/O Expander
HT16K33 LED Matrix Module
2 Servo Motors
4 DC Motors
Infrared Tracking Module
Photoresistor (LDR)
Active Buzzer
Rechargeable Battery Pack
📚 Libraries Used
Arduino
Wire
PCA9685
PCF8574
esp_camera
esp_adc_cal

Additional Freenove libraries:

Freenove_4WD_Car_For_ESP32
Freenove_4WD_Car_Emotion
Freenove_4WD_Car_WS2812
Freenove_4WD_Car_WiFi
Freenove_VK16K33_Lib_For_ESP32
📂 Project Structure
├── 06.3_Multi_Functional_Car.ino
├── Freenove_4WD_Car_For_ESP32.cpp
├── Freenove_4WD_Car_For_ESP32.h
├── Freenove_4WD_Car_Emotion.cpp
├── Freenove_4WD_Car_Emotion.h
└── Additional Freenove Libraries
⚙️ Main Functional Modules
Motor Control
Motor_Move(m1, m2, m3, m4);

Controls all four motors individually.

Servo Control
Servo_1_Angle(angle);
Servo_2_Angle(angle);

Moves servos to the desired angle.

Emotion Display
Emotion_SetMode(mode);

Available modes:

Mode	Emotion
0	Clear Display
1	Rotating Eyes
2	Crying
3	Smiling
4	Right Wheel
5	Left Wheel
6	Blinking
Light Following
Light_Car(1);

Enables autonomous light tracking.

Line Following
Track_Car(1);

Enables autonomous line tracking.

Battery Monitoring
float voltage = Get_Battery_Voltage();

Reads current battery voltage.

🚀 Getting Started
1. Install Arduino IDE

Download from:

Arduino IDE

2. Install ESP32 Board Package

Add the ESP32 board support to Arduino IDE.

3. Install Required Libraries

Install all Freenove dependencies and external libraries listed above.

4. Upload Firmware

Open:

06.3_Multi_Functional_Car.ino

Select your ESP32 board and upload the firmware.

🔧 Operating Modes
Mode	Description
Manual	Controlled by commands
Light Following	Tracks light source
Line Tracking	Follows a line
Emotion Display	Shows animated expressions
🎓 Educational Objectives

This project demonstrates:

Embedded Systems Programming
ESP32 Development
Robotics Fundamentals
PWM Motor Control
Sensor Integration
I2C Communication
Autonomous Navigation
Human-Robot Interaction using LED Emotions
📄 License

This project is intended for educational and research purposes.

👨‍💻 Author

Kevin Osorio

Systems Engineering Student

ESP32 Robotics and Embedded Systems Project

