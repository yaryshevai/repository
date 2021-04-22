import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
troyka = 17

GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)

def num2dac(num):
    a = list(map(int, bin(num)[2:].zfill(8)))
    for i in range(8):
        GPIO.output(dac[i], a[i])

try:
    GPIO.output(17, 1)
    
    while True:
        num = int(input("Enter number > "))
        num2dac(num)
        print(3.24 / 255 * num)

finally:
    GPIO.output(17, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()