#!/usr/bin/env python
# coding: utf-8

# In[151]:


import numpy as np
import pandas as pd

wares_info = [
    {"name": "ware_1",
    "price": 900,
    "weight": 100},
    
    {"name": "ware_2",
    "price": 75,
    "weight": 5},
    
    {"name": "ware_3",
    "price": 900,
    "weight": 30},
    
    {"name": "ware_4",
    "price": 750,
    "weight": 1},
    
    {"name": "ware_5",
    "price": 5,
    "weight": 35},
    
    {"name": "ware_6",
    "price": 5,
    "weight": 10},
    
    {"name": "ware_7",
    "price": 2,
    "weight": 1},
    
    {"name": "ware_8",
    "price": 800,
    "weight": 20},
    
    {"name": "ware_9",
    "price": 900,
    "weight": 15},
]


# In[152]:


p_w_rate = []
for i in wares_info:
    
    rate = i["weight"]/i["price"]
    p_w_rate.append([rate, i["name"], i["weight"], i["price"]])
    
p_w_rate = pd.DataFrame(p_w_rate, columns=["rate", "name", "weight", "price"])
p_w_rate = p_w_rate.sort_values(by = "rate")
p_w_rate = np.array(p_w_rate)


# In[153]:


inside_knapsack = []
capasity_knap = 75
for i in np.arange(len(p_w_rate)):
    if p_w_rate[i][2] < capasity_knap:
            inside_knapsack.append([p_w_rate[i][1], p_w_rate[i][3], p_w_rate[i][2]])
            capasity_knap = capasity_knap - p_w_rate[i][2]
    if i == len(p_w_rate):
        break
        


# In[154]:


inside_knapsack =  pd.DataFrame(inside_knapsack, columns=["name", "price", "weight"])
inside_knapsack

