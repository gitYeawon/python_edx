#!/usr/bin/env python
# coding: utf-8

# # 2-1.2 Intro Python
# ## Sequence: String
# - Accessing String Character with index
# - **Accessing sub-strings with index slicing**
# - Iterating through Characters of a String
# - More String Methods
# 
# ----- 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - Work with String Characters
# - **Slice strings into substrings**
# - Iterate through String Characters
# - Use String Methods

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Accessing sub-strings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/251ad8c1-588b-47de-8638-a5bcd0f29800/Unit2_Section1.2a-Index_Slicing-Substrings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/251ad8c1-588b-47de-8638-a5bcd0f29800/Unit2_Section1.2a-Index_Slicing-Substrings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [start:stop]
# String slicing returns a string section by addressing the start and stop indexes
# 
# ```python
# # assign string to student_name
# student_name = "Colette"
# # addressing the 3rd, 4th and 5th characters
# student_name[2:5]
# ```
# The slice starts at index 2 and ends at index 5 (but does not include index 5)

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[1]:


# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters using a slice
print("slice student_name[2:5]:",student_name[2:5])


# In[2]:


# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters individually
print("index 2, 3 & 4 of student_name:", student_name[2] + student_name[3] + student_name[4])


# In[3]:


# [ ] review and run example
long_word = 'Acknowledgement'
print(long_word[2:11])
print(long_word[2:11], "is the 3rd char through the 11th char")
print(long_word[2:11], "is the index 2, \"" + long_word[2] + "\",", "through index 10, \"" + long_word[10] + "\"")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## slice a string
# ### start & stop index

# In[12]:


# [ ] slice long_word to print "act" and to print "tic"
long_word = "characteristics"

print(long_word[4:7], long_word[-4:-1])


# In[13]:


# [ ] slice long_word to print "sequence"
long_word = "Consequences"

print(long_word[3:-1])


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Accessing beginning of sub-strings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/368b352f-6061-488c-80a4-d75e455f4416/Unit2_Section1.2b-Index_Slicing_Beginnings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/368b352f-6061-488c-80a4-d75e455f4416/Unit2_Section1.2b-Index_Slicing_Beginnings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [:stop]
# String slicing returns a string section from index 0 by addressing only the stop index
# 
# ```python
# student_name = "Colette"
# # addressing the 1st, 2nd & 3rd characters
# student_name[:3]
# ```
# **default start for a slice is index 0**

# ### &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[14]:


# [ ] review and run example
student_name = "Colette"
# addressing the 1st, 2nd & 3rd characters
print(student_name[:3])


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 

# In[15]:


# [ ] print the first half of the long_word
long_word = "Consequences"

print(long_word[:7])


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Accessing ending of sub-strings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29beb75a-aee7-43df-9569-e9ad22cffac4/Unit2_Section1.2c-Index_Slicing_Endings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29beb75a-aee7-43df-9569-e9ad22cffac4/Unit2_Section1.2c-Index_Slicing_Endings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [start:]
# String slicing returns a string section including by addressing only the start index
# 
# ```python
# student_name = "Colette"
# # addressing the 4th, 5th and 6th characters
# student_name[3:]
# ```
# **default end index returns up to and including the last string character**

# ### &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[16]:


# [ ] review and run example
student_name = "Colette"
#  4th, 5th, 6th and 7th characters
student_name[3:]


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 

# In[17]:


# [ ] print the second half of the long_word
long_word = "Consequences"

print(long_word[6:])


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## accessing sub-strings by step size
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/62c65917-4979-4d26-9a05-09e1ed02cc51/Unit2_Section1.2d-Index_Slicing-Step_Sizes.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/62c65917-4979-4d26-9a05-09e1ed02cc51/Unit2_Section1.2d-Index_Slicing-Step_Sizes.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [:], [::2]
# - **[:]** returns the entire string
# - **[::2]** returns the first char and then steps to every other char in the string
# - **[1::3]** returns the second char and then steps to every third char in the string  
# 
# the number **2**, in the print statement below, represents the **step** 
# 
# ```python
# print(long_word[::2])
# ```

# ### &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[18]:


# [ ] review and run example
student_name = "Colette"
# return all
print(student_name[:])


# In[19]:


# [ ] review and run example
student_name = "Colette"
# return every other
print(student_name[::2])


# In[4]:


# [ ] review and run example
student_name = "Colette"
# return every third, starting at 2nd character
print(student_name[1::3])


# In[21]:


# [ ] review and run example
long_word = "Consequences"
# starting at 2nd char (index 1) to 9th character, return every other character
print(long_word[1:9:2])


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 

# In[26]:


# [ ] print the 1st and every 3rd letter of long_word
long_word = "Acknowledgement"

print(long_word[::2])


# In[32]:


# [ ] print every other character of long_word starting at the 3rd character
long_word = "Acknowledgement"
print(long_word[2::3])


# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Accessing sub-strings  continued  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2e59f526-fadb-434e-822e-afe3732f75df/Unit2_Section1.2e-Index_Slicing-Reverse.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2e59f526-fadb-434e-822e-afe3732f75df/Unit2_Section1.2e-Index_Slicing-Reverse.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### stepping backwards 
# 
# ```python
# print(long_word[::-1])
# ```  
# 
# use **[::-1]** to reverse a string  

# ### &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[29]:


# [ ] review and run example of stepping backwards using [::-1]
long_word = "characteristics"
# make the step increment -1 to step backwards
print(long_word[::-1])


# In[30]:


# [ ] review and run example of stepping backwards using [6::-1]
long_word = "characteristics"
# start at the 7th letter backwards to start
print(long_word[6::-1])


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 5</B></font>  
# use slicing

# In[33]:


# [ ] reverse long_word
long_word = "stressed"

print(long_word[::-1])


# In[36]:


# [ ] print the first 5 letters of long_word in reverse
long_word = "characteristics"

print(long_word[4::-1])


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 6</B></font>  
# use slicing

# In[63]:


# [ ] print the first 4 letters of long_word
# [ ] print the first 4 letters of long_word in reverse
# [ ] print the last 4 letters of long_word in reverse
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
long_word = "timeline"

print(long_word[:4])
print(long_word[3::-1])
print(long_word[3:-1])  #7:3:-1
print(long_word[6:2:-1])




# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
