#!/usr/bin/env python
# coding: utf-8

# In[2]:


#map

def cube(x):
    return x * x * x


# In[3]:


cube(3)


# In[8]:


lst = [1,2,3,4,5,6]

map(cube,lst)


# In[9]:


list(map(cube,lst))


# In[10]:


#Filter

def even_odd(x):
    return x%2 == 0


# In[11]:


even_odd(2)


# In[12]:


filter(even_odd,lst)


# In[13]:


list(filter(even_odd,lst))


# In[ ]:





# In[19]:


#lambda it is used when a particular function is to be exectued
#only once in the whole piece of code
def cube(x):
    return x * x * x

cube1 =  lambda x : x * x * x


# In[15]:


cube1(3)


# In[16]:


list(map(lambda x : x * x * x,lst))


# In[17]:


list(filter(lambda x : x%2 == 0, lst))


# In[ ]:


#class


# In[20]:


#Class in Python # Declaring a class
#For eg. class is the list function and object is the variable declared

class Priyank():
    pass

p = Priyank()


# In[22]:


type(p)


# In[23]:


#cycle class
#init is constructor

class cycle():
    
    name = ''
    
    def __init__(self,name1):
        self.name = name1
    
    


# In[24]:


atlas = cycle('firefox')


# In[25]:


atlas.name


# In[27]:


mountainbike = cycle('madrock')


# In[28]:


mountainbike.name


# In[30]:


#Method in a class

class movies():
    movie_name = ''
    releaseDate = ' '
    actors = ''
    directors = ''
    producers = ''
    IMDB_rating = ''
    budget = ''
    
    def __init__ (self,movie_name,releaseDate,actors,directors,producers,IMDB_rating,budget):
        self.movie_name=movie_name
        self.releaseDate=releaseDate
        self.actors = actors
        self.directors=directors
        self.producers=producers
        self.IMDB_rating=IMDB_rating
        self.budget=budget
        
    def getBasicDetails(self):
        return {'movie_name':self.movie_name,'IMDB_rating':self.IMDB_rating}
    
    def getTheBudget(self):
        return self.budget
    
    def setActors(self,actors):
        self.actors = actors
        


# In[32]:


harryPotter = movies('harry potter 2','12-9-1999','radcliff','some director','you all', 8.9, '100 cr')


# In[33]:


harryPotter.getBasicDetails()


# In[34]:


harryPotter.directors


# In[35]:


harryPotter.setActors('Daniel and You Guys')


# In[36]:


harryPotter.actors


# In[ ]:





# In[38]:


#Inheritance 


# In[44]:


#base class
class dog:

    def __init__(self,name):
        self.name=name
        print(self.name +'Dog got created')
    def talk(self):
        return self.name +'Says bow bow'

#Derived class1
    
class Doberman(dog):
    def __init__(self):
        Dog.__init__(self,'doberman')
        print('doberman got created')
        
    def drink(self):
        print('doberman drinks milk')
    def height(self):
        print('minmum height is 1 meter')

#Derived class2        
        
class pug(dog):
    def __init__(self):
        dog.__init__(self,'pug')
        print('pug got created')
        
    def drink(self):
        print('pug drinks water')


# In[45]:


sally = pug()


# In[47]:


sally.talk()


# In[48]:


sally.drink()


# In[ ]:





# In[ ]:


#Assignment


# In[2]:


class bank():
    owner = ' '
    balance = ' '

def __init__ (self,owner,balance,deposit, withdraw):
    self.owner = owner
    self.balance = balance

    
def getBasicDetails(self):
        return {'owner':self.owner, 'balance':self.balance}

def deposit(self):
    a=balance + deposit
    return Final a


    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




