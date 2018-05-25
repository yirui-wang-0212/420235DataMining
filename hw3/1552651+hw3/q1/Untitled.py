
# coding: utf-8

# In[79]:


import pandas as pd
from pandas import DataFrame
import math


# In[82]:


# 合并两张表，用 data_2g 中的 RNCID_1，CellID_1 与 gongcan_2g 的 RNCID，CellID 匹配，将基站的经纬度信息加到 data_2g 中
def merge_data_gongcan():
    data_2g = pd.read_csv('../../raw_data/data_2g.csv')
    gongcan_2g = pd.read_csv('../../raw_data/2g_gongcan.csv')
    for i in range(1, 8):
        # 换掉 gongcan_2g 的列名用以和 data_2g merge
        gongcan_2g.columns = ['RNCID_' + str(i), 'CellID_' + str(i), 'Lat_' + str(i), 'Lon_'+str(i)]    
        data_2g = pd.merge(data_2g, gongcan_2g, on=['RNCID_' + str(i), 'CellID_' + str(i)])
    return data_2g


# In[83]:


data = merge_data_gongcan()


# In[86]:


data

