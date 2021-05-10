#!/usr/bin/env python
# coding: utf-8

# # 2-1.4 Intro Python
# ## Sequence: String
# - Accessing String Character with index
# - Accessing sub-strings with index slicing
# - Iterating through Characters of a String
# - **More String Methods**
# 
# ----- 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - Work with String Characters
# - Slice strings into substrings
# - Iterate through String Characters
# - **Use String ~~Tricks~~ Methods**
#   - `len()`
#   - `.count()`
#   - `.find()`

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## String Methods: return string information
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c300e46e-b3c7-4bbf-8117-e72b33998cd3/Unit2_Section1.4a-String_Methods-Length.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c300e46e-b3c7-4bbf-8117-e72b33998cd3/Unit2_Section1.4a-String_Methods-Length.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### len()  
# returns a strings length  
# ### .count()  
# returns number of times a character or sub-string occur  
# ### .find()   
# returns index of first character or sub-string match  
# returns **-1** if no match found  
# 
# ```python
# work_tip = "save your code"
# 
# # number of characters
# len(work_tip)
# 
# # letter "e" occurrences
# work_tip.count("e")
# 
# # find the index of the first space
# work_tip.find(" ")
# 
# # find the index of "u" searching a slice work_tip[3:6]
# work_tip.find("u",3,6)
# ```  
# These methods **return** information that we can use to sort or manipulate strings

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>  
# run each example cell in order

# In[1]:


# [ ] review and run example
work_tip = "save your code"

print("number of characters in string")
print(len(work_tip),"\n")

print('letter "e" occurrences')
print(work_tip.count("e"),"\n")

print("find the index of the first space")
print(work_tip.find(" "),"\n")

print('find the index of "u" searching a slice work_tip[3:9] -', work_tip[3:9])
print(work_tip.find("u",3,9),"\n")

print('find the index of "e" searching a slice work_tip[4:] -', work_tip[4:])
print(work_tip.find("e",4))


# ### len()  
# returns a strings length  

# In[2]:


# [ ] review and run example
work_tip = "good code is commented code"

print("The sentence: \"" + work_tip + "\" has character length = ", len(work_tip) )


# In[3]:


# [ ] review and run example
# find the middle index
work_tip = "good code is commented code"
mid_pt = int(len(work_tip)/2)

# print 1st half of sentence
print(work_tip[:mid_pt])

# print the 2nd half of sentence
print(work_tip[mid_pt:])


# ### .count()  
# returns number of times a character or sub-string occur   

# In[4]:


# [ ] review and run example
print(work_tip)
print("how many w's? ", work_tip.count("w"))
print("how many o's? ", work_tip.count("o"))
print("uses 'code', how many times? ", work_tip.count("code"))


# In[6]:


# [ ] review and run example 
print(work_tip[:mid_pt])
print("# o's in first half")
print(work_tip[:mid_pt].count("o"))

print()
print(work_tip[mid_pt:])
print("# o's in second half")
print(work_tip[mid_pt:].count("o"))


# ### .find(*string*) 
# returns index of first character or sub-string match  
# returns **-1** if no match found
# #### .find(*string*, *start index*, *end index*)
# same as above .find() but searches from optional start and to optional end index

# In[7]:


# [ ] review and run example 
work_tip = "good code has meaningful variable names"
print(work_tip)
# index where first instance of "code" starts
code_here = work_tip.find("code")
print(code_here, '= starting index for "code"')


# In[8]:


# [ ] review and run example 
# set start index = 13 and end index = 33
print('search for "meaning" in the sub-string:', work_tip[13:33],"\n")
meaning_here = work_tip.find("meaning",13,33)
print('"meaning" found in work_tip[13:33] sub-string search at index', meaning_here)


# In[9]:


# [ ] review and run example 
# if .find("o") has No Match, -1 is returned
print ("work_tip:" , work_tip)
location = work_tip.find("o")

# keeps looping until location = -1 (no "o" found)
while location >= 0:
    print("'o' at index =", location)
    # find("o", location + 1) looks for a "o" after index the first "o" was found
    location = work_tip.find("o", location + 1)
print("no more o's")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## `len()`

# In[18]:


# [ ] use len() to find the midpoint of the string 
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"

print(len(random_tip))
print(random_tip[:mid_pt])
print(random_tip[mid_pt:])


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## `.count()`

# In[2]:


# for letters: "e" and "a" in random_tip
# [ ] print letter counts 
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"

print(random_tip.count("e"))
print(random_tip.count("a"))


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ###  `.find()`

# In[3]:


# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"

long_word.find("t")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# ##  Program: print each word in a quote
# ```python
# start = 0
# space_index = quote.find(" ")
# while space_index != -1:
#     # code to print word (index slice start:space_index)
# ```  
# 
# Output should look like below: 
# ```
# they
# stumble
# who
# run
# fast
# ```  

# In[5]:


# [ ] Print each word in the quote on a new line  
quote = "they stumble who run fast"

start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start = space_index + 1
    #print(space_index)
    space_index = quote.find(" ", space_index+1)
    #print(space_index)
    
print(quote[start:])




# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
