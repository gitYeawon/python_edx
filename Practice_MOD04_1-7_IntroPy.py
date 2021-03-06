#!/usr/bin/env python
# coding: utf-8

# # 1-7.2 Intro Python Practice
# ## `while()` loops & increments
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - create forever loops using `while` and `break`
# - use incrementing variables in a while loop
# - control while loops using Boolean operators

# In[26]:


# [ ] use a "forever" while loop to get user input of integers to add to sum, 
# until a non-digit is entered, then break the loop and print sum

sum = 0 

while True:
    addition = input("Enter only digits: ")
    
    if addition.isdigit() :
        sum += int(addition)
        
    else : 
        print(sum)
        break


# 6###### 4#### [ ] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# # rainbow = "red orange yellow green blue indigo violet"
# 
# 

# In[29]:


# [ ] Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)

while True :
    
    title = input("book title: ")

    if not title.istitle():
        ("please write titles")
        break
    else :
        print(title)


# In[35]:


# [ ] create a math quiz question and ask for the solution until the input is correct

answer = "5"

while True:
    
    q1 = input("What is 3 + 2 = ?: ")
    
    if q1 == answer :
        print("You are right !")
        break
        
    else :
        print("try again")
        
        


# #### Fix the Error

# In[39]:


# [ ] review the code, run, fix the error
tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
        # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("you win!")
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))

print("Game ended")
    


# ### create a function: quiz_item()  that asks a question and tests if input is correct  
# - quiz_item()has 2 parameter **strings**: question and solution  
# - shows question, gets answer input  
# - returns True if `answer == solution` or continues to ask question until correct answer is provided  
# - use a while loop
# 
# create 2 or more quiz questions that call quiz_item()  
# **Hint**: provide multiple choice or T/F answers

# In[ ]:


# Create quiz_item() and 2 or more quiz questions that call quiz_item()

def quiz_item(question, solution) :
    print(question)
    while True :

        answer = input("Answer: ").lower()
        
        if answer.lower() == solution :
            print("Good")
            return True
            break
        else :
            print("Try again ")
     
            
question = "Guess What I want to eat right now  "
solution = "waffle"
quiz_item(question,solution)
question = "which waffles?"
solution = "apple cinnamon"
quiz_item(question,solution)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; ?? 2017 Microsoft
