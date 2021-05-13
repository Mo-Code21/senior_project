%% 
% 5/10/21
% Mohammed
%
% This is a script that control a motor and a sensor with arduino 
% connection. This is a calibration script

%% Arduino Setup

clear

Board = 'Mega2560';
Port = 'COM3';
Sensor_Pins = {'D3', 'D2'};
Motor_Pins = {'D8', 'D9'};
Gain = 128;

%% Initiate Connections
all_libs = listArduinoLibraries;

HX_711 = 'advancedHX711/advanced_HX711';
libs = { 'Serial', 'Servo'};

Ard = arduino(Port, Board, 'Libraries', libs);

Sensor = device(Ard, 'SerialPort', 2);
Sensor.BaudRate = 115200;
Sensor.TxPin = 'D2';
Sensor.RxPin = 'D3';
% Sensor = addon(Ard, 'advancedHX711/advanced_HX711', 'Pins', Sensor_Pins);
x=1;












% read_HX711(Sensor)
% while x==1
%     read_HX711(Sensor)
%     pause(0.5)
% end


