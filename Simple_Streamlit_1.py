#!/usr/bin/env python
# coding: utf-8

# ## 1. Import Libraries:

# In[1]:


import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd


# ## 2. Create Sidebar:

# In[2]:


with st.sidebar:
    selected = option_menu('Calculation App',
                           ['Addition',
                            'Subtraction'],
                           
                           icons = ['file-plus','file-minus' ],
                           
                           default_index = 0)


# ## 3. Addition Page:

# In[ ]:


if (selected == 'Addition'):
    
    # Page title:
    st.title('Addition')
    
    # Getting input data from the user :
    col1, col2 = st.columns(2)
    
    with col1:
        first = st.number_input('First Number')
    with col2:
        second = st.number_input('Second Number')

    
    # Prediction Value:
    Value = ''
    
    # Prediction Button:
    if st.button('Calculate'):
        calculation = first + second

    st.success(calculation)

