#!/usr/bin/env python
# coding: utf-8

# # Przykładowy rozdział

# In[1]:


import numpy as np              # numeric
import matplotlib.pyplot as plt # plotting


# Komórki trojakiego rodzaju

# ## Jakiś podrozdział

# Rozumie latex:
# 
# $w_0+w_1 x_1 + w_2 x_2 > 0$.

# In[2]:


def sq(x):
    return x*x  # square


# In[3]:


y=2
print(y, ' ', sq(y)) 


# In[4]:


# sigmoid 
def sig_T(s,T):
    return 1/(1+np.exp(-s/T))


# In[5]:


plt.figure(figsize=(2.8,2.3),dpi=120)

s = np.linspace(-10, 10, 100)

fs = [sig_T(z,.5) for z in s]
plt.plot(s, fs)
fs = [sig_T(z,2) for z in s]
plt.plot(s, fs)

plt.title("Sigmoid with temperature", fontsize=11)
plt.legend(('T=0.5','T=2','step'),fontsize=9)

plt.xlabel('signal',fontsize=11)
plt.ylabel('response',fontsize=11)
plt.show()

