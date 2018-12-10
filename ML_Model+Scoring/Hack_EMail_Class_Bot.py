#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import string
import nltk

from nltk.corpus import stopwords
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

#from sklearn.ensemble import RandomForestClassifier
#from sklearn.linear_model import LogisticRegression
#from sklearn.svm import LinearSVC
#from sklearn.svm import SVC


# In[3]:


fields = ['Text Message', 'Category']
messages = pd.read_csv('To_Train/Emails.csv', skipinitialspace=True, usecols=fields)


# In[4]:


#messages


# In[5]:


messages.describe()


# In[6]:


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


# In[7]:


msg_train, msg_test, label_train, label_test = train_test_split(messages['Text Message'], messages['Category'], test_size=0.2)

#print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))
msg_test#, label_test


# In[8]:


from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])
#NaiveBayes - BinominalNB(), MultiNominalNB(), GaussianNB()
#RandomForestClassifier() 
#LogisticRegression()
#LinearSVC()
#SVC()


# In[9]:


pipeline.fit(msg_train,label_train)


# In[10]:


predictions = pipeline.predict(msg_test)


# In[12]:


#print(classification_report(label_test,predictions))


# In[16]:


#print (label_test, predictions)


# In[18]:


#for i in predictions:
#    print (i)


# In[19]:


#print(label_test)


# In[13]:


# Save the model as a pickle in a file 
joblib.dump(pipeline, 'EMail_Class_Model.pkl') 


# In[14]:


# Load the model from the file 
pipeline_from_joblib = joblib.load('EMail_Class_Model.pkl')  


# In[16]:


# Use the loaded model to make predictions 
#pipeline_from_joblib.predict(msg_test) 
#for i in pipeline_from_joblib.predict(msg_test):
#    print (i)

