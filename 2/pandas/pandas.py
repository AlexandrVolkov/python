#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


a = {'author_id': [1,2,3], 'author_name': ['Тургенев', 'Чехов', 'Островский']}
authors  = pd.DataFrame(data=a)


# In[6]:


authors 


# In[7]:


b = {'author_id':[1, 1, 1, 2, 2, 3, 3], 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],'price':[450, 300, 350, 500, 450, 370, 290]}
book = pd.DataFrame(data=b)


# In[9]:


book


# In[11]:


authors_price = authors.merge(book, on='author_id', how='inner')


# In[12]:


authors_price


# In[14]:


top5 = authors_price.nlargest(5,'price')


# In[15]:


top5


# In[24]:


authors_stat = authors_price.groupby('author_name').agg(min_price = ('price',min), max_price = ('price', max), mean_price = ('price', 'mean'))


# In[25]:


authors_stat


# In[ ]:




