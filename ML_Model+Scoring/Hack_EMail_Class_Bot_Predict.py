#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import string
import nltk
import os

from nltk.corpus import stopwords
from sklearn.externals import joblib


# In[2]:


def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


# In[3]:


fields = ['Text Message']
messages = pd.read_csv('To_predict/Emails.csv', skipinitialspace=True, usecols=fields)


# In[4]:


pd_in = pd.DataFrame(messages['Text Message'])


# In[5]:


pd_in


# In[6]:


# Load the model from the file 
pipeline_from_joblib = joblib.load('EMail_Class_Model.pkl')  


# In[7]:


# Use the loaded model to make predictions 
output = pipeline_from_joblib.predict(messages['Text Message']) 
output
#for i in output:
#    print (i)


# In[8]:


pd_out = pd.DataFrame(data=output)


# In[9]:


pd_in,pd_out


# In[10]:


cons_output = pd.concat([pd_in,pd_out],axis=1)


# In[11]:


cons_output


# In[12]:


#cons_output.columns = cons_output.iloc[0]
#cons_output = cons_output[1:]


# In[13]:


cons_output.to_csv('To_predict/Cons_Pred_Output.csv', index= True, header= False)


# In[ ]:


os.system("python C:/Python37/Project/Project/app/services/ImporttoMySQL.py")


# In[ ]:




