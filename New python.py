#!/usr/bin/env python
# coding: utf-8

# In[4]:


L = []
for i in range(5):
    print(i + 1)
    L.append(i**2)
print(L)


# In[7]:


i = 1
while True:
    if i%17 == 0:
        print("BREAK")
    else:
        i += 1
        print("do nothing")
        break
print("DONE")


# In[21]:


import time
for i in range(10):
    i += 1
    print(i, end='')
    time.sleep(2)


# In[6]:


n = 10
i = 1
while True:
    if i%9 != 0:
        print("inside if")
        i += 1
        continue
    else:
        print("yes")
        print("yes-yes")
        break
print("DONE")


# In[10]:


L = []
for i in range (10):
    print(i + 1)
    L.append(i**2)
print(L)


# In[23]:


s = {"apple","wefwe","akama" }
for x in s:
    print(x)
else:
    print ("loop ends")


# In[34]:


q = {"A":23, "B":123, "C":'ABC'}
for x in q:
    print(x, q[x])


# In[56]:


L = [1,2,4,-10,-5,13]
m = L[0]
for i in L:
    if i < m:
        m = i
    
print(m)


# In[63]:


Q = [12,233,344,6778,77]
p = Q[0]
for T in Q:
    if T<p:
        P = T
       
print(p)


# In[74]:


L = [12777,333,456,44567,344,34,4566]
m = L[0]
idx = 0
c = 0
for i in L:
    if i<m:
        m = i
        idx = c
    c+=1
tmp = L[0]
L[0] = m
L[idx] = tmp
print(L)


# In[3]:


L = [0.3,-23,-344,2,3,4555]
for j in range(len(L)):
    m = L[j]
    idx = j
    c = j
    for i in range (j,len(L)):
        if L[i] < m:
            m = L[i]
            idx = c
        c += 1
    tmp = L[j]
    L[j] = m
    L[idx] = tmp
    
print()


# In[5]:


def print_all():
    print("lweny marwa")
    print("ROHO")


# In[7]:


print_all()





# In[8]:


def PrintSuccess():
    """This function is basically printing 'hello world'.
    """
    print("hellow Allan Akama")


# In[9]:


get_ipython().run_line_magic('pinfo', 'PrintSuccess')


# In[17]:


def printGiven(given):
    """This function will print the details provided by the user if a string or else it will 
    while show the type of message it is.
    """
    if isinstance(given,str):
        print(given)
    else:
        print("The given input is not a string but rather a:",type(given))


# In[18]:


printGiven(23)


# In[20]:


printGiven("I am the best")


# In[27]:


def mypow(a,b):
    c= a**b
    print(c)


# In[30]:


mypow(375,44)


# In[73]:


def CheckDetails(a,c,b):
    if isinstance(a,(int,float)) and isinstance(c,(int,float)) and isinstance(b,(int,float)):
        print((a+c)**34)
    else:
        print("Error")

    


# In[74]:


CheckDetails(3,4,3)


# In[75]:


CheckDetails(2383,9494,4994)


# In[96]:


a = input("ENTER :" ) 
if isinstance == int:
    print("integer")
else:
    print(a,"is not an integer",type(a))


# In[90]:


get_ipython().run_line_magic('pinfo', 'int')


# In[97]:


def g():
    a = 124555
    b = 2299922
    c = a*b
    print("DONE")
    return


# In[100]:


print(type,g())


# In[107]:


def g():
    a = 23433
    b = 12345678
    d = a*b
    print("DONE")
    return d


# In[108]:


g()


# In[118]:


def s():
    a = 8222
    b = 2993
    d = "Something"
    return a,b,d


# In[124]:


x,y,z = s()
print(x,y,z)


# In[133]:


def add(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]  #sum = sum + args[i]
    return sum


# In[134]:


print(add(233,344,4445,56555,555566))


# In[138]:


print((add(233,3444,678,88887778)**3))


# In[16]:


def f(**args):
    for x in args:
        print(x,args[x])


# In[17]:


f(a="illest", b= 21, c= 345678,d= 345642345)


# In[18]:


def gg(s=5):
    print(s)


# In[19]:


gg()


# In[20]:


gg(45678)


# In[21]:


gg("heloo")


# In[22]:


L = [2233,455,66]
L2 = L
L2[0] = -23
print(L)


# In[38]:


def Checkifnumeric(*args):
    for i in args:
        if isinstance(i,(float,int)):
            print("Numeric")
        else:
            print("Not Numeric")


# In[40]:


Checkifnumeric(2,3),(233,454,544),(112,34445,5666,"low")


# In[47]:


price = 12
s = "The price of this book is: "
v = s + str(price)


# In[48]:


print(v)


# In[51]:


s = "How are you and where do you come from?"
print(s[4:15])


# In[53]:


type(s[4:15])


# In[54]:


s[-1]


# In[57]:


s[1:12:2]


# In[60]:


s[::-1]


# In[61]:


print(len(s))


# In[62]:


b = s.strip()
print(b)


# In[67]:


T = '                  I believe you    can see  the     spaces    in this sentence                           '
a = T.strip()


# In[68]:


print(a)


# In[71]:


a = "ABC def gh"
b = a.lower()
print(b)


# In[73]:


a = "abc Def ,,,, gh"
b = a.upper()
print(b)


# In[86]:


a = "hello you ,,,, there"
d = a.replace(",,,,", "***" ) 


# In[87]:


print(d)


# In[ ]:


#PROJECTS


# In[37]:


import random
def guess(x):
    random_number = random.randint(1,20)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and 20:"))
        if guess < random_number:
            print ("sorry, low ")
        elif guess > random_number:
            print("sorry, high")
    print(f"Good job you have the right number which is {random_number}")



# In[30]:


import random
target_num, guess_num = random.randint(1, 10),0 
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')


# In[ ]:





# In[ ]:




