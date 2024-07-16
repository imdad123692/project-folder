Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#iterative structure in python
#while loop
count=0
while(count<3):
    count=count+1
    print("hello greek")

    
hello greek
hello greek
hello greek
l=["geeks","for","geeks"]
for i in l:
    print(i)

    
geeks
for
geeks
l2=[1,3,4,5,6]
for i in l2:
    print(i)

    
1
3
4
5
6
#for in loop
#iterating over a tuple
t=("geeks","for","geeks")
for i in t
SyntaxError: expected ':'
t=("geeks","for","geeks")
for i in t:
    print(i)

    
geeks
for
geeks
#iterating over a string
print("string iteration")
string iteration
str1="python tutorial"
for i in str1:
    print(i)

    
p
y
t
h
o
n
 
t
u
t
o
r
i
a
l
#iterating by index of sequences
list=[1,2,3,4,5,6]
for index in range(len(list)):
    print(list[2])

    
3
3
3
3
3
3
#loop control statement
#continue statement
#continue statement
list=[1,2,3,4,5]
for i in list
SyntaxError: expected ':'
list[1,2,3,4,5,6]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list[1,2,3,4,5,6]
TypeError: list indices must be integers or slices, not tuple
list1=[1,2,3,4,5]
for i in list:
    print(i)

    
1
2
3
4
5
list2=[1,2,3,4,5,6]
for i in list
SyntaxError: expected ':'
list3=[1,2,3,34,5,6]
for i in list:
    if(i==6)
    
SyntaxError: expected ':'
list4=[1,2,3,4,5,6]
for i in list:
    if(i==3):
        continue
    print(list4)

    
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
list5=[7,8,9,1,2]
for i in list5
SyntaxError: expected ':'
list6=[1,2,3,4,5,6,7,8,9]
for i in list6
SyntaxError: expected ':'
list7=[1,2,3,4,5]
for i in list7:
    if(i==2)
    
SyntaxError: expected ':'
list8=(1,2,3,4,5,6)
for i in list8:
    if(i==2):
        continue
    print(list8)

    
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)
str1="python"
for i in str1:
    if(i=="y")
    
SyntaxError: expected ':'
str1="pythhon"
for i in str1:
    if(i=="y"):
        continue
    print(str1)

    
pythhon
pythhon
pythhon
pythhon
pythhon
pythhon
pythhon
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    pythhon
NameError: name 'pythhon' is not defined
str2="geeks for geeks"
for i in str2
SyntaxError: expected ':'
str3="geeksforgeeks"
for i in str3:
    if(i=='e'or i=='s'):
        continue
    print("current letter",i)

    
current letter g
current letter k
current letter f
current letter o
current letter r
current letter g
current letter k
list=[1,2,3,4,5]
for i in list:
    if(i==2):
        continue
    print(i)

    
1
3
4
5
word="apple"
for letter in word:
    if(letter=="p"):
        continue
    print("current letter",letter)

    
current letter a
current letter l
current letter e
for i in range(5):
    print(i)

    
0
1
2
3
4
for letter in 'geeksforgeeks':
    if(letter=="e" or letter=='s'):
        continue
    print(letter)

    
g
k
f
o
r
g
k
#break statement
for letter in "geeksforgeeks":
    if(letter=="k"):
        break
    print(letter)

    
g
e
e
#pyhthon function
def myfunction():
    print("hello from my function")
#calling function
myfunction()
SyntaxError: invalid syntax
def func():
    print("Hello")

    
func()
Hello
def func2():
    for i in "loop inside function":
        print(i)

        
func2()
l
o
o
p
 
i
n
s
i
d
e
 
f
u
n
c
t
i
o
n
#parameters in function
def my_function(fname):
    print(fname +'Refsnes)
          
SyntaxError: unterminated string literal (detected at line 2)
def func(fname):
    print(fname + "Refsnes")

    
func(emil)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    func(emil)
NameError: name 'emil' is not defined
def names(words):
    print(word +"Refsnes")

    
names(Tobias)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    names(Tobias)
NameError: name 'Tobias' is not defined
def name(words):
    print(word + "Refsnes")

    
name("tobias")
appleRefsnes
def funct(i):
    if(i>=3):
        print("hello word")

        
i=0
funct(4)
hello word
#default parameters
def my_function(country="pakistan"):
    print("i am from" ,country)

    
my_function("sweden")
i am from sweden
my_function()
i am from pakistan
my_function("Brazil")
i am from Brazil
#passing a list as a parameter
def my_func(food):
    for x in food:
        print(x)

        
fruits=["apple","banana","orange"]
my_funv(food)
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    my_funv(food)
NameError: name 'my_funv' is not defined. Did you mean: 'my_func'?
NameError: name 'my_funv' is not defined. Did you mean: 'my_func'?def my_func(food):
    for x in food:
        print(x)

        
fruits=["apple","banana","orange"]
my_func(food)
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
def fuction6(foods):
    for i in foods:
        print(i)

        
list=["apple","banana","cherry"] function6(list)
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
def my_elements(my_list):
    for i in my_list:
        print(i)

        
list1=["apple","cherry","banana"]
my_elements(list1)
apple
cherry
banana
#Return value
def myfunction(x)
SyntaxError: expected ':'
def myfunc(x):
    return 5*x
print(myfunc(3))
SyntaxError: invalid syntax
def my_f1(i):
    return5*i

    
print(my_f1(3))
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    print(my_f1(3))
  File "<pyshell#182>", line 2, in my_f1
    return5*i
NameError: name 'return5' is not defined
NameError: name 'return5' is not defined
SyntaxError: invalid syntax
def func5(z):
    return z*3
print(func5(3))
SyntaxError: invalid syntax
def multiply(a,b):
    return a*b
print(multiply(3,5))
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
def sun(x):
 return 5*x
print(sun(3))
SyntaxError: invalid syntax
def moon(y):
    return 6*y
result=moon(4)
SyntaxError: invalid syntax
def add(a,b):
    return a+b

result=add(3,5)
print(result)
8
def my_function1(t):
    return 5*t

print(my_function(3))
i am from 3
None
def subtract(a,b):
    return a-b

print(subtract(8,5))
3
#keyword arguments
#keyword arguments
def childs(x,y,z):
    print("the youngest child is" + z)

    
childs(y="tobias",z="emil",x="linus")
the youngest child isemil
#python classes and objects

class my_class:
    x=5

    
p1=my_class
>>> print(p1.x)
5
>>> class mine_c:
...     x=7
... 
...     
>>> mine_c p2
SyntaxError: invalid syntax
>>> class again:
...     z=9
... 
...     
>>> p3=again
>>> print(p3.z)
9
>>> #the _init_function
>>> class my_class2:
...     def _init_(self,name,age)
...     
SyntaxError: expected ':'
>>> class my_class3:
...     def _init_(self,name,age):
...         self.name=name
...         self.age=age
... 
...         
>>> p5=my_class3("john",34)
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    p5=my_class3("john",34)
TypeError: my_class3() takes no arguments
>>> class my_class4:
...     def _init_(self,name,age)
...     
SyntaxError: expected ':'
>>> SyntaxError: expected ':'
SyntaxError: invalid syntax
>>> 
>>> class person(self,name,age):
...     self.name=name
...     self.age=age
... 
...     
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    class person(self,name,age):
NameError: name 'self' is not defined
#the _init_function
print("Hello word")



