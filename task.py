import RPi.GPIO as GPIO
import time

#GPIO.output(chan_list,0)
chan_list=[21,20,16,12,7,8,25,24]


def lightUp(ledNumber,period):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(chan_list, GPIO.OUT)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)
    time.sleep(period)
    GPIO.cleanup()
def dark(ledNumber,period):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(chan_list, GPIO.OUT)
    GPIO.output(ledNumber, 0)
    time.sleep(period)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.cleanup()    

def blink(ledNumber,blinkCount,blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber,blinkPeriod)
    GPIO.cleanup()    

def runningLight(count,period):
    for j in range(count):
        for i in range(len(chan_list)):
            lightUp(chan_list[i],period)     

def runningDark(count,period):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(chan_list, GPIO.OUT)
    GPIO.output(chan_list, 1)
    for j in range(count):
        for i in range(len(chan_list)):
            dark(chan_list[i],period)
    GPIO.output(chan_list, 0)
    GPIO.cleanup() 

def  decToBinList(decNumber):
    a=format(decNumber,'b')
    s=[0,0,0,0,0,0,0,0]
    b=list(a)
    k=len(b)
    n=len(s)
    while k!=0:
        s[n-1]=int(b[k-1])
        n-=1
        k-=1
    return s

def lightNumber(number):
    GPIO.setmode(GPIO.BCM)
    chan_list=[21,20,16,12,7,8,25,24]
    GPIO.setup(chan_list, GPIO.OUT)
    a=decToBinList(int(number))
    num_list=[]
    for i in range(len(a)):
        if a[i]==1:
            num_list.append(chan_list[i])
    #print(num_list)
    GPIO.output(num_list, 1)
    time.sleep(1)
    GPIO.output(num_list, 0)
    GPIO.cleanup()


def runningPattern(pattern,direction):
    
    k=0
    b=[0,0,0,0,0,0,0,0]
    a=decToBinList(int(pattern))
    if direction==0:
        k=a[-1]
        for i in range(8):
            
            if i!=7:
                b[i+1]=a[i]
            if i==7:
                b[0]==k
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(b, GPIO.OUT)
            GPIO.output(b,1)
            time.sleep(1)
    if direction==1:
        k=a[0]
        for i in range(8):
            if i!=0:
                b[i]=a[i-1]
            if i==0:
                b[i]==k
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(b, GPIO.OUT)
            GPIO.output(b,1)
            time.sleep(1)


#lightUp(21,0.1)
#blink(20,4,0.1)
#runningLight(2,0.1)
#runningDark(2,0.1)
#print(decToBinList(232))
#lightNumber(31)
runningPattern(232,0)
#runningPattern(3,1)
GPIO.output(chan_list, 0)
GPIO.cleanup()