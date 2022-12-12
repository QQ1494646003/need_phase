#!/usr/bin/env python
# -*- coding: gbk-*-

import math
import time
import numpy as np
import matplotlib.pyplot as  plt

px=0
py=0
s=[]
phase=[]#np.arange(0,100*100,1,dtype=float).reshape(20,20)
init_phase=0
PI=3.141592653589793
def PA_phase(a,f,frequency):
    i=0
    j=0
    acc=0
    global s,phase
    s=[]
    phase=[]#np.arange(0,100*100,1,dtype=float)
    wl=3e11/(frequency*1e9)#wavelength
    print("cacul PA_phs")
    time.sleep(1)
    while i < a:

        while j <  a:
            dx = (2*i-a+1)*px/2
            #ax=100;x/2
            dy = (2*j-a+1)*py/2
            phas=(360 * (math.sqrt(dx * dx + dy * dy + f * f) - f)) / wl+init_phase;#抛物相位
            #phas=ax*(360*(math.sqrt((pow(dx,2)+ pow(dy, 2))/(pow(f,2)-pow(ax,2))+1  )))/wl
            while phas>360:
                phas-=360;
            #if 85<phas<=265:
            #    phas=175
            #else:
            #    phas=355
            phase.append(phas)
            cache="{:.2f}".format(phas)
            s.append(cache+" ")
            #print("%.2f"%phas)#输出相位
            j+=1
            acc+=1
        i+=1
        j=0
    #print(phase)

def txt(a):
    global s
    file="E:\\phx\\need_phase.txt"
    with open(file,"w+") as f:
        i=0
        print("creating file")
        while i < a*a:
            f.write(str(s[i]))
            i+=1
        time.sleep(1)
        print("creating complete")
def Vortex_beam(a,f,frequency):
    PA_phase(a,f,frequency)
    global s,phase
    acc=0
    s=[]
    #print(s)
    i = 0
    j=0
    print("cacul VBE_phs + PA_phs")
    time.sleep(1)
    while i < a:

        while j <  a:
            dx = (2*i-a+1)*px/2
            #ax=100;x/2
            dy = (2*j-a+1)*py/2
            if (dx==0)&(dy==0):
                theta=0
            else:
                r=math.sqrt(math.pow(dx,2)+math.pow(dy,2))
                cos_theta=dy/r 
                theta=math.acos(cos_theta)*360/PI #owing to the acos function result is rad rather than degree
                if dx>=0:
                    theta=theta
                else :
                    if dx<0:
                        theta=360-theta
            phase[acc]=theta+phase[acc]
            while phase[acc]>360:
                phase[acc]-=360
            while phase[acc]<0:
                phase[acc]+=360
            cache="{:.2f}".format(phase[acc])
            s.append(cache+" ")
            #print("%.2f"%phase[acc])#输出相位
            j+=1
            acc+=1
        i+=1
        j=0
    #print(s)

if __name__=="__main__":#main function
    while True:
        px=float(input("Length_x of CELL"))
        py=float(input("Length_y of CELL"))
        arr_len=int(input("the length of the array"))
        f=float(input("the f of the array"))
        frequency=float(input("Work Frequency"))
        print("what type of array do you need?\nparaboloid(PA);Vortex beam(VBE)?")
        w=input()
        if ("pa"in w)|("PA" in w):
            PA_phase(arr_len,f,frequency)
            #fig =plt.figure()#matplotlib fingure
            #ax=fig.add_subplot(projection="3d")
        if ("vbe"in w)|("VBE" in w):
            Vortex_beam(arr_len,f,frequency)
        txt(arr_len)