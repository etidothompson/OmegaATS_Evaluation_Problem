# OmegaATS_Evaluation_Problem

# Ensure you have proper libraries installed and if not go on terminal and install them

:~ etidothompson$ pip install pandas

:~ etidothompson$ pip install datetime

# make sure you have python and verify by checking on terminal by calling python

:~ etidothompson$ python


# import necessary libraries on a code editor  

import numpy as np
import pandas as pd

# load data file 

df = pd.read_csv('store_metrics.csv')

# Finding the Totral Price Paid 
df['TOTAL AMOUNT'] = df['AMOUNT'] * df['UNIT PRICE']

# change the TIMESTAMP to Standard Datetime 

from datetime import datetime

df['DATETIME'] = df['TIMESTAMP'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%Y-%m-%d'))
df = df.drop(columns=['TIMESTAMP'])
df= df [['DATETIME', 'STORE LOCATION', 'UNIT TYPE', 'AMOUNT','UNIT PRICE','TOTAL AMOUNT']]

# Get rid of days where the TOTAL AMOUNT was $0 

new_df = df[df['AMOUNT']!= 0]


# find the maximum total sales per day 

new_df = new_df[new_df.groupby('DATETIME')['TOTAL AMOUNT'].transform('max') == new_df['TOTAL AMOUNT']]
new_df

# Export as an Excel Spreadsheet

new_df.to_csv('OmegaATS_Complete.csv')

