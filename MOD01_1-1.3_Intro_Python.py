#!/usr/bin/env python
# coding: utf-8

# # 1-1.3 Intro Python
# ##  Getting started with Python in Jupyter Notebooks
# - Python 3 in Jupyter notebooks
# - `print()`
# - comments  
# - **data types basics**
# - **variables**  
# - addition with Strings and Integers
# - Errors  
# - character art  
# 
# -----
# 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - use Python 3 in Jupyter notebooks
# - write working code using `print()` and `#` comments  
# - **write working code using `type()` and variables**
# - combine Strings using string addition (+)
# - add numbers in code (+)
# - troubleshoot errors
# - create character art

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Using the Python `type()` function
# **`type()`** returns the data type of python objects
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b8fbc662-a42e-4a4a-8cfc-564cb240576e/Unit1_Section1.3-Type.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b8fbc662-a42e-4a4a-8cfc-564cb240576e/Unit1_Section1.3-Type.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### `str`, `int`, `float`  
# #### What does using `type()` reveal?
# - **`str`**: when **type()** returns **str** that means it has evaluated a **string** characters (numbers, letters, punctuation...) in quotes 
# - **`int`**: when **type()** returns **int** that means it has evaluated an **Integer** (+/- whole numbers) 
# - **`float`**: when **type()** returns **`float`** that means it has evaluated decimal numbers (e.g. 3.33, 0.01, 9.9999 and 3.0), ...more later in the course

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# - Read and run the code for each sample

# In[1]:


# [ ] Read and run the code
type("Hello World!")


# In[1]:


type(501)


# In[2]:


type(8.33333)


# In[2]:


student_name = "Colette Browning"
type(student_name)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1: multi-part</B></font> 
# ## Using `type()`
# - Complete the "identify data types" tasks by assigning  values to the variable&nbsp; **`bucket`** and using **`type()`** 

# In[3]:


# [ ] show the type after assigning bucket = a whole number value such as 16 
bucket = 14
type(bucket)


# In[4]:


# [ ] show  the type after assigning bucket = a word in "double quotes"
bucket = "mark"
type(bucket)


# In[5]:


# [ ] display the type of 'single quoting' (use single quotes) 
a = 'na'
type(a)


# In[6]:


# [ ] display the type of "double quoting" (use double quotes)
a = "j"
type(a)


# In[8]:


# [ ] display the type of "12" (use quotes)
a = "12"
type(a)


# In[9]:


# [ ] display the type of 12 (no quotes)

a = 12
type(a)


# In[11]:


# [ ] display the type of -12 (no quotes)
a = -12
type(a)


# In[12]:


# [ ] display the type of 12.0 (no quotes)
a = 12.0
type(a)


# In[7]:


# [ ] display the type of 1.55
a = 1.55
type(a)


# In[ ]:


# [ ] find the type of the type(3) statement (no quotes) - just for fun


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
