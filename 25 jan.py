#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the required libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


sns.get_dataset_names()


# In[3]:


df= sns.load_dataset("planets")


# In[4]:


df


# In[5]:


df.method.unique()


# In[6]:


df.method.value_counts()


# In[7]:


df.head()


# In[8]:


sns.lineplot(x='year', y='distance', data=df, ci=None) #Confidence interval
plt.show()


# In[15]:


sns.lineplot(x='year', y='distance', data=df,hue='mass', ci=None)
plt.show()


# In[17]:


sns.lineplot(x='year', y='mass', data=df,hue='mass', ci=None)
plt.show()


# In[18]:


## Scatter plot
sns.scatterplot(x='year',y='distance',data=df, hue='mass')
plt.title("Scatter plot")
plt.show()


# In[19]:


## Bar plot (categorical estimate plot)
##A barplot is basically used to aggregate the categorical data according to some methods and by default its the mean. 
##It can also be understood as a visualization of the group by action. 
#To use this plot we choose a categorical column for 
##the x axis and a numerical column for the y axis and we see that it 
# creates a plot taking a mean per categorical column. 

sns.barplot(x='year', y='distance', data=df)
plt.show()


# In[20]:


sns.countplot(x='mass', data=df)
plt.show()


# In[21]:


sns.boxplot(x='distance',data=df)
plt.show()


# In[23]:


sns.boxplot(x='mass', y='distance', data=df)
plt.show()


# In[26]:


sns.violinplot(x='mass', y='distance', data=df)
plt.show()


# In[27]:


sns.stripplot(x='mass', y='orbital_period', data=df)
plt.show()


# In[29]:


sns.histplot(x='distance', data=df)
plt.show()


# In[30]:


sns.histplot(x='distance', data=df,hue='mass', kde=True) # kernel density estimation 
plt.show()


# In[31]:


sns.pairplot(data=df, hue='mass')
plt.show()


# In[32]:


sns.catplot(x='distance', data=df, kind='violin')
plt.show()


# In[33]:


sns.catplot(x='distance',y='mass',data=df)
plt.show()  


# In[ ]:




