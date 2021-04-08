import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
import math as math

def  decToBinList(decNumber):
    a=bin(decNumber)[2:].zfill(8)
    a=list(map(int,a))
    return a

def num2dac(value,time1):
    a=decToBinList(int(value))
    num_list=[] 
    for i in range(len(a)):
        if a[i]==1:
            num_list.append(chan_list[i])
    #print(num_list)
    GPIO.setup(num_list, GPIO.OUT)
    GPIO.output(num_list, 3)
    time.sleep(time1)
    GPIO.output(num_list, 0)
    
def repetitionsNumber(time):    
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
samplingFrequency=5
def graph(frequency):
    x=np.arange(0,20,frequency)
    y=np.sin(x)*128+128
    plt.plot(x,y)
    plt.show()
    for i in y:
        a=y[i]
        if a<0:
            continue
        else:
            num2dac(int(a),1/samplingFrequency)    
        
try:
    print("Enter the frequency")
    a=float(input())
    graph(a)
    


    
finally:
    GPIO.cleanup()