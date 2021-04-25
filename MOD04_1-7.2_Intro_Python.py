#!/usr/bin/env python
# coding: utf-8

# # 1-7.2 Intro Python
# ## `while()` loops & increments
# - while `True`  or forever loops
# - incrementing in loops
# - **Boolean operators in while loops**
# 
# 
# -----  
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - create forever loops using `while` and `break`
# - use incrementing variables in a while loop
# - **control while loops using Boolean operators**

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## `while` with Boolean comparison
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f540955e-543b-48f0-8201-3513b0beeed9/Unit1_Section7.2-while-boolean-comp.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f540955e-543b-48f0-8201-3513b0beeed9/Unit1_Section7.2-while-boolean-comp.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ## `while` with Boolean comparison operator
# ### `while x < 5:`
# with increment we used  **`break`** when count becomes greater than some number  
# 
# The same result can be achieved by using **`while x < 5:`**

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
#   
# 

# In[1]:


# review and run GREET COUNT
greet_count = 5

# loop while count is greater than 0
while greet_count > 0:
    print(greet_count, "!")
    greet_count -= 1
print("\nIGNITION!")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## `while` with comparison operator 
# ### Program: Animal Names
# - Use **`while`** to get the user input, animal_name, of 4 animals 
#   - use a counter, num_animals, in the while loop condition
#   - append the names to a string variable, all_animals
#   - User can exit early by typing "exit" (check if animal_name is "exit" and break)
# - when the loop finishes, print the names of all_animals
# 
# -bonus: print "no animals" if animal_name is empty after exiting the loop
# 
# **Tip:** Think about Sequence and variables that need to be initialized before the while loop

# In[16]:


# [ ] Create the Animal Names program, run tests

counter = 0
num_animals = 0
all_animals = ""

while num_animals < 4 :
             
    animal_name = input("give me an animal: (or exit) ").lower()
    
    if animal_name == "exit" :
        print("all animals : ",all_animals)
        break
        
    elif not animal_name.isalpha():
        print("no animasls")
        break
        
    else:
        num_animals += 1
        all_animals += animal_name + " "
else :
    print(all_animals)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## `while` Boolean string tests
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/26728191-873d-42ba-b6b5-48b396a8f42f/Unit1_Section7.2-while-boolean-string.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/26728191-873d-42ba-b6b5-48b396a8f42f/Unit1_Section7.2-while-boolean-string.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ## Using `while` with a Boolean String Tests
# A while loop can be controlled by Boolean strings such as `while name.isalpha() == False:`

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[17]:


# review and run example that loops until a valid first name format is entered
student_fname = ""
while student_fname.isalpha() == False:
    student_fname = input("enter student\'s first (Letters only, No spaces): ")
print("\n" + student_fname.title(),"has been entered as first name")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## Using `while` with a Boolean String
# ### Program: Long Number
# #### Create variables
# - **`int_num`** and get user input **string** of only digits  
# - **`long_num`** and initialize it as an empty string  
# 
# #### Create a while loop that runs as long as the input is all digits  
# 
# #### Inside the while loop   
# - add **`int_num`** to the end of **`long_num`**
# - get user input for **`int_num`** again (*inside while loop this time*)  
# 
# #### After the loop exits 
# - print the value of **`long_num`**   

# In[38]:


# [ ] Create the program, run tests

long_num = ""
int_num = ""

int_num = input("only digits: ")

while int_num.isdigit() == True :
    int_num = input("only digits: ")
    long_num += int_num + " "
       
else : 
    print(long_num)


# t##### &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ## Fix the Errors
# This loop never runs
# ### This is a logic error - there is no ErrorMessage, but the code *doesn't work*

# In[47]:


# [ ] review the code, run, fix the Logic error
count = 1

# loop 5 times
while count <= 5:
    print(count, "x", count, "=", count*count)
    count +=1
    
else :
    print(count)
    


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
