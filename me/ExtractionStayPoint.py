# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 14:01
# @Author  : LiJian
# @Site    : 
# @File    : ExtractionStayPoint.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from me.Distance import getDistance
import csv

Wd=200.0
Wt=10*60

data = np.loadtxt("data/user001.csv", delimiter=",")
#标记
a = [0 for _ in range(len(data))]
re = []
i=0
while(i<len(data)):
    n = i+1
    m = i-1
    while((n+1)<len(data) and getDistance(data[i][0],data[i][1],data[n][0],data[n][1])<100.0):
        n=n+1
    while( (m - 1) > -1 and getDistance(data[i][0], data[i][1], data[m][0], data[m][1]) < 100.0):
        m = m - 1
    dt=data[n][2]-data[m][2]
    if(dt>300):
        re.append([m,n,i,dt])
    i = n+1
re.sort(key=(lambda x:x[3]),reverse= True)

with open('data/user001_candidate_points_200_300.csv', 'w', newline='') as csvfile:
    fieldnames = ['startLabel','endLabel','centerLabel', 'timeLength']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for x in re:
      writer.writerow({'startLabel':x[0],'endLabel':x[1],'centerLabel':x[2], 'timeLength':x[3]})
print(re)
# print(data[1][0],data[1][1],data[2][0],data[2][1])
# listDat=[]
# with open('data/user004.csv', 'w', newline='') as csvfile:
#     fieldnames = ['startLabel','endLabel','centerLabel', 'timeLength']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
