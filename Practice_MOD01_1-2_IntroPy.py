#!/usr/bin/env python
# coding: utf-8

# # 1-2 Intro Python Practice
# ## Strings: input, testing, formatting
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - gather, store and use string `input()`  
# - format `print()` output  
# - test string characteristics  
# - format string output  
# - search for a string in a string  

# ## input()
# getting input from users

# In[1]:


# [ ] get user input for a variable named remind_me
remind_me = input()

# [ ] print the value of the variable remind_me

print(remind_me)


# In[3]:


# use string addition to print "remember: " before the remind_me input string
print("remember: " + remind_me)


# ### Program: Meeting Details
# #### [ ] get user **input** for meeting subject and time
# `what is the meeting subject?: plan for graduation`  
# `what is the meeting time?: 3:00 PM on Monday`  
# 
# #### [ ] print **output** with descriptive labels  
# `Meeting Subject: plan for graduation`  
# `Meeting Time:    3:00 PM on Monday`

# In[4]:


# [ ] get user input for 2 variables: meeting_subject and meeting_time
meeting_subject = input()
meeting_time = input()

# [ ] use string addition to print meeting subject and time with labels
print("Meeting Subject: " + meeting_subject)
print("Meeting Time: " + meeting_time)



# ## print() formatting 
# ### combining multiple strings separated by commas in the print() function

# In[5]:


# [ ] print the combined strings "Wednesday is" and "in the middle of the week" 

print("Wednesday is" , "in the middle of the week")


# In[6]:


# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remeber to ", remind_me)


# In[10]:


# [ ] Combine 3 variables from above with multiple strings
combine = remind_me + meeting_subject + meeting_time
print(combine)


# ### print() quotation marks

# In[11]:


# [ ] print a string sentence that will display an Apostrophe (')

print("'Hey you'")


# In[12]:


# [ ] print a string sentence that will display a quote(") or quotes

print('"What?"')


# ## Boolean string tests

# ### Vehicle tests  
# #### get user input for a variable named vehicle  
# print the following tests results  
# - check True or False if vehicle is All alphabetical characters using .isalpha()  
# - check True or False if vehicle is only All alphabetical & numeric characters  
# - check True or False if vehicle is Capitalized (first letter only)  
# - check True or False if vehicle is All lowercase  
# - **bonus** print description for each test (e.g.- `"All Alpha: True"`)

# In[31]:


# [ ] complete vehicle tests 

a = "vehicle"
a.isalpha()
a.isalnum()
a.istitle()
a.islower()
a.isupper()





# In[26]:


# [ ] print True or False if color starts with "b" 
a.startswith("b")


# In[ ]:





# ## Sting formatting

# In[27]:


# [ ] print the string variable capital_this Capitalizing only the first letter
capitalize_this = "the TIME is Noon."

capitalize_this.title()


# In[32]:


# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"

swap_this.swapcase()


# In[33]:


# print the string variable whisper_this in all lowercase
whisper_this = "Can you hear me?"

whisper_this.lower()


# In[34]:


# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"

yell_this.upper()


# In[40]:


#format input using .upper(), .lower(), .swapcase, .capitalize()
format_input = input('enter a string to reformat: ')

#format_input.upper()
#format_input.lower()
#format_input.swapcase()
format_input.capitalize()


# ### input() formatting

# In[41]:


# [ ] get user input for a variable named color
# [ ] modify color to be all lowercase and print

user_input = input("Color :").lower()
print(user_input)


# In[42]:


# [ ] get user input using variable remind_me and format to all **lowercase** and print
# [ ] test using input with mixed upper and lower cases
remind_me = input().lower()
print(remind_me)


# In[44]:


# [] get user input for the variable yell_this and format as a "YELL" to ALL CAPS

yell_this = input().upper()
print(yell_this)


# In[ ]:





# ## "in" keyword
# ### boolean: short_str in long_str

# In[48]:


# [ ] get user input for the name of some animals in the variable animals_input
animnals_input = input("some animals: ").lower()

# [ ] print true or false if 'cat' is in the string variable animals_input
print('cat' in animnals_input)


# In[54]:


# [ ] get user input for color
user_color = input("Color: ").lower()

# [ ] print True or False for starts with "b"
print(user_color.startswith("b"))

# [ ] print color variable value exactly as input 
#     test with input: "Blue", "BLUE", "bLUE"




# ## Program: guess what I'm reading
# ### short_str in long_str
# 
# 1. **[ ]** get user **`input`** for a single word describing something that can be read 
#  save in a variable called **can_read**  
#  e.g. - "website", "newspaper", "blog", "textbook"  
#  &nbsp;  
# 2. **[ ]** get user **`input`** for 3 things can be read  
#  save in a variable called **can_read_things**  
# &nbsp;  
# 
# 3. **[ ]** print **`true`** if the **can_read** string is found  
#  **in** the **can_read_things** string variable
#   
# *example of program input and output*  
# [![01 02 practice Allergy-input](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/guess_reading.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij7A_G6RtDlWZeYA3ZA)
# 

# In[57]:


# project: "guess what I'm reading"

# 1[ ] get 1 word input for can_read variable
can_read = input("a single word describing something that can be read: ").lower()

# 2[ ] get 3 things input for can_read_things variable
can_read_things = input("3 things can be read: ").lower()

# 3[ ] print True if can_read is in can_read_things
print(can_read in can_read_things)

# [] challenge: format the output to read "item found = True" (or false)
# hint: look print formatting exercises
print("item found = " ,can_read in can_read_things)


# ## Program: Allergy Check
# 
# 1. **[ ]** get user **`input`** for categories of food eaten in the last 24 hours  
#  save in a variable called **input_test**  
#  *example input*
#  [![01 02 practice Allergy-input](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_input.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65qzFD5CGvv95-ijg)
# &nbsp;  
# 2. **[ ]** print **`True`** if "dairy" is in the **input_test** string  
# **[ ]** Test the code so far  
# &nbsp;
# 3. **[ ]** modify the print statement to output similar to below  
# *example output*
# [![01 02 Allergy output](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_output.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65rET-wmlpCdMX7CQ)  
# Test the code so far trying input including the string "dairy" and without  
# &nbsp;  
# 
# 4. **[ ]** repeat the process checking the input for "nuts", **challenge** add "Seafood" and "chocolate"  
# **[ ]** Test your code  
# &nbsp;  
#   
# 5. **[ ] challenge:** make your code work for input regardless of case, e.g. - print **`True`** for "Nuts", "NuTs", "NUTS" or "nuts"  
# 

# In[ ]:


# Allergy check 

# 1[ ] get input for test
greeting = "hello"
input_test = input("enter food categories eaten in last 24 hrs: ").lower()

# 2/3[ ] print True if "dairy" is in the input or False if not
first = 'dairy' in input_test
print('It is', first, 'that "',input_test,'"contains "dairy"')
# 4[ ] Check if "nuts" are in the input
second = 'nuts' in input_test
print('It is', second, 'that "',input_test,'"contains "nuts"')
# 4+[ ] Challenge: Check if "seafood" is in the input
third = 'seafood' in input_test
print('It is', third, 'that "',input_test,'"contains "seafood"')
# 4+[ ] Challenge: Check if "chocolate" is in the input
forth = 'chocolate' in input_test
print('It is', forth, 'that "',input_test,'"contains "chocolate"')

input_test2 = input("enter food ").lower()

first2 = "nut" in input_test
print("It is ", first2, "that ''",input_test2, "'contains 'nut'")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
