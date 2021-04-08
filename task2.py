import RPi.GPIO as GPIO
import time
def  decToBinList(decNumber):
    a=bin(decNumber)[2:].zfill(8)
    b=[]
    for i in range(len(a)):
        b.append(int(a[i]))
    return b

def num2dac(value):
    a=decToBinList(int(value))
    num_list=[] 
    for i in range(len(a)):
        if a[i]==1:
            num_list.append(chan_list[i])
    #print(num_list)
    GPIO.setup(num_list, GPIO.OUT)
    GPIO.output(num_list, 3)
    time.sleep(8)
    GPIO.output(num_list, 0)
    

GPIO.setmode(GPIO.BCM)
chan_list=[26,19,13,6,5,11,9,10]

try:
    a=0
    
    while a!=-1:
        print("Enter the number")
        a=int(input())
        if a>255 or a<=-1:
            exit()
        else:
            num2dac(a)
    
finally:
    GPIO.cleanup()