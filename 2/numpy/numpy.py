#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np


# In[9]:


a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]])


# In[10]:


a.shape


# In[15]:


mean_a = np.mean(a,axis = 0)


# In[16]:


mean_a


# In[24]:


a_centered = np.subtract(a, mean_a)


# In[25]:


a_centered


# In[26]:


a_centered_sp = np.dot(a_centered[:,0],a_centered[:,1])


# In[27]:


a_centered_sp


# In[28]:


a_centered_sp /= 4


# In[29]:


a_centered_sp


# In[ ]:




