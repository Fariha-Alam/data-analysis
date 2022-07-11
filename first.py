#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('vgsales.csv')


# In[3]:


df


# In[4]:


df.head(5)


# In[12]:



#Rename columns
df=df.rename(columns={'NA_Sales':'Na','EU_Sales':'EU','JP_Sales':'JP'})


# In[10]:


df


# In[13]:


df


# # Null Value Check
# 

# # Q1.What genre has been sold the most between 2000-2015?

# In[18]:


df.head(2)


# In[24]:


df_Genre=df[(df['Year']>=2000)&(df['Year']<=2015)]['Genre'].value_counts()
df_Genre.head(5)


# # Q2.Null-'Publihser' will be replaced by 'Unknown'

# In[25]:


df.head(2)


# In[26]:


df['Publisher']=df['Publisher'].fillna('Unknown')


# In[27]:


df['Publisher']


# In[28]:


df.isnull().sum()


# # the most profitable type of game in Europe

# In[30]:


import   numpy as np
df.groupby('Genre')['EU'].agg(np.mean).sort_values(ascending=False)


# In[35]:


import seaborn as sns
sns.set(rc={'figure.figsize':(15,8)})
plot=sns.barplot(x='Genre',y='EU',data=df,ci=None)
plot.set_xticklabels(plot.get_xticklabels(),rotation=110);


# # the most  profitable game

# In[36]:


df.head(2)


# In[50]:


df.groupby('Genre')['Global_Sales'].agg(np.mean).sort_values(ascending=False)


# # What about the most common genre?

# In[45]:


genre=df['Genre'].mode()[0]
genre


# # What are the top 20 highest grossing games?

# In[47]:


def ques():
    for i in range (20):
        print(df['Name'][i])
ques()   


# # For North American video game sales, what’s the median?

# In[49]:


df['Na'].median()


# # Which company has sold the most 'Action' games?

# In[61]:


df=df[(df['Genre']=='Action')]

df


# In[66]:


df.groupby(['Publisher'])['GB'].sum().sort_values(ascending=False)


# In[78]:




sns.catplot(x = 'Year',y='Global_Sales', kind = 'strip', data = df.head(5),aspect = 1)


# In[ ]:




