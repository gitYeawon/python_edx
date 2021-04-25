#!/usr/bin/env python
# coding: utf-8

# # 1-5.2 Python Intro  
# ## conditionals, type, and mathematics extended
# - conditionals: `elif`  
# - casting   
# - **basic math operators**  
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - code more than two choices using `elif`  
# - gather numeric input using type casting   
# - **perform subtraction, multiplication and division operations in code** 
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Math basic operators
# ### `+` addition
# ### `-` subtraction
# ### `*` multiplication
# ### `/` division  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5bc97f7e-3015-4178-ac20-371a5302def1/Unit1_Section5.2-Math-operators.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5bc97f7e-3015-4178-ac20-371a5302def1/Unit1_Section5.2-Math-operators.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[1]:


# [ ] review and run example
print("3 + 5 =",3 + 5)
print("3 + 5 - 9 =", 3 + 5 - 9)
print("48/9 =", 48/9)
print("5*5 =", 5*5)
print("(14 - 8)*(19/4) =", (14 - 8)*(19/4))


# In[3]:


# [ ] review and run example - 'million_maker'
#def million_maker():
#    make_big = input("enter a non-decimal number you wish were bigger: ")
#    return int(make_big)*1000000


def milion_maker():
    make_big = input("I can make your money bigger: ")
    return int(make_big)*1000

print("Now you have", million_maker())


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## use math operators to solve the set of tasks below

# In[4]:


# [ ] print the result of subtracting 15 from 43

a = 15

print("43 - 15 =", 43 - 15)


# In[5]:


# [ ] print the result of multiplying 15 and 43

print("15 * 43 = ", 43*15)


# In[6]:


# [ ] print the result of dividing 156 by 12

print("156 / 12 =", 156/12)


# In[7]:


# [ ] print the result of dividing 21 by 0.5

print("21 / 0.5 = ", 21/0.5)


# In[8]:


# [ ] print the result of adding 111 plus 84 and then subtracting 45

print("111 + 84 - 45 = ", 111+84-45)


# In[10]:


# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4

print("(21 + 4) * 4 =", (21+4)*4)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## Program: Multiplying Calculator Function
# - define function **`multiply()`**, and within the function:
#   - gets user input() of 2 *strings* made of whole numbers
#   - cast the input to **`int()`**
#   - multiply the integers and **return** the equation with result as a **`str()`**
#     - **return** example 
#      ```python
#      9 * 13 = 117
#      ```

# #### [ ] create and test multiply() function
# 
# def multiply() :
#     a = int(input())
#     b = int(input())
#     
#     return (a+ '*'+ b + = + a*b)
# 
# multiply()

# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ## Project: Improved Multiplying Calculator Function
# ### putting together conditionals, input casting and math
# - #### update the multiply() function to multiply or divide 
#   - single parameter is **`operator`** with arguments of **`*`** or **`/`** operator
#   - default operator is "*" (multiply)
#   - **return** the result of multiplication or division
#   - if operator other than **`"*"`** or **`"/"`**  then **` return "Invalid Operator"`**

# In[35]:


# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)
def multifly(operator) :
    
    a = int(input())
    b = int(input())
    
    if operator == "*" :
        return a * b
    
    elif operator == "/" :
        return a / b
    
    else :
        return ("Invaild Operator")

print(multifly("/"))


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# ## Fix the Errors

# In[37]:


# Review, run, fix 
student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
