#!/usr/bin/env python
# coding: utf-8

# In[407]:


import numpy as np
import pandas as pd


# In[408]:


# load data file 
df = pd.read_csv('store_metrics.csv')


# In[409]:


df


# In[410]:


# Finding the Totral Price Paid 

df['TOTAL AMOUNT'] = df['AMOUNT'] * df['UNIT PRICE']
print(df)




# In[411]:


# change the TIMESTAMP to Standard Datetime 

from datetime import datetime
df['DATETIME'] = df['TIMESTAMP'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%Y-%m-%d'))
df = df.drop(columns=['TIMESTAMP'])
df= df [['DATETIME', 'STORE LOCATION', 'UNIT TYPE', 'AMOUNT','UNIT PRICE','TOTAL AMOUNT']]
df


# In[412]:



# Get rid of days where the TOTAL AMOUNT was $0 

new_df = df[df['AMOUNT']!= 0]
new_df



# In[414]:


# find the maximum total sales per day 
new_df = new_df[new_df.groupby('DATETIME')['TOTAL AMOUNT'].transform('max') == new_df['TOTAL AMOUNT']]
new_df


# In[428]:


# Export as an Excel Spreadsheet

new_df.to_csv('OmegaATS_Complete.csv')



# In[ ]:





# In[ ]:





# In[ ]:




