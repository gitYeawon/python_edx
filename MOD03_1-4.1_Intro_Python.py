#!/usr/bin/env python
# coding: utf-8

# # 1-4.1 Intro Python
# ## Conditionals 
# - **`if`, `else`, `pass`**
#   - **Conditionals using Boolean String Methods**
#   - Comparison operators
#   - String comparisons
# 
# ----- 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - **control code flow with `if`... `else` conditional logic**  
#   - **using Boolean string methods (`.isupper(), .isalpha(), startswith()...`)**  
#   - using comparison (`>, <, >=, <=, ==, !=`)  
#   - using Strings in comparisons  

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Conditionals use `True` or `False`
#  - **`if`**
#  - **`else`**
#    - **`pass`**  
#    
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c53fdb30-b2b0-4183-9686-64b0e5b46dd2/Unit1_Section4.1-Conditionals.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c53fdb30-b2b0-4183-9686-64b0e5b46dd2/Unit1_Section4.1-Conditonals.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[1]:


if True:
    print("True means do something")
else:
    print("Not True means do something else")


# In[2]:


hot_tea = True

if hot_tea:
    print("enjoy some hot tea!")
else:
    print("enjoy some tea, and perhaps try hot tea next time.")


# In[3]:


someone_i_know = False
if someone_i_know:
    print("how have you been?")
else:
    # use pass if there is no need to execute code 
    pass


# In[4]:


# changed the value of someone_i_know
someone_i_know = True
if someone_i_know:
    print("how have you been?")
else:
    pass

x = 3
y = 3
calculation = x/y
print(calculation)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Conditionals
# ### Using Boolean with &nbsp; `if, else`
# 
# - **Give a weather report using `if, else`**

# In[5]:


sunny_today = True
# [ ] test if it is sunny_today and give proper responses using if and else
if sunny_today :
    print("enjoy")
else:
    pass


    


# In[6]:


sunny_today = False
# [ ] use code you created above and test sunny_today = False

if sunny_today :
    ("enjoy")
    
else :
    pass


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Conditionals: Boolean String test methods  with `if`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/caa56256-733a-4172-96f7-9ecfc12d49d0/Unit1_Section4.1-conditionals-bool.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/caa56256-733a-4172-96f7-9ecfc12d49d0/Unit1_Section4.1-conditonals-bool.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ```python
# if student_name.isalpha():
# ```  
# - **`.isalnum()`**
# - **`.istitle()`**
# - **`.isdigit()`**
# - **`.islower()`**
# - **`.startswith()`**
# 

# ### &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[7]:


# review code and run cell
favorite_book = input("Enter the title of a favorite book: ")

if favorite_book.istitle():
    print(favorite_book, "- nice capitalization in that title!")
else:
    print(favorite_book, "- consider capitalization throughout for book titles.")


# In[11]:


# review code and run cell
a_number = input("enter a positive integer number: ")

if a_number.isdigit():
    print(a_number, "is a positive integer")
else:
    print(a_number, "is not a positive integer")
    
# another if
if a_number.isalpha():
    print(a_number, "is more like a word")
else:
    pass


# In[13]:


# review code and run cell
vehicle_type = input('"enter a type of vehicle that starts with "P": ')

if vehicle_type.upper().startswith("P"):
    print(vehicle_type, 'starts with "P"')
else:
    print(vehicle_type, 'does not start with "P"')


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2: multi-part</B></font>
# 
# ## Evaluating Boolean Conditionals 
# ### create evaluations for `.islower()`
# - print output describing **if** each of the 2 strings is all lower or not
# 

# In[18]:


test_string_1 = "welcome"
test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings
if test_string_2.islower():
    print(test_string_2)
    
else :
    print(test_string_1)


# <font size="3" color="#B24C00"  face="verdana"> <B>Task 2 continued.. </B></font>
# ### create a functions  using `startswith('w')`
# - w_start_test() tests if starts with "w"  
# **function should have a parameter for `test_string` and print the test result**

# In[24]:


test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')
def w_strat_test() :
    if test_string_1.lower().startswith("w"):
        print(test_string_1)
    if test_string_3.startswith("w"):
        print(test_string_3)
    else:
        print(test_string_2)
# [ ] Test the 3 string variables provided by calling w_start_test()
w_strat_test()


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
