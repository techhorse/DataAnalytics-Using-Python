
# coding: utf-8

# In[14]:


import pandas as pd
from pandas import Series, DataFrame


# In[15]:


titanic_df = pd.read_csv('train.csv')


# In[3]:


titanic_df.head()


# In[4]:


titanic_df.info()


# In[16]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[17]:


sns.factorplot('Sex',data=titanic_df,kind='count')


# In[18]:


sns.factorplot('Sex',data=titanic_df,hue='Pclass',kind='count')


# In[19]:


sns.factorplot('Pclass',data=titanic_df,hue='Sex',kind='count')


# In[20]:


def male_female_child(passenger):
    age , sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex
    


# In[21]:


titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)


# In[23]:


titanic_df[0:10]


# In[46]:


sns.factorplot('Pclass',data =titanic_df,hue='person',kind='count')


# In[47]:


sns.factorplot('Pclass',data=titanic_df,hue='person',kind='count')


# In[42]:


def male_female_child(passenger):
    # Take the Age and Sex
    age,sex = passenger
    # Compare the age, otherwise leave the sex
    if age < 16:
        return 'child'
    else:
        return sex
    

# We'll define a new column called 'person', remember to specify axis=1 for columns and not index
titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)


# In[43]:


titanic_df[0:10]


# In[45]:


sns.factorplot('Pclass',data=titanic_df,hue='person',kind='count')

