#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


pd.options.display.max_rows = 200


# In[21]:


#in this step and next step i want to try different ways to show columns
artist = pd.read_csv("/Users/yangxi/Desktop/collecting data/collection-master/artist_data.csv", delimiter =',', encoding ='utf-8')
artist.head()


# In[22]:


df = pd.read_csv('/Users/yangxi/Desktop/collecting data/collection-master/artist_data.csv')


# In[23]:


df


# In[24]:


df = pd.read_csv('/Users/yangxi/Desktop/collecting data/collection-master/artwork_data.csv')


# In[25]:


df


# In[26]:


artist = artist.rename(columns={'id': 'artistId'})


# In[27]:


df = pd.merge(artist, artwork, on='artistId')


# In[28]:


df.head()


# In[29]:


df = df.drop(['url_x','thumbnailUrl','url_y'],axis = 1)


# In[30]:


df


# In[31]:


df.describe(include='all')


# In[32]:


#my first question is How many female and male artists respectively?


# In[33]:


df.groupby('gender').count()['id']


# In[34]:


#in this step i want to do some visualisations


# In[36]:


import seaborn as sns
sns.catplot(x="gender",kind="count",data=df)


# In[43]:


import plotly.express as px
labels = ['female','male']
values = [2727,65774]
fig=px.pie(df,values=values, names=labels, title="Percentage of Male and Female Artists")
fig.show()


# In[44]:


#i want to know the cities artists were born


# In[46]:


placeofbirth = df.placeOfBirth.value_counts()
placeofbirth.head()


# In[48]:


import plotly.express as px
labels = ['London','Castleford','Chertsey','Krefeld','Edinburgh']
values = [44218,623,620,579,573]
fig=px.pie(df,values=values, names=labels, title="Percentage of Places that Artists Were Born")
fig.show()

