#!/usr/bin/env python
# coding: utf-8

# # 1-6.2 Intro Python
# ## Nested Conditionals
# - nested conditionals  
# - **print formatting with the (\) escape sequence** 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - create nested conditional logic in code  
# - **print format print using escape sequence (\)**

# 
# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## formatting with escape sequences
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b64e53fd-eb3b-4383-8b5f-4da51fc881c5/Unit1_Section6.2-Escape-Sequences.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b64e53fd-eb3b-4383-8b5f-4da51fc881c5/Unit1_Section6.2-Escape-Sequences.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Escape Sequences
# - escape sequences all start with a backslash (**`\`**) 
# - escape sequences can be used to display characters in python reserved for formatting
#   - **`\\`** &nbsp; Backslash (**`\`**)  
#   - **`\'`** &nbsp; Single quote (**'**)  
#   - **`\"`** &nbsp; Double quote (**"**)  
# 
# 
# - escape sequences are part of special formatting charcters\n    Linefeed 
#   - **`\t`** &nbsp; Tab
#   - **`\n`** &nbsp; return or newline
# 
# We use escape sequences in strings - usually with `print()` statements 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>  

# In[2]:


# review and run example using \n (new line)
print('Hello World!\nI am formatting print ')


# In[3]:


# review and run code using \t (tab)
student_age = 17
student_name = "Hiroto Yamaguchi"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t' + str(student_age))


# In[5]:


# review and run code 
# using \" and \' (escaped quotes)
print("\"quotes in quotes\"")
print("I\'ve said \"save your notebook,\" so let\'s do it!")

# using  \\ (escaped backslash)
print("for a newline use \\n")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>  
# Format using backslash (**`\`**) escape sequences

# In[6]:


# [ ] print "\\\WARNING!///"

print("\\\\\\WARNING!///")


# In[8]:


# [ ] print output that is exactly (with quotes): "What's that?" isn't a specific question.

print("\"What's that?\" isn't a specific question.")


# In[9]:


# [ ] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six

print("One\tTwo\tThree\nFour\tFive\tSix")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## Program: `pre_word()` Function
# Function has a single string parameter that it checks s is a single word starting with "pre"
# - Check if word starts with "pre"
# - Check if word .isalpha() 
# - if all checks pass: return **`True`**
# - if any checks fail: return **`False`**
# - **Test** 
#   - get input using the directions: *enter a word that starts with "pre": *
#   - call pre_word() with the input string
#   - test **if** return value is **`False`** and print message explaining not a "pre" word 
#   - **else** print message explaining is a valid "pre" word

# In[21]:


# [ ] create and test pre_word()

def pre_word(word) :
    
    if word.isalpha() and word.startswith("pre") :
        return True
    
    else :
        return False
    
test = input("let me check: ").lower()
print(pre_word(test))


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 5</B></font>
# ## Fix the Errors

# In[22]:


# [ ] review, run, fix
print("Hello\nWorld!")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
