#!/usr/bin/env python
# -*- coding: gbk-*-

import math
import time
import numpy as np
import matplotlib.pyplot as  plt
import seaborn as sns



px=0
py=0
s=[]
phase=np.array([])#np.arange(0,100*100,1,dtype=float).reshape(20,20)
init_phase=0
PI=3.141592653589793



def PA_phase(a,f,frequency):
    i=0
    j=0
    acc=0
    global s,phase
    s=[]
    phase=np.zeros((a,a))#np.arange(0,100*100,1,dtype=float)
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
            phase[i,j]=phas
            cache="{:.2f}".format(phas)
            s.append(cache+" ")
            #print("%.2f"%phas)#phase print
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
        print("creating file TO E:\\phx\\need_phase.txt")
        while i < a*a:
            f.write(str(s[i]))
            i+=1
        time.sleep(1)
        print("creating complete")
def Vortex_beam(a,f,frequency):
    m=float(input("num of modes"))
    PA_phase(a,f,frequency)
    global s,phase
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
                theta=m*math.acos(cos_theta)*180/PI #owing to the acos function result is rad rather than degree
                if dx>=0:
                    theta=theta
                else :
                    if dx<0:
                        theta=360-theta
            phase[i,j]=theta+phase[i,j]
            while phase[i,j]>360:
                phase[i,j]-=360
            while phase[i,j]<0:
                phase[i,j]+=360
            cache="{:.2f}".format(phase[i,j])
            s.append(cache+" ")
            #print("%.2f"%phase[acc])#phase print
            j+=1
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
        sns.set()
        plt.rcParams['font.sans-serif']='SimHei'#设置中文显示，必须放在sns.set之后

        f, ax = plt.subplots(figsize=(9, 6))

#heatmap后第一个参数是显示值,vmin和vmax可设置右侧刻度条的范围,
#参数annot=True表示在对应模块中注释值
# 参数linewidths是控制网格间间隔
#参数cbar是否显示右侧颜色条，默认显示，设置为None时不显示
#参数cmap可调控热图颜色，具体颜色种类参考：https://blog.csdn.net/ztf312/article/details/102474190
        #sns.heatmap(phase, ax=ax,vmin=0,vmax=360,cmap='viridis',annot=False,linewidths=2,cbar=True)
        sns.heatmap(phase, ax=ax,cmap='viridis',annot=False,linewidths=0,cbar=True)
        ax.set_title('phase') #plt.title('热图'),均可设置图片标题
        ax.set_ylabel('Y')  #设置纵轴标签
        ax.set_xlabel('X')  #设置横轴标签

#设置坐标字体方向，通过rotation参数可以调节旋转角度
        label_y = ax.get_yticklabels()
        plt.setp(label_y, rotation=360, horizontalalignment='right')
        label_x = ax.get_xticklabels()
        plt.setp(label_x, rotation=90, horizontalalignment='right')
        sns.set(font_scale=1.5)
        plt.rc('font',family='Times New Roman',size=24)
        plt.show()
