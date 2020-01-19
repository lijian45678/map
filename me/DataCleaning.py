# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 14:31
# @Author  : LiJian
# @Site    : 
# @File    : DataCleaning.py
# @Software: PyCharm
import time
import numpy as np
import sys
import os
import csv


class TrackPoint:
    def __init__(self ,  latitude =0.0, longitude =0.0 ,time=0 ):
        self.latitude =latitude
        self.longitude = longitude
        self.time = time
    def print(self):
        print(self.latitude+' '+self.longitude+' '+self.time)
def compare_time(time1,time2):
    s_time = time.mktime(time.strptime(time1,'%Y-%m-%d %H:%M:%S'))
    e_time = time.mktime(time.strptime(time2,'%Y-%m-%d %H:%M:%S'))
    return int(s_time) - int(e_time)
if __name__ == '__main__':
    startTime1 = time.time()
    listData = [] #轨迹序列
    rootdir = 'C:\\Users\\LJ\\Desktop\\TA\\Data\\004\\Trajectory'
    #rootdir = 'C:\\Users\\lcy\\Desktop\\HardwareSimulator\\TrackAnalysis\\Geolife Trajectories 1.3\\Data\\000\\Trajectory'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as f:
                fileList = f.readlines()
                for dataLine in fileList[6:fileList.__len__()]:
                    dataLineList=dataLine.split(',')
                    trackPoint = TrackPoint(float(dataLineList[0]),float(dataLineList[1]),
                                            int(time.mktime(time.strptime( str(dataLineList[5]+' '+dataLineList[6]).split('\n')[0], '%Y-%m-%d %H:%M:%S'))))
                    listData.append(trackPoint)
            f.close()

    for i in range(len(listData)-1):
            if (listData[i].time-listData[i + 1].time) > 0 :
                print("重新排序")
                listData.sort(key=TrackPoint.time)
    print('轨迹点序列排列正确，完成第一步，总计点数是：',len(listData))
    with open('data/user004.csv', 'w', newline='') as csvfile:
        fieldnames=['latitude','longitude','time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for x in listData:
            writer.writerow({"latitude":x.latitude,"longitude":x.longitude,"time":x.time})