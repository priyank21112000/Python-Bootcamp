#!/usr/bin/env python
# coding: utf-8

# In[ ]: 2


#Modules are predefined piece of code
#package is collection of modules,programs


# In[1]:


get_ipython().system(' pip install excel-to-json')


# In[ ]:


#writing a module


# In[8]:


get_ipython().run_cell_magic('writefile', 'file1.py', 'def fun(x):\n    return [num for num in range(x) if num%2==0]\nlist1 = myfun(15)\nprint(list1)')


# In[9]:


get_ipython().system(' python file1.py')


# In[4]:


get_ipython().run_cell_magic('writefile', 'file2.py', 'import file1\nfile1.list1.append(98)\nprint(file1.list1)\nfile1.myfun(56)\nprint(file1.list1)')


# In[10]:


get_ipython().system(' python file2.py')


# In[12]:


import file1

file1.list1.append(180)
print(file1.list1)


# In[13]:


import math
print(dir(math))


# In[14]:


import math
print(dir(file1))


# In[15]:


import math

print(math.sin(45))
print(dir(math.sin))


# In[16]:


get_ipython().run_cell_magic('writefile', 'ab1.py', "\ndef hello():\n    print('I am directly getting executed')\ndef greet():\n    print('I am here indirectly getting executed')\n    \nif(__name__ == '__main__'):\n    hello()\nelse:\n    greet()")


# In[17]:


get_ipython().system(' python ab1.py')


# In[18]:


get_ipython().run_cell_magic('writefile', 'ab2.py', "\nimport ab1\nprint('we are in ab2')")


# In[19]:


get_ipython().system('python ab2.py')


# In[ ]:


#Decorators


# In[ ]:


#How to get all the local variable and global variable


# In[26]:


s = 'GLOBAL vARIABLE'

def check_for_locals():
    name = 'Priyank'
    print(locals())
    print(globals())


# In[27]:


check_for_locals()


# In[30]:


s = 'GLOBAL vARIABLE'

def check_for_locals():
    name = 'Priyank'
    print(locals())
    print(globals()['s'])


# In[31]:


check_for_locals()


# In[32]:


def hello(name='LetsUpgrade'):
    print('Hi',name)


# In[33]:


hello('Priyank')


# In[ ]:


#assigning a function to another variable just like how we do variable assignment


# In[34]:


hi = hello


# In[35]:


hi


# In[36]:


hello


# In[37]:


#function within a function


# In[38]:


def hola():
    print('we are inside hola function')
    
    def Priyank():
        print('I am Priyank')
    Priyank()
                          


# In[39]:


hola()


# In[40]:


#Passing function as arguement


# In[41]:


def hello():
    print('Hey this is hello')
    
def anotherHello(arg):
    print('We are inside hello')
    arg()


# In[42]:


anotherHello(hello)


# In[43]:


#Decorator
#which adds some extra functionality to your code

def some_function():
    
    def wrap_fun():
        print('I am the code which is at the top of your function')
        function_as_arg()
        print('i am the code which is at the bottom of your function')
    return wrap_fun


# In[44]:


def function_which_requires_code_adds():
    print('Hey I am a function')
    print('I want some other code to be added')


# In[45]:


function_which_requires_code_adds()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




