#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json 
with open("reproduce-cases.ipynb", mode = "r", encoding= "utf-8") as f:
    fileoutput = json.loads(f.read())
fileoutput


# In[4]:


import json 
with open("reproduce-cases-original.ipynb", mode = "r", encoding= "utf-8") as f:
    fileoutput = json.loads(f.read())
fileoutput
#0feeacfb-4b64-416c-a232-3de290fac7e9 nb format


# In[7]:


import pandas as pd
df = pd.DataFrame({"A": ["a", "b", "c", "a"]})

df["B"] = df["A"].astype("category")


# In[13]:






raise Exception("Blah it runned")


# In[ ]:




