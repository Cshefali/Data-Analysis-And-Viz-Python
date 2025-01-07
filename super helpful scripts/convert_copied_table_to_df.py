# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:12:13 2025

Author- Shefali C.
"""

import pandas as pd
import numpy as np

table_data = """
   Duration          Date  Pulse  Maxpulse  Calories
  60  '2020/12/01'    110       130     409.1
  60  '2020/12/02'    117       145     479.0
  60  '2020/12/03'    103       135     340.0
  45  '2020/12/04'    109       175     282.4
  45  '2020/12/05'    117       148     406.0
  60  '2020/12/06'    102       127     300.0
  60  '2020/12/07'    110       136     374.0
  450  '2020/12/08'    104       134     253.3
  30  '2020/12/09'    109       133     195.1
  60  '2020/12/10'     98       124     269.0
  60  '2020/12/11'    103       147     329.3
  60  '2020/12/12'    100       120     250.7
  60  '2020/12/12'    100       120     250.7
  60  '2020/12/13'    106       128     345.3
  60  '2020/12/14'    104       132     379.3
  60  '2020/12/15'     98       123     275.0
  60  '2020/12/16'     98       120     215.2
  60  '2020/12/17'    100       120     300.0
  45  '2020/12/18'     90       112       NaN
  60  '2020/12/19'    103       123     323.0
  45  '2020/12/20'     97       125     243.0
  60  '2020/12/21'    108       131     364.2
  45           NaN    100       119     282.0
  60  '2020/12/23'    130       101     300.0
  45  '2020/12/24'    105       132     246.0
  60  '2020/12/25'    102       126     334.5
  60    2020/12/26    100       120     250.0
  60  '2020/12/27'     92       118     241.0
  60  '2020/12/28'    103       132       NaN
  60  '2020/12/29'    100       132     280.0
  60  '2020/12/30'    102       129     380.3
  60  '2020/12/31'     92       115     243.0
"""

#split the data into rows
rows = table_data.strip().splitlines()
#extract header
header = rows[0].split()

#Create a nested list of each row above, converted to a list.
data = [row.split(maxsplit = len(header) - 1) for row in rows[1:]]

#Transpose these rows to columns
columns = list(zip(*data))

#convert each column to a dictionary of key:value where
# key is taken from the "header" list and value is a list
# taken from columns nested-tuple.

dict_data = {header[i] : list(columns[i]) for i in range(len(header))}

#convert this dictionary to dataframe
df = pd.DataFrame(dict_data, index=None)

#df.head()
df.info()

#Total missing values in the dataframe
df.isna().sum()

#All values are string right now, convert to correct datatype.
#Column- Duration
df['Duration'] = df['Duration'].astype(int)
#Column- Date
#remove the single quotes from Date column
df['Date'] = df['Date'].astype(str).str.strip("'")
#convert the Date column from string to Date
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
#count total number of NaNs
df['Date'].isna().sum()
#Replace NaT to 2020-12-01
df['Date'].fillna(pd.Timestamp('2020-12-01'), inplace=True)
#Column- Pulse
df['Pulse'] = df['Pulse'].astype(int)
#Column- MaxPulse
df['Maxpulse'] = df['Maxpulse'].astype(int)
#Column- Calories
df['Calories'] = df['Calories'].astype(float)
#replace NaN in Calories to mean of the calories value
df['Calories'].fillna(df['Calories'].median(), inplace=True)

#Check summary stats of each column
df.describe()

#save this file
df.to_csv('sample_data.csv', index=False)
