from math import *
for _ in range(int(input())):v,a,x,h,j=map(float,input().split());t=x/(v*cos(a:=pi/180*a));print('Not '*(not j-1>v*t*sin(a)-1/2*9.81*t*t>h+1)+'Safe')