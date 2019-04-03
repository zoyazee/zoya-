Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=2
>>> b=3
>>> d="boy"
>>> c="girl"
>>> a
2
>>> b
3
>>> d
'boy'
>>> c
'girl'
>>> a+b
5
>>> e=a**b
>>> e
8
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(d)
<class 'str'>
>>> type(c)
<class 'str'>
>>> type(e)
<class 'int'>
>>> f=10/b
>>> f
3.3333333333333335
>>> type(f)
<class 'float'>
>>> g=10//b
>>> g
3
>>> type(g)
<class 'int'>
>>> str(a)
'2'
>>> h=str(b)
>>> h
'3'
>>> type(h)
<class 'str'>
>>> i="123"
>>> i
'123'
>>> j=int(i)
>>> j
123
>>> type(j)
<class 'int'>
>>> print("hello akirachix")
hello akirachix
>>> print(hello airachix.\n 2019")
	  
SyntaxError: invalid syntax
>>>  print(hello akirachix.\n 2019")
	   
SyntaxError: unexpected indent
>>> print("hello airachix.\n 2019")
	   
hello airachix.
 2019
>>> print("my name is:\n joy \n wanja")
	   
my name is:
 joy 
 wanja
>>> print("haha\a")
	   
haha
>>> 
	   
>>> print("hello\t akirachix)
	  
SyntaxError: EOL while scanning string literal
>>> print("hello\t akirachix")
	  
hello	 akirachix
>>> print("hello\vakirachix")
	  
helloakirachix
>>> school="akirachix"
	  
>>> school.upper()
	  
'AKIRACHIX'
>>> school.lower()
	  
'akirachix'
>>> school="i love akirachix"
	  
>>> s
	  
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> school.upper()
	  
'I LOVE AKIRACHIX'
>>> school.lower()
	  
'i love akirachix'
>>> s.capitalize()
	  
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.capitalize()
NameError: name 's' is not defined
>>> s."i love akirachix"
	  
SyntaxError: invalid syntax
>>> s="i love akirachix"
	  
>>> s
	  
'i love akirachix'
>>> s.capitalize()
	  
'I love akirachix'
>>> s.endswith()
	  
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
>>> s.endswith()
	  
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
>>> s.endwith()
	  
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.endwith()
AttributeError: 'str' object has no attribute 'endwith'
>>> s.endswith("x")
	  
True
>>> s.endswith("z")
	  
False
>>> s.startswith("a")
	  
False
>>> s.startswith("i")
	  
True
>>> s.is numeric()
	  
SyntaxError: invalid syntax
>>> s.isnumeric()
	  
False
>>> school.isalpha()
	  
False
>>> s.isalpha()
	  
False
>>> school.isupper()
	  
False
>>> a=
	  
SyntaxError: invalid syntax
>>> a="AKIRACHIX"
	  
>>> b="akirachix"
	  
>>> s.isupper()
	  
False
>>> a.isupper()
	  
True
>>> b.islower()
	  
True
>>> first="Joy"
	  
>>> last="Wanja"
	  
>>> school="akirachix"
	  
>>> print("hello {}{} welcome to {}".format(first,last,school))
	  
hello JoyWanja welcome to akirachix
>>> year=1996
	  
>>> age=23
	  
>>> print("hello {}{} you are {} years old".format(first,last,age))
	  
hello JoyWanja you are 23 years old
>>> 
c1="kenya"
	  
>>> c2="uganda"
	  
>>> 
	  
>>> c3="tanzania"
	  
>>> ke_code="254"
	  
>>> ug_code="256"
	  
>>> tz_code="255"
	  
>>> c1
	  
'kenya'
>>> c2
	  
'uganda'
>>> c3
	  
'tanzania'
>>> ke_code
	  
'254'
>>> ug_code
	  
'256'
>>> tz_code
	  
'255'
>>> print("{} code is {}".formaat(c1,ke_code))
	  
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    print("{} code is {}".formaat(c1,ke_code))
AttributeError: 'str' object has no attribute 'formaat'
>>> print("{} code is {}".format(c1,ke_code))
	  
kenya code is 254
>>> print("{} code is {}".format(c2,ug_code))
	  
uganda code is 256
>>> print("{} code is {}".format(c3,tz_code))
	  
tanzania code is 255
>>> print({} code is {} \n {} code is {} \n {} code is {}".format(c1,ke_code,c2,ug_code,c3,tz_code))
	  
SyntaxError: invalid syntax
>>> print("{} code is {} \n {} code is {} \n {} code is {}".format(c1,ke_code,c2,ug_code,c3,tz_code))
	  
kenya code is 254 
 uganda code is 256 
 tanzania code is 255
>>> print("{} code is {},\n {} code is {},\n {} code is {}".format(c1,ke_code,c2,ug_code,c3,tz_code))
	  
kenya code is 254,
 uganda code is 256,
 tanzania code is 255
>>> print("{} code is {},{} code is {},{} code is {}".format(c1,ke_code,c2,ug_code,c3,tz_code))
	  
kenya code is 254,uganda code is 256,tanzania code is 255
>>> print("the codes of {},{},{} are {},{},{}".format(c1,ke_code,c2,ug_code,c3,tz_code))
	  
the codes of kenya,254,uganda are 256,tanzania,255
>>> print("the codes of {},{},{} are {},{},{}".format(c1,c2,c3,ke_code,ug_code,tz_code))
	  
the codes of kenya,uganda,tanzania are 254,256,255
>>> 
