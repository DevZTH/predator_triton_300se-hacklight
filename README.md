# predator_triton_300se-haclight
python script what uses ec_sys module to control backlight and fan also perfomance profile for predator triton 300se pt314-51s
use at own risc !!!

ec
Registers description

0x13, 0x14 L H CPU FAN RPM

0x15, 0x16 L H GPU FAN RPM

0x2d gpu power status 0- gpu on 1-gpu off


0x21 GPU fan mode register auto: 0x50 turbo 0x60 manual 0x70 \\values from dump

0x22 CPU fan mode register  auto 0x54 turbo 0x58  manual 0x5c (bit 3,4)

0x21 perfomance profile: 00 quiet 01 normal 04 hi perf. 05 turbo

0x37 values 0x00-0x64 CPU FAN control

0x3A values 0x00-0x64 GPU FAN control

0x5b TURBO LED 0 -off 1 -on

0xa7,0xb0, 0xb1 -cpu and system temperatures

0x32 GPU temp

