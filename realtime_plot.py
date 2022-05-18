# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:21:50 2021

@author: frenz
"""
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
x_vals=[]#[0,1,2,3,4,5]
y_vals=[]#[0,1,3,2,3,5]
plt.plot(x_vals,y_vals)

index=  count()
def animate(i):
    data=pd.read_csv('ftpserver/Data.csv')
    x=data['x_vals']
    y1=data['tot_1']
    y2=data['tot_2']
    curr_x=x.iloc[-1]
    curr_y1=y1.iloc[-1]
    curr_y2=y2.iloc[-1]
    print(curr_x,curr_y1,curr_y2)
# =============================================================================
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0,5))
# =============================================================================
    
    #plt.scatter(curr_x,curr_y1,marker=''s=14)
   # plt.scatter(curr_x,curr_y2,marker='o's=14)
    plt.cla()
    plt.plot(curr_x,curr_y1,'-x',color='blue')
    plt.plot(curr_x,curr_y2,'-x',color='black')
    plt.plot(x,y1, label='channel 1',color='blue',linewidth=1)
    plt.plot(x,y2,label='channel 2',color='black',linewidth=1)
    plt.xlim([0,500])
    plt.ylim([999,1003])
    
    
    plt.legend(loc='upper left')
    
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),animate,interval=100)

plt.show()