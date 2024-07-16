Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello , Word")
Hello , Word
x=1
#comments in phthon
#comments in phthon the initial value of x is 1.
if x>0:
    print("these are two comments ") #print a string.

    
these are two comments 
txt=input("type something to test this out")
type something to test this out
print(txt)




#multiple statement on a single line:
print("statement 1")
statement 1
print("statement 2")
statement 2
print("statement 1");print("statement 2")
statement 1
statement 2
#identation
x=1
if x>0:
print("this statement has no identation")
SyntaxError: expected an indented block after 'if' statement on line 1
x=1
if x>0:
 print("this statement has a single space identation")

 
this statement has a single space identation
x=1
if x>0 :
    print("this statement has a single tab identation")

    
this statement has a single tab identation
x=1
if x>0
SyntaxError: expected ':'
x=1
if x>0:
     print("this statement has a single tab+single space identation)
           
SyntaxError: unterminated string literal (detected at line 2)

x=1
           
if x>0:
     print("this statement has a single space+single tab indentatin")

           
this statement has a single space+single tab indentatin
#Data types and Types casting
           
a=7
           
type(a)
           
<class 'int'>
<class 'int'>
           
SyntaxError: invalid syntax
h=11.34
           
type(h)
           
<class 'float'>
#complex number
           
x=complex(3,5)
           
type(x)
           
<class 'complex'>
print(x)
           
(3+5j)
z=complex(7,9)
           
type(x)
           
<class 'complex'>
print(z)
           
(7+9j)
#boolean(bool)
           
x=True
           
type(x)
           
<class 'bool'>
g=False
           
type(g)
           
<class 'bool'>
#strings
           
str1="this is a double quotes string"
           
print(str1)
           
this is a double quotes string
str2='this is single quote string'
           
print(str2)
           
this is single quote string
str3="day's"#sinle quote within double quote
           
print(str3)
           
day's
#special characters in strings
           
print("this is a tab \t key")
           
this is a tab 	 key
print("ihis is a new \n line key")
           
ihis is a new 
 line key
print("ihis is a \" double quotes \" key")
           
ihis is a " double quotes " key
print("this is a \\ mark.")
           
this is a \ mark.
#string indices and accessing string elements
           
string1="python tutorial"
           
print(string1[5])
           
n
string2="python tutorial"
           
print(string2[-2])
           
a
#string slices
           
#creating list
           
#creating list
           
list1=[1,2,3,4,5,6,7]
           
print(list1)
           
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
           
[1, 2, 3, 4, 5, 6, 7]
list2=[red,1,0.9,4,black]
           
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    list2=[red,1,0.9,4,black]
NameError: name 'red' is not defined
NameError: name 'red' is not defined list3=[3,5]
           
SyntaxError: invalid syntax
list3=['red',1]
...            
>>> print(list3)
...            
['red', 1]
>>> #list indices
...            
>>> mylist=["red","black","white","blue"]
...            
>>> print(mylist)
...            
['red', 'black', 'white', 'blue']
>>> mylist(0)
...            
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    mylist(0)
TypeError: 'list' object is not callable
>>> list5=[1,2,3,4,5,6]
...            
>>> list5[3]
...            
4
>>> list6=[1,2,3,4,5,6]
...            
>>> list6[-2]
...            
5
>>> #list slice
...            
>>> str7="phython tuturial"
...            
>>> print(str7[2:4])
...            
yt
>>> list8=[1,2,3,4,5]
...            
>>> print(list8[0,2])
...            
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(list8[0,2])
TypeError: list indices must be integers or slices, not tuple
>>> list9=[1,2,3,4,5]
...            
>>> print(list9[0:2])
...            
[1, 2]
