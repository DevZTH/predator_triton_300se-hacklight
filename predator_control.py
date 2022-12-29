#!/usr/bin/python
import os
from time import sleep

EC_IO="/sys/kernel/debug/ec/ec0/io" 
#EC_IO="/tmp/test"

os.system("modprobe -r ec_sys")
os.system("modprobe ec_sys write_support=1") 

GPUFAN_CR = 0x21
GPUFAN_PWMR = 0x3a

CPUFAN_CR = 0x22
CPUFAN_PWMR = 0x37

PROFILE_REG = 0x2c

COLOR_REG_OFFSET = 0x3c
KEY_RIGHTNESS = 0x19
KEY_ACTIVATE = 0x1F

#0x13 0x16 -fan speed

def filter_char(char: int):
    if char<0 or char>255:
        raise Exception("it's not a single byte")
    return hex(char).encode()

def ec_read(offset):
    ec = os.open(EC_IO, os.O_RDONLY)
    os.lseek(ec, offset,0)
    byte=os.read(ec, 1)
    print(byte)
    os.close(ec)
    return ord(byte)

def ec_write(offset, value):
    value=clamp(value,255)
    value=value.to_bytes(1,byteorder="big")
    ec = os.open(EC_IO, os.O_RDWR )
    os.lseek(ec, offset,0)
    print(value)
    os.write(ec, value)
    os.close(ec)

def clamp(value, max):
    if value<0:
        value=0
    if value>max:
        value=max
    return value

#start led
def start():
    if ec_read(3) == 1:
        ec_write(3,0x11)

def stop():
    ec_write(3, 0x01)

def auto_cpufan():
    on = ec_read(CPUFAN_CR) & ~0b1100
    on |= 0b0100
    ec_write(CPUFAN_CR, on)

def auto_gpufan():
    on = ec_read(GPUFAN_CR) & ~0b110000
    on |= 0b010000
    ec_write(GPUFAN_CR, on)

def manual_cpufan():
    on = ec_read(CPUFAN_CR) & ~0b1100
    on |= 0b1100
    ec_write(CPUFAN_CR, on)

def manual_gpufan():
    on = ec_read(GPUFAN_CR) & ~0b110000
    on |= 0b0110000
    ec_write(GPUFAN_CR, on)

def turbo_cpufan():
    on = ec_read(CPUFAN_CR) & ~0b1100
    on |= 0b1000
    ec_write(CPUFAN_CR, on)

def turbo_gpufan():
    on = ec_read(GPUFAN_CR) & ~0b110000
    on |= 0b100000
    ec_write(GPUFAN_CR, on)


def set_cpufan(value):
    value = clamp(value,100)
    ec_write(CPUFAN_PWMR, value)

def set_gpufan(value):
    value = clamp(value,100)
    ec_write(GPUFAN_PWMR, value)


def fan_auto():
    auto_cpufan()
    auto_gpufan()

def fan_max():
    turbo_cpufan()
    turbo_gpufan()

def fan_manual():
    manual_cpufan()
    manual_gpufan()


def set_profile(value):
    profiles = [0,1,4,5]
    ec_write(PROFILE_REG,profiles[value])

def set_color(r,g,b,br=100):
    r=clamp(r,255)
    g=clamp(g, 255)
    b=clamp(b, 255)
    br=clamp(br,100)

    colors = [r,g,b, r,g,b, r,g,b]
    for i in range(0,9):
        ec_write(COLOR_REG_OFFSET+i,colors[i])
    ec_write(KEY_RIGHTNESS, br)
    if (ec_read(KEY_ACTIVATE) != 0x07):
        ec_write(KEY_ACTIVATE, 0x07)
    ec_write(KEY_RIGHTNESS, br)


#default script
if __name__ == "__main__":
    set_color(256,256,128,10)
    start()

    manual_cpufan()
    manual_gpufan()
    set_cpufan(100)
    set_gpufan(100)
    set_profile(0) # lowest
    sleep(10)
    set_cpufan(0)
    set_gpufan(0)


    
