#!/usr/bin/env python
# coding: utf-8

# # 1-4.3 Intro Python
# ## Conditionals 
# - **`if`, `else`, `pass`**
#   - Conditionals using Boolean String Methods
#   - Comparison operators
#   - **String comparisons**
# 
# ----- 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - **control code flow with `if`... `else` conditional logic**  
#   - using Boolean string methods (`.isupper(), .isalpha(), startswith()...`)  
#   - using comparison (`>, <, >=, <=, ==, !=`)  
#   - **using Strings in comparisons**  

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## String Comparisons
# - ### Strings can be equal `==` or unequal `!=`
# - ### Strings can be greater than `>` or less than `<` 
# - ### alphabetically `"A"` is less than `"B"`
# - ### lower case `"a"` is greater than upper case `"A"`

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[1]:


# review and run code
"hello" < "Hello"


# In[2]:


# review and run code
"Aardvark" > "Zebra"


# In[3]:


# review and run code
'student' != 'Student'


# In[4]:


# review and run code
print("'student' >= 'Student' is", 'student' >= 'Student')
print("'student' != 'Student' is", 'student' != 'Student')


# In[5]:


# review and run code
"Hello " + "World!" == "Hello World!"


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## String Comparisons

# In[6]:


msg = "Hello"
# [ ] print the True/False results of testing if msg string equals "Hello" string
if msg == "Hello" :
    print(msg == "Hello")
else :
    print(msg)
    


# In[11]:


greeting = "Hello"
# [ ] get input for variable named msg, and ask user to 'Say "Hello"'
# [ ] print the results of testing if msg string equals greeting string

msg = input("say 'Hello'")
if greeting == msg :
    print("True")
else :
    print("Try Again")


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## Conditionals: String comparisons with `if`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d66365b5-03fa-4d0d-a455-5adba8b8fb1b/Unit1_Section4.3-string-compare-if.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d66365b5-03fa-4d0d-a455-5adba8b8fb1b/Unit1_Section4.3-string-compare-if.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[12]:


# [ ] review and run code
msg = "Save the notebook"

if msg.lower() == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")


# In[13]:


# [ ] review and run code
msg = "Save the notebook"
prediction = "save the notebook"

if msg.lower() == prediction.lower():
    print("message as expected")
else:
    print("message not as expected")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## Conditionals: comparison operators with if
# 

# In[15]:


# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"

answer = input('What is 8 + 13?: ')
if answer == "21" :
    print("Correct")
else :
    print("idiot")


# # &nbsp;  
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>  
# ## Program: True False Quiz Function
# Call the tf_quiz function with 2 arguments
# - T/F question string 
# - answer key string like "T"  
# 
# Return a string: "correct" or incorrect"
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/3805cc48-f5c9-4ec8-86ad-1e1db45788e4/Unit1_Section4.3-TF-quiz.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/3805cc48-f5c9-4ec8-86ad-1e1db45788e4/Unit1_Section4.3-TF-quiz.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Define and use `tf_quiz()` function  
# - **`tf_quiz()`** has **2 parameters** which are both string arguments  
#   - **`question`**: a string containg a T/F question like "Should save your notebook after edit?(T/F): "  
#   - **`correct_ans`**: a string indicating the *correct answer*, either **"T"** or **"F"** 
# - **`tf_quiz()`** returns a string:  "correct" or "incorrect"
# - Test tf_quiz(): **create a T/F question** (*or several!*) to **call tf_quiz()**  
# 

# In[ ]:


# [ ] Create the program, run tests
def tf_quiz(quesion, correct_ans) :
    #quesion = input(": ")
    input(quesion).lower()
    
    if input(quesion).lower() == correct_ans.lower() :
           return(print(question))
    else :
        return("incorrect")
        
    return a

#def my_qustion() :
#    return input()
    
q1 = tf_quiz("can you count 1 to 100?(T/F)","t")
print("Answer is ",q1)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
