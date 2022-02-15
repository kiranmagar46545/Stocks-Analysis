#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd



airtel = pd.read_csv(r"C:\save temp\Stock Datasets\airtel_df.csv",parse_dates=["Date"])
infy = pd.read_csv(r"C:\save temp\Stock Datasets\infy_df.csv",parse_dates=["Date"])
reliance = pd.read_csv(r"C:\save temp\Stock Datasets\reliance_df.csv",parse_dates=["Date"])
tcs = pd.read_csv(r"C:\save temp\Stock Datasets\tcs_df.csv",parse_dates=["Date"])


# In[2]:


print("Airtel Data:\n",airtel.head(1))
print(airtel.tail(1))
print("INFY Data:\n",infy.head(1))
print(infy.tail(1))
print("Reliance Data:\n",reliance.head(1))
print(reliance.tail(1))
print("TCS Data:\n",tcs.head(1))
print(tcs.tail(1))


# In[3]:


print(airtel.isnull().sum())
airtel=airtel.dropna(how="any",axis=0)
print(airtel.isnull().sum())


# In[4]:


print(infy.isnull().sum())
infy=infy.dropna(how="any",axis=0)
print(infy.isnull().sum())


# In[5]:


print(reliance.isnull().sum())
reliance=reliance.dropna(how="any",axis=0)
print(reliance.isnull().sum())


# In[6]:


print(tcs.isnull().sum())
tcs=tcs.dropna(how="any",axis=0)
print(tcs.isnull().sum())


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


airtel["Open"].plot(c="r",figsize=(15,7))
infy["Open"].plot(c="g")
reliance["Open"].plot(c="b")
tcs["Open"].plot(c="y")
plt.show()


# In[11]:


plt.plot(airtel["Volume"].astype(int),c="r")
plt.plot(infy["Volume"].astype(int),c="g")
plt.plot(reliance["Volume"].astype(int),c="b")
plt.plot(tcs["Volume"].astype(int),c="y")
plt.show()


# In[12]:


airtel["Total Trade"] = airtel["Open"]*airtel["Volume"]
infy["Total Trade"] = infy["Open"]*infy["Volume"]
reliance["Total Trade"] = reliance["Open"]*reliance["Volume"]
tcs["Total Trade"] = tcs["Open"]*tcs["Volume"]


# In[13]:


airtel["Total Trade"].plot(label="Airtel",figsize=(15,7),c="r")
infy["Total Trade"].plot(label="INFY",c="g")
reliance["Total Trade"].plot(label="Reliance",c="b")
tcs["Total Trade"].plot(label="TCS",c="y")
plt.show()


# In[14]:


# moving avarage
def mov_av(name):
    name["Open"].plot(c="y", figsize=(15, 7))
    name["MA50"] = name["Open"].rolling(50).mean()
    name["MA50"].plot(label="MA50", c="r")
    plt.show()
mov_av(airtel)
mov_av(infy)
mov_av(reliance)
mov_av(tcs)


# In[15]:


import seaborn as sns


# In[16]:


def corr(name):
    print(name.corr())
    sns.heatmap(name.corr())
    plt.show()
corr(reliance)


# In[18]:


def pairplot(name):
    sns.pairplot(name)
    plt.show()
pairplot(reliance)


# In[19]:


airtel["returns"]= ((airtel["Close"]/airtel["Close"].shift(1))-1)*100
infy["returns"]= ((infy["Close"]/infy["Close"].shift(1))-1)*100
reliance["returns"]= ((reliance["Close"]/reliance["Close"].shift(1))-1)*100
tcs["returns"]= ((tcs["Close"]/tcs["Close"].shift(1))-1)*100


# In[20]:


print("Airtel Data:\n",airtel.head(1))
print(airtel.tail(1))
print("INFY Data:\n",infy.head(1))
print(infy.tail(1))
print("Reliance Data:\n",reliance.head(1))
print(reliance.tail(1))
print("TCS Data:\n",tcs.head(1))
print(tcs.tail(1))


# In[23]:


plt.hist(airtel["returns"],bins=150,label="Airtel",alpha=0.5)
plt.hist(infy["returns"],bins=150,label="Infosys",alpha=0.5)
plt.hist(reliance["returns"],bins=150,label="Reliance",alpha=0.5)
plt.hist(tcs["returns"],bins=150,label="TCS",alpha=0.5)
plt.legend()
plt.show()


# In[24]:


box= pd.concat([airtel["returns"],infy["returns"],reliance["returns"],tcs["returns"]],axis=1)
box.columns=["Airtel Returns","INFY Returns","Reliance Returns","TCS Returns"]
box.plot(kind="box")
plt.show()

