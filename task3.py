import RPi.GPIO as GPIO
import time
def  decToBinList(decNumber):
    a=bin(decNumber)[2:].zfill(8)
    a=list(map(int,a))
    return a

def num2dac(value):
    a=decToBinList(int(value))
    num_list=[] 
    for i in range(len(a)):
        if a[i]==1:
            num_list.append(chan_list[i])
    #print(num_list)
    GPIO.setup(num_list, GPIO.OUT)
    GPIO.output(num_list, 3)
    time.sleep(0.01)
    GPIO.output(num_list, 0)
    
def repetitionsNumber(number):    
    for i in range(number):
        a=0
        while a!=256:
            num2dac(a)
            a+=1
        a=255
        while a!=0:
            num2dac(a)
            a-=1
GPIO.setmode(GPIO.BCM)
chan_list=[26,19,13,6,5,11,9,10]

try:
    print("Enter the repetition number")
    a=int(input())
    repetitionsNumber(a)

    
finally:
    GPIO.cleanup()