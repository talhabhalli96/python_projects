#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mpl


# In[3]:


df = pd.read_csv(r"C:\Users\tsale\Downloads\world_population.csv")
df


# In[4]:


df.info()


# In[6]:


df.describe()


# In[8]:


df.isnull().sum()


# In[9]:


df.nunique()


# In[12]:


df.sort_values(by = "Rank", ascending = True).head(15)


# In[24]:


sb.heatmap(df.corr(), annot = True)
mpl.rcParams['figure.figsize'] = (20,14)
mpl.show()


# In[29]:


df2 = df.groupby("Continent")['1970 Population', '1980 Population', '1990 Population', '2000 Population', '2010 Population', '2015 Population', '2020 Population', '2022 Population'].sum().sort_values(by = "2022 Population", ascending = False)


# In[30]:


df3 = df2.transpose()
df3


# In[31]:


df3.plot()


# In[32]:


df.boxplot()


# In[40]:


df.select_dtypes(include = ["object", "number"])


# In[ ]:




