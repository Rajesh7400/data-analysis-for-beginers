#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[26]:


df = pd.read_csv("file.csv")


# In[27]:


df.head()


# In[28]:


df.dtypes


# In[8]:


df.nunique()


# In[9]:


df.count()


# In[10]:


df['Date/Time'].value_counts()


# In[11]:


#FIND UNIQUE VALUES IN WIND COLUMN
df["Wind Speed_km/h"].unique()


# In[ ]:


# Find the number of times when weather is clear
df.Weather.value_counts()


# In[15]:


#Other way by filtering the data
df[df.Weather=='Clear']


# In[16]:


#other way we can use groupby
df.groupby('Weather').get_group('Clear')


# In[17]:


#how many times wind speed is 4km/h
df[df['Wind Speed_km/h']==4]


# In[20]:


# find the null values
df.isnull().sum()


# In[31]:


# renaming the column nme
df.rename(columns={'Weather':'weather_condition'}, inplace=True)


# In[32]:


df


# In[33]:


# converting column names lower case
df.columns=df.columns.str.lower()


# In[34]:


df.head(2)


# In[44]:


df.columns.str.replace(r'[^a-z,A-Z,0-9]','_',regex=True)


# In[53]:


df.rename(columns={'rel hum__':'humidity'},inplace=True)


# In[54]:


df.head(2)


# In[56]:


# all instances of snow condition
df[df['weather_condition'].str.contains('Snow')]


# In[57]:


df.groupby('weather_condition').get_group('Snow')


# In[58]:


# when wind speed is greter then 24 and visiblity equal to 25
df[(df['wind speed_km/h']>24) & (df['visibility_km']== 25)]


# In[ ]:




