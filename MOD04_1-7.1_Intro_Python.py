#!/usr/bin/env python
# coding: utf-8

# # 1-7.1 Intro Python
# ## `while()` loops & increments
# - **while `True`  or forever loops**
# - **incrementing in loops**
# - Boolean operators in while loops
# 
# 
# -----  
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - **create forever loops using `while` and `break`**
# - **use incrementing variables in a while loop**
# - control while loops using Boolean operators

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## `while True:`
# ### Using the 'while True:' loop
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f43862cd-7cdc-45a3-adb1-a07dcbd9ae16/Unit1_Section7.1-while-forever.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f43862cd-7cdc-45a3-adb1-a07dcbd9ae16/Unit1_Section7.1-while-forever.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# **`while True:`** is known as the **forever loop** because it ...loops forever  
# 
# Using the **`while True:`** statement results in a loop that continues to run forever   
# ...or, until the loop is interrupted, such as with a **`break`** statement  
# 
# ## `break`
# ### in a `while` loop, causes code flow to exit the loop  
# a **conditional** can implement **`break`** to exit a **`while True`** loop  

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# ## `while True` loops forever unless a `break` statement is used  

# In[1]:


# Review and run code
# this example never loops because the break has no conditions
while True:
    print('write forever, unless there is a "break"')
    break


# In[2]:


# [ ] review the NUMBER GUESS code then run - Q. what cause the break statement to run?
number_guess = "0"
secret_number = "5"

while True:
    number_guess = input("guess the number 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess,"is correct!\n")
        break
    else:
        print(number_guess,"is incorrect\n")


# In[3]:


# [ ] review WHAT TO WEAR code then run testing different inputs
while True:
    weather = input("Enter weather (sunny, rainy, snowy, or quit): ") 
    print()

    if weather.lower() == "sunny":
        print("Wear a t-shirt and sunscreen")
        break
    elif weather.lower() == "rainy":
        print("Bring an umbrella and boots")
        break
    elif weather.lower() == "snowy":
        print("Wear a warm coat and hat")
        break
    elif weather.lower().startswith("q"):
        print('"quit" detected, exiting')
        break
    else:
        print("Sorry, not sure what to suggest for", weather +"\n")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## `while True` 
# ### [ ] Program: Get a name forever ...or until done
# - create variable, familar_name, and assign it an empty string (**`""`**)
# - use **`while True:`**
# - ask for user input for familar_name (common name friends/family use) 
# - keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
# - break loop and print a greeting using familar_name

# In[7]:


# [ ] create Get Name program

familar_name = ""

while True :
    
    familar_name = input("let me know any names: ")
    
    if familar_name.isalpha() :
        
        print("Hi !")
        break
        
    else : 
        
        print("Sorry do it again")
        


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## Incrementing a variable
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{%22src%22:%22http://jupyternootbookwams.streaming.mediaservices.windows.net/cc7925d2-0652-4659-93fb-f4cc8d09ac51/Unit1_Section7.1-increment.ism/manifest%22,%22type%22:%22application/vnd.ms-sstr+xml%22}],[{%22src%22:%22http://jupyternootbookwams.streaming.mediaservices.windows.net/cc7925d2-0652-4659-93fb-f4cc8d09ac51/Unit1_Section7.1-increment.vtt%22,%22srclang%22:%22en%22,%22kind%22:%22subtitles%22,%22label%22:%22english%22}])
# ## Incrementing
# ### `votes = votes + 1` &nbsp; &nbsp; or &nbsp;  `votes += 1`
# 
# ## Decrementing 
# ### `votes = votes - 1` &nbsp; &nbsp; or &nbsp; `votes -= 1`

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
#   
# 

# In[8]:


# [ ] review and run example
votes = 3
print(votes)

votes = votes + 1
print(votes)

votes += 2
print(votes)


# In[9]:


print(votes)

votes -= 1
print(votes)


# In[2]:


# [ ] review the SEAT COUNT code then run 

seat_count = 0
while True:
    print("seat count:",seat_count)
    seat_count = seat_count + 1

    if seat_count > 4:
        break


# In[11]:


# [ ] review the SEAT TYPE COUNT code then run entering: hard, soft, medium and exit

# initialize variables
seat_count = 0
soft_seats = 0
hard_seats = 0
num_seats = 4

# loops tallying seats using soft pads vs hard, until seats full or user "exits"
while True:
    seat_type = input('enter seat type of "hard","soft" or "exit" (to finish): ')
    
    if seat_type.lower().startswith("e"):
        print()
        break
    elif seat_type.lower() == "hard":
        hard_seats += 1
    elif seat_type.lower() == "soft":
        soft_seats += 1
    else:
        print("invalid entry: counted as hard")
        hard_seats += 1  
    seat_count += 1
    if seat_count >= num_seats:
        print("\nseats are full")
        break
        
print(seat_count,"Seats Total: ",hard_seats,"hard and",soft_seats,"soft" )


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## incrementing in a `while()` loop
# ### Program: Shirt Count
# - enter a sizes (S, M, L)
# - tally the count of each size
# - input "exit" when finished
# - report out the purchase of each shirt size  
# 

# In[15]:


# [ ] Create the Shirt Count program, run tests

s = 0
m = 0
l = 0
amount = 4

while True :
    
    user = input("Please select size: ")
    if user.lower().startswith("e") :
        print("Total size : ",amount,"S: ",s,"M: ",m,"L: ",l)
        break
        
    elif user.lower() == "s":
        s += 1
    elif user.lower() == "m":
        m += 1
    elif user.lower() == "l":
        l += 1
    
    elif user.isdigit() :
        print("please slect a size. ")


# ### CHALLENGE: Shirt Register (optional)  
# Update the **Shirt Count** program to calculate cost
# - use shirt cost (S = 6, M = 7, L = 8)
# - to calculate and report the subtotal cost for each size 
# - to calculate and report the total cost of all shirts

# In[55]:


# [ ] Create the Shirt Register program, run tests

s_cost = 6
m_cost = 7
l_cost = 8
total_cost = 0

s = 0
m = 0
l = 0
amount = 4

while True :
    
    user = input("Please select size: ")
    if user.lower().startswith("e") :
        print("Total size : ",amount,"S:",s,"M:",m,"L:",l,"\nTotal cost :$",(s*s_cost + m*m_cost + l*l_cost),"$",s*s_cost,"$",m*m_cost,"$",l*l_cost)
        break
        
    elif user.lower() == "s":
        s += 1
        
    elif user.lower() == "m":
        m += 1
      
    elif user.lower() == "l":
        l += 1
       
    elif user.isdigit() :
        print("please slect a size. ")
        
    


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
