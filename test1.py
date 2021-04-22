import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
troyka = 17
comp=4

GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def num2dac(num):
    a = list(map(int, bin(num)[2:].zfill(8)))
    for i in range(8):
        GPIO.output(dac[i], a[i])

try:
    GPIO.output(17, 1)
    while True:
        num=0
        num2dac(num)
        a=GPIO.input(comp)
        #print(a)
        while a!=0:
            num+=1
            num2dac(num)
            a=GPIO.input(comp)
            time.sleep(0.01)
            #print(a)
            #print(num)
        print(num)
        print(3.24 / 255 * num)

finally:
    GPIO.output(17, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()