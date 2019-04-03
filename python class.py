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
>>> e+f
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    e+f
NameError: name 'e' is not defined
>>> e=a**b
>>> e
8
>>> type[a]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    type[a]
TypeError: 'type' object is not subscriptable
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
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'boy'
>>> i="23"
>>> i
'23'
>>> type(i)
<class 'str'>
>>> j=int(i)
>>> j
23
>>> type(j)
<class 'int'>
>>> float(3)
3.0
>>> print("hello achirachix")
hello achirachix
>>> print("hllo akirachix.\n 2019")
hllo akirachix.
 2019
>>> print("my namme is:\n joy \n wanja")
my namme is:
 joy 
 wanja
>>> print(haha\a")
	  
SyntaxError: unexpected character after line continuation character
>>> 
	  
>>> print("hello \t akirachix")
	  
hello 	 akirachix
>>> print("hello \v akirachix")
	  
hello  akirachix
>>> school="akirachix"
	  
>>> 
	  
>>> school= "akirachix"
	  
>>> school.upper9
	  
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    school.upper9
AttributeError: 'str' object has no attribute 'upper9'
>>> 
	  
>>> school.upper()
	  
'AKIRACHIX'
>>> school.lower()
	  
'akirachix'
>>> s="i love akirachix"
	  
>>> 
	  
>>> 
	  
>>> 
	  
>>> s"i love akirachix"
	  
SyntaxError: invalid syntax
>>> s" i love akirachix"
	  
SyntaxError: invalid syntax
>>> s=."i love akirachix"
	  
SyntaxError: invalid syntax
>>> s=".i love akirachix"
	  
>>> s="i love akirahix"
	  
>>> s
	  
'i love akirahix'
>>> s.upper()
	  
'I LOVE AKIRAHIX'
>>> s.lower()
	  
'i love akirahix'
>>> s.capitalize()
	  
'I love akirahix'
>>> school.endswith("x")
	  
True
>>> school.endwith("z")
	  
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    school.endwith("z")
AttributeError: 'str' object has no attribute 'endwith'
>>> school.endswith("z")
	  
False
>>> school.startswith("b")
	  
False
>>> school.startswith(:"A")
	  
SyntaxError: invalid syntax
>>> school.startswith("A")
	  
False
>>> s.isnumeic()
	  
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.isnumeic()
AttributeError: 'str' object has no attribute 'isnumeic'
>>> s.isnumeric()
	  
False
>>> school.isupper()
	  
False
>>> school.isalpha()
	  
True
>>> a="AKIRACHIX"
	  
>>> b="akirachix"
	  
>>> a.isupper()
	  
True
>>> b.islower()
	  
True
>>> first="Joy"
	  
>>> last="Wanja"
	  
>>> schooll="Akirachix"
	  
>>> print({}{},welcome to {}".format(first,last,school))
	  
SyntaxError: invalid syntax
>>> print("hello {}{},welcome to {}".format(first,last,school))
	  
hello JoyWanja,welcome to akirachix
>>> year=1995
	  
>>> year=1996
	  
>>> age=23
	  
>>> print(hello {}{},you are {} years old".format(first,last,age))
	  
SyntaxError: invalid syntax
>>> print("hello {}{},you are {}years old".format(first,last,age))
	  
hello JoyWanja,you are 23years old
>>> c1="Kenya"
	  
>>> c2="Uganda"
	  
>>> c3="Tanzania"
	  
>>> ke_code="254"
	  
>>> ug_code="256"
	  
>>> tzz_code="255"
	  
>>> cl
	  
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    cl
NameError: name 'cl' is not defined
>>> c1
	  
'Kenya'
>>> c2
	  
'Uganda'
>>> c3
	  
'Tanzania'
>>> ke_code
	  
'254'
>>> ug_code
	  
'256'
>>> tz_code
	  
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    tz_code
NameError: name 'tz_code' is not defined
>>> tzz_code
	  
'255'
>>> print("{} code is {}".format(c2,ke_code))
	  
Uganda code is 254
>>> print("{} code is {}".format(c1,ke_code))
	  
Kenya code is 254
>>> print("{}code is {}".format(cl,ug_code))
	  
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    print("{}code is {}".format(cl,ug_code))
NameError: name 'cl' is not defined
>>> print("{] code is {}".format(c2,ug_code))
	  
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    print("{] code is {}".format(c2,ug_code))
ValueError: unexpected '{' in field name
>>> print("{} code is {}".format(c2,ug_code))
	  
Uganda code is 256
>>> print("{} code is{}".format(c3,tz_code))
	  
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print("{} code is{}".format(c3,tz_code))
NameError: name 'tz_code' is not defined
>>> print("{} code is{}".format(c3,tzz_code))
	  
Tanzania code is255
>>> print("{} code is {} \n {} code is {} \n {} code is {}".format(c1
 
