# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 16:21
# @Author  : LiJian
# @Site    : 
# @File    : Distance.py
# @Software: PyCharm
import math
import csv
from math import radians, cos, sin, asin, sqrt,pi
EARTH_REDIUS = 6378.137

def rad(d):
    return d * pi / 180.0
def getDistance(lat1, lng1, lat2, lng2):
            radLat1 = rad(lat1)
            radLat2 = rad(lat2)
            a = radLat1 - radLat2
            b = rad(lng1) - rad(lng2)
            s = 2 * math.asin(
                math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * math.pow(sin(b / 2), 2)))
            s = s * EARTH_REDIUS
            return s * 1000

def get_address_distance(lat1,lon1,lat2,lon2):
    # lon1 = 104.071000
    # lat1 = 30.670000
    # lon2 = 104.622000
    # lat2 = 28.765000
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半径，单位为公里
    #返回结果除以米为单位保留两位小数
    return int(c * r * 1000)