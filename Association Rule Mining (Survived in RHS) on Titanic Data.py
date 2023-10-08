#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install apyori')


# In[5]:


import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import ARutils
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().system('pip install plotly==5.10.0')
import plotly.express as px

#reading the dataset
titanic_preprocessed=pd.read_csv('titanic_preprocessed.csv')
titanic_preprocessed

#converting the dataset to list
titanic=ARutils.data_prepare(titanic_preprocessed)
titanic

#making rules
Rules=list(apriori(titanic,min_support=0.02,min_confidence=0.2))

#Extracting the association rules
associationRules=ARutils.extract(Rules)

#writing the association rules to a dataframe
rules_df=pd.DataFrame(associationRules,columns=['LHS','RHS','Support','Confidence','Lift'])
survived_rules_df=rules_df[rules_df['RHS'].apply(lambda x:'Survived' in x)]
survived_rules_df

#plotting the survived_rules_df support-confidence fig
fig=px.scatter(survived_rules_df,x='Support',y='Confidence',color='Lift',hover_data=['LHS','RHS'],color_continuous_scale='agsunset')
fig.show()


# In[ ]:




