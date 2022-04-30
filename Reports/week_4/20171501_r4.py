#!/usr/bin/env python
# coding: utf-8

# # Report 4

# 
# The Colonial Origins of Comparative Development: An Empirical Investigation Author(s): Daron Acemoglu, Simon Johnson, James A. Robinson
# 
# 
# The principal interest of the article is to identify the most important causes of the differences in income per capita across countries, for that reason the paper validate itself by presenting graphics about the relation between institutions and factors of efficiency.
# The authors propose a theory of institutional differences among countries colonized by Europeans their principal arguments rely on the arguments that the different types of colonization policies witch leaded to different institutions, how much was the colonization affected for the facility of settlement for Europeans, and the fact that institution persisted after independence.    
# This document helps to support the vision of the development in Latin America is not just a matter of development of the society after independence, instead, a sum of factors that are related to each other. The view of international relations as an academy area is often influenced by the perception of american international relations, one that often does not take the responsibility of the colonies, their past and effects to the present. Having an academic American paper that makes visible the effects in the structural bases for the institution in this countries helps to strengthen the  same opinion that latin America had for itself, but with the visibility that requires.     
# 
# Its necesary to take in count in which year was done this paper, when we considerate the data disponibility in 2001, we can observe how much effort implied. Neverless its still difficult to asume that the papers focused on development studing past cases are totaly conclusive, particulary because every academic would give more inportance, as the autors mentioned before, to different variables in their own investigations. 
# 
# 
# 

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings 
import seaborn as sns
import statistics


# In[123]:


columns = ['Year', 'PBIperc']
df = pd.read_excel(r"C:\Users\DELL\Downloads\Anuales-20220430-084922.xlsx", header = None, names = columns)
df=df[2:102]
df


# In[124]:


df['growth_rate']=df['PBIperc'].pct_change()
df['growth_rate']=df['growth_rate']*100


# In[160]:


df


# In[157]:


plt.figure(figsize=(10,6))
sns.lineplot(x='Year',y='PBIperc',data=df)
plt.ylabel("PERU GDP percapita")
plt.title("PERU GDP percapita from 1922-2021")


# This first graphic shows us that between 1922 to 2021, Peru GDP per capita  tends to increase, except between 1980 and around 1990 where we observe the most considerable decrease in these years. The graphic itselve its not able to comunicate us how much is indeed growing, because we dont separate or study population grow from the apparent increment of GDP.
# Neverless, independient from other factors, we are able to observe that the years of decline match times with the armed conflict and aparicion of MRTA, apart from that, we would need to consider that the presidents of these years were Alan Garcia and Fujimomri. These social and political condicions could be part of the reason why the GDP between these years is affected. 

# In[151]:


df2=df[3:102]
x = statistics.mean(df2.growth_rate)
print("Mean is :", x)


# In[161]:


plt.figure(figsize=(10,6))
sns.lineplot(x='Year',y='growth_rate',data=df)
plt.ylabel("Annual Growth Rate of real GDP per Capita in PERU (in %)")
plt.axhline(y=1.86, color='red',linestyle='-')
plt.axhline(y=0, color='black',linestyle='--')
plt.title("Annual Growth Rate of real GDP per Capita in PERU Between 1922 and 2021")


# In this graphic we observe the mean of GDP per capita in Peru between 1922-2021 represented in the red line, it's slightly higher that the zero. We observe that the anual grow rate is not frecuently stable. The years between 1940 and 1980 would be the most regular ones, while the next 20 years would be the most irregulars, coinciding with the previous statement that the political context affected the GDP development negatively. It was expected that the first COVID year would had a big decrease.
