# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:56:25 2021

@author: river
"""


import pandas as pd
import folium

station_info=pd.read_csv('..\dataset\con_sta_info.csv')
station_info.head()

station_info=station_info[['ID','Y','X']]
station_info.rename(columns={'Y':'위도','X':'경도'}, inplace=True)

lat=station_info['위도'].mean()
long=station_info['경도'].mean()

# 지도 띄우기
view_map=folium.Map([lat,long], zoom_state=9)
view_map