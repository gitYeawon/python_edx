#!/usr/bin/env python
# coding: utf-8

# # 2-1.3 Intro Python
# ## Sequence: String
# - Accessing String Character with index
# - Accessing sub-strings with index slicing
# - **Iterating through Characters of a String**
# - More String Methods
# 
# ----- 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - Work with String Characters
# - Slice strings into substrings
# - **Iterate through String Characters**
# - Use String Methods

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Iterate a String: 1 character at a time
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/edd3631b-bceb-45a1-82bb-addf532aba4d/Unit2_Section1.3a-Iterate_a_String.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/edd3631b-bceb-45a1-82bb-addf532aba4d/Unit2_Section1.3a-Iterate_a_String.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `for letter in word:`
# Python provides powerful sequence iteration features.  Below, **`for letter in word:`** loops through each letter in *word*.
# 
# ```python
# word = "cello"
# 
# for letter in word:
#     print(letter)
# ```  
# 
# The variable **`letter`** is an arbitrary variable name .  Any valid variable name can be used.
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[1]:


# [ ] review and run example
word = "cello"

for letter in word:
    print(letter)


# In[2]:


# [ ] review and run example
# note: the variable 'letter' changed to 'item'
word = "trumpet"

for item in word:
    print(item)


# In[3]:


# [ ] review and run example
# note: variable is now 'xyz' 
# using 'xyz', 'item' or 'letter' are all the same result
word = "piano"

for xyz in word:
    print(xyz)


# In[7]:


# [ ] review and run example
# creates a new string (new_name) adding a letter (ltr) each loop
# Q?: how many times will the loop run?
student_name = "Skye"
new_name = ""

for ltr in student_name:
    if ltr.lower() == "y":
        new_name += ltr.upper()
        #print(ltr)
    else:
        new_name += ltr
        print(ltr)
print(student_name,"to",new_name)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## iterate a String
# ### one character at a time

# In[8]:


# [ ] Get user input for first_name
# [ ] iterate through letters in first_name 
#    - print each letter on a new line


first_name = input()

for ho in first_name:
    print(ho)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Program: capitalize-io
# - get user input for first_name
# - create an empty string variable: new_name
# - iterate through letters in first_name 
#   -  add each letter in new_name
#   - capitalize if letter is an "i" or "o" *(hint: if, elif, else)
# - print new_name

# In[9]:


# [ ] Create capitalize-io

first_name = input()
new_name = ""

for letters in first_name :
    
    if letters == "i":
        new_name += letters.upper()
    elif letters == "o":
        new_name += letters.upper()
    else :
        new_name += letters

        
print(first_name , "to",new_name)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Iterate sub-strings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/257ed101-c530-406a-ba20-6d437d88e529/Unit2_Section1.3b-Iterate-Substrings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/257ed101-c530-406a-ba20-6d437d88e529/Unit2_Section1.3b-Iterate-Substrings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# Combine String slicing and iteration
# 
# ```python
# student_name = "Skye"
# 
# for letter in student_name[:3]:
#     print(letter)
# ```  
# 
# Iterate backwards using: **`student_name[::-1]`**

# ### &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[10]:


# [ ] review and run example
student_name = "Skye"

for letter in student_name[:3]:
    print(letter)


# In[11]:


# Iterate BACKWARDS
# [ ] review and run example
student_name = "Skye"

# start at "y" (student_name[2]), iterate backwards
for letter in student_name[2::-1]:
    print(letter)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ###  String slicing and iteration

# In[25]:


# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
other_word = ""

for other_word in long_word[::-1]:
    print(other_word)


# In[12]:


# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"

fav_color = input("tell me your favorite color")

print(fav_color[::-1] + fav_color)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
