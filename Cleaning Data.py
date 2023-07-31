#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"C:\Users\tsale\Downloads\Customer Call List.xlsx")
df


# In[3]:


df = df.drop_duplicates()


# In[4]:


df.drop(columns = "Not_Useful_Column", inplace = True)


# In[5]:


df["Last_Name"] = df["Last_Name"].str.strip("..._/")
df


# In[6]:


df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '')
df


# In[7]:


df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])


# In[8]:


df['Phone_Number'] = df['Phone_Number'].str.replace("nan--", "")
df['Phone_Number'] = df['Phone_Number'].str.replace("Na--", "")
df


# In[9]:


df[["Street_Address", "State", "Zip_Code"]] = df['Address'].str.split(",", 2, expand = True)
df


# In[10]:


df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")
df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")
df


# In[11]:


df = df.fillna("")


# In[12]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y":
        df.drop(x, inplace = True)
        
for x in df.index:
    if df.loc[x, "Phone_Number"] == "":
        df.drop(x, inplace = True)
        
df


# In[15]:


df.reset_index(drop= True, inplace = True)


# In[16]:


df


# In[ ]:




