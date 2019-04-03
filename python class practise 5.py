Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
a=(1,2,3,4)
>>> 
>>> 
>>> a=(1,2,3,4)
>>> b=('a','b','c','d')
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> b.remove('c')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b.remove('c')
AttributeError: 'tuple' object has no attribute 'remove'
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> b.pop()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> b.sort()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> for x in a:
	print(x)

	
1
2
3
4
>>> c=list(a)
>>> c
[1, 2, 3, 4]
>>> d=(x for x in a)
>>> d
<generator object <genexpr> at 0x036AACB0>
>>> d=[x for x in a]
>>> d
[1, 2, 3, 4]
>>> a
(1, 2, 3, 4)
>>> f=a+b
>>> f
(1, 2, 3, 4, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> "b" in b
True
>>> "e in b
SyntaxError: EOL while scanning string literal
>>> "e" in b
False
>>> 5 in a
False
>>> 1 in a
True
>>> x=[1,2,3,4]
>>> y=(x)
>>> y
[1, 2, 3, 4]
>>> y=(z for z in x)
>>> y
<generator object <genexpr> at 0x036AACB0>
>>> a=[1,2,3,1,4,2,5,3,7]
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 7}
>>> c={"a","b","a","c","c"}
>>> c
{'c', 'a', 'b'}
>>> d={"a","A","b","B"}
>>> d
{'B', 'A', 'a', 'b'}
>>> s1{1,2,3,}
SyntaxError: invalid syntax
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s2.remove(7)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s2.remove(7)
KeyError: 7
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{4, 5, 6}
>>> s1.intersection(s2)
{3}
>>> s2.intersection(s1)
{3}
>>> s2.union(s1)
{1, 2, 3, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> 
>>> 
>>> s1.extend(s2)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s1.extend(s2)
AttributeError: 'set' object has no attribute 'extend'
>>> s2.add(7,8)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s2.add(7,8)
TypeError: add() takes exactly one argument (2 given)
>>> s2.update({10,11,12})
>>> s2
{3, 4, 5, 6, 10, 11, 12}
>>> 
>>> 
>>> codes{"Kenya"
	  
SyntaxError: invalid syntax
>>> codes{"Kenya":254, "Uganda":256, "Tanzania":255}
	  
SyntaxError: invalid syntax
>>> codes={"Kenya":254, "Uganda":256, "Tanzania":255}
	  
>>> codes
	  
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255}
>>> codes["Kenya"]
	  
254
>>> codes["Uganda"]
	  
256
>>> codes["Tanzania"]
	  
255
>>> codes["Kenya"]=250
	  
>>> codes
	  
{'Kenya': 250, 'Uganda': 256, 'Tanzania': 255}
>>> codes["Kenya"]=254
	  
>>> codes
	  
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255}
>>> codes["Rwanda"]=252
	  
>>> codes
	  
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255, 'Rwanda': 252}
>>> codes.pop("Rwanda")
	  
252
>>> codes
	  
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255}
>>> codes.keys()
	  
dict_keys(['Kenya', 'Uganda', 'Tanzania'])
>>> codes.values()
	  
dict_values([254, 256, 255])
>>> for key in codes.keys():
	  print(key)

	  
Kenya
Uganda
Tanzania
>>> for x in codes.keys():
	  print(x)

	  
Kenya
Uganda
Tanzania
>>> for value in codes.values()
	  
SyntaxError: invalid syntax
>>> for value in codes.values():
	  print(value)

	  
254
256
255
>>> m=dict()
	  
>>> m
	  
{}
>>> m["a"]=10
	  
>>> m["b"]=20
	  
>>> m
	  
{'a': 10, 'b': 20}
>>> range(0,10)
	  
range(0, 10)
>>> range.keys()
	  
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    range.keys()
AttributeError: type object 'range' has no attribute 'keys'
>>> range.keys(range)
	  
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    range.keys(range)
AttributeError: type object 'range' has no attribute 'keys'
>>> print(range)
	  
<class 'range'>
>>> m=range(0,10)
	  
>>> for x in m:
	  print(x)

	  
0
1
2
3
4
5
6
7
8
9
>>> m.keys()
	  
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    m.keys()
AttributeError: 'range' object has no attribute 'keys'
>>> m.keys(0,10)
	  
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    m.keys(0,10)
AttributeError: 'range' object has no attribute 'keys'
>>> x.keys()
	  
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    x.keys()
AttributeError: 'int' object has no attribute 'keys'
>>> int.keys()
	  
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    int.keys()
AttributeError: type object 'int' has no attribute 'keys'
>>> m.range()
	  
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    m.range()
AttributeError: 'range' object has no attribute 'range'
>>> m=dict()
	  
>>> m
	  
{}
>>> m.keys()
	  
dict_keys([])
>>> m=dict(0,10)
	  
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    m=dict(0,10)
TypeError: dict expected at most 1 arguments, got 2
>>> m.keys(0,10)
	  
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    m.keys(0,10)
TypeError: keys() takes no arguments (2 given)
>>> m.keys([1,10])
	  
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    m.keys([1,10])
TypeError: keys() takes no arguments (1 given)
>>> for key in m.keys()
	  
SyntaxError: invalid syntax
>>> for key in m.keys():
	  print(key)

	  
>>> for key in m.keys():
	  print(key)

	  
>>> for key in m. keys():
	  print(key)

	  
>>> 
	  
>>> 
	  
>>> m[0,10]=0,10*0,10
	  
>>> m
	  
{(0, 10): (0, 0, 10)}
>>> m=dict()
	  
>>> for p in range(10):
	  m[p]=p*p
	  print(m)

	  
{0: 0}
{0: 0, 1: 1}
{0: 0, 1: 1, 2: 4}
{0: 0, 1: 1, 2: 4, 3: 9}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> for p in rangee(10:
		    
SyntaxError: invalid syntax
>>> m[p]=p*p
		    
>>> print(m)
		    
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> fruits=["melon","apple","orange,","banana","kiwi","avocado","peas","plums","mango","pineapple")
		    
SyntaxError: invalid syntax
>>> fruits=["melon","apple","orange,","banana","kiwi","avocado","peas","plums","mango","pineapple"]
		    
>>> j=dict()
		    
>>> for z in character(fruits)
		    
SyntaxError: invalid syntax
>>> for z in character(fruits):
>>>print(z)
		    
SyntaxError: expected an indented block
>>> print(z)
		    
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> j[z]=length
		    
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    j[z]=length
NameError: name 'length' is not defined
>>> j[z]=characters
		    
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    j[z]=characters
NameError: name 'characters' is not defined
>>> for x in fruits
		    
SyntaxError: invalid syntax
>>> for x in fruits:
		    jx=length
		    jx

		    
Traceback (most recent call last):
  File "<pyshell#153>", line 2, in <module>
    jx=length
NameError: name 'length' is not defined
>>> for x in fruits:
		    j[x=len of (z)]
		    
SyntaxError: invalid syntax
>>> j[x]=len(x)
		    
>>> 
		    
>>> j
		    
{'melon': 5}
>>> j=dict()
		    
>>> for x in fruits
		    
SyntaxError: invalid syntax
>>> for x in fruits:
		    j(x)len(x)
		    
SyntaxError: invalid syntax
>>> fruits=["melon","apple","orange,","banana","kiwi","avocado","peas","plums","mango","pineapple"]
		    
>>> fruits
		    
['melon', 'apple', 'orange,', 'banana', 'kiwi', 'avocado', 'peas', 'plums', 'mango', 'pineapple']
>>> h=dict()
		    
>>> h
		    
{}
>>> for x in fruits:
		    h[x]=len(x)

		    
>>> h
		    
{'melon': 5, 'apple': 5, 'orange,': 7, 'banana': 6, 'kiwi': 4, 'avocado': 7, 'peas': 4, 'plums': 5, 'mango': 5, 'pineapple': 9}
>>> 






