
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[3]:


arr = np.array([[1,2,np.nan],[np.nan,3,4]])


# In[4]:


arr


# In[5]:


dframe = DataFrame(arr,index=['A','B'],columns = ['one','two','Three'])


# In[6]:


dframe


# In[12]:


dframe.sum(axis=1)

dframe.min(
# In[13]:


dframe.min()


# In[14]:


dframe.idxmin()


# In[15]:


dfrafrom me


# In[16]:


dframe.cumsum()


# In[18]:


dframe.describe()


# In[20]:


from IPython.display import YouTubeVideo


# In[21]:


YouTubeVideo('8NgvxN9RJSg')


# In[24]:


from pandas import data
import datetime


# In[23]:


from pandas_datareader import data, wb

