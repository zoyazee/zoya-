Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[1,2,3,4,5]
>>> L=['a','b','c','d']
>>> 
>>> fruits= ['banana','apple','melon','avocado','orange','mango']
>>> for fruit in fuits:
	print(fruit)

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for fruit in fuits:
NameError: name 'fuits' is not defined
>>> for fruit in fruits:
	print(fruit)

	
banana
apple
melon
avocado
orange
mango
>>> numbers= [0,1,2,3,4,5,6,7,8,9]
>>> for number in numbers:
	print(number)

	
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
>>> fruits[0]
'banana'
>>> fruits[4]
'orange'
>>> fruits[0:4]
['banana', 'apple', 'melon', 'avocado']
>>> fruits[4:]
['orange', 'mango']
>>> fruits[-2:]
['orange', 'mango']
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6]
>>> d=a*3
>>> d
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> fruits
['banana', 'apple', 'melon', 'avocado', 'orange', 'mango']
>>> fruits.append(grapes)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fruits.append(grapes)
NameError: name 'grapes' is not defined
>>> fruits.append("grapes")
>>> 
>>> fruits.append("grapes")
>>> fruits
['banana', 'apple', 'melon', 'avocado', 'orange', 'mango', 'grapes', 'grapes']
>>> fruits.extend("peach","kiwi,"
		  fruits
		  
SyntaxError: invalid syntax
>>> fruits.extend("peach","kiwi,")
		  fruits
		  
SyntaxError: multiple statements found while compiling a single statement
>>> fruits.extend("peach","kiwi")
		  
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    fruits.extend("peach","kiwi")
TypeError: extend() takes exactly one argument (2 given)
>>> fruits.extend(["peach","kiwi"])
		  
>>> fruits
		  
['banana', 'apple', 'melon', 'avocado', 'orange', 'mango', 'grapes', 'grapes', 'peach', 'kiwi']
>>> fruits.remove("melon)
		  
SyntaxError: EOL while scanning string literal
>>> fruits.remove("melon")
		  
>>> fruit
		  
'mango'
>>> fruits
		  
['banana', 'apple', 'avocado', 'orange', 'mango', 'grapes', 'grapes', 'peach', 'kiwi']
>>> fruits.sort()
		  
>>> fruits
		  
['apple', 'avocado', 'banana', 'grapes', 'grapes', 'kiwi', 'mango', 'orange', 'peach']
>>> fruits.reverse()
		  
>>> fruits
		  
['peach', 'orange', 'mango', 'kiwi', 'grapes', 'grapes', 'banana', 'avocado', 'apple']
>>> fruits.pop()
		  
'apple'
>>> fruits
		  
['peach', 'orange', 'mango', 'kiwi', 'grapes', 'grapes', 'banana', 'avocado']
>>> del fruits[0]
		  
>>> fruits
		  
['orange', 'mango', 'kiwi', 'grapes', 'grapes', 'banana', 'avocado']
>>> fruits.replace("banana","dates")
		  
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    fruits.replace("banana","dates")
AttributeError: 'list' object has no attribute 'replace'
>>> numbers
		  
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sum(numbers)
		  
45
>>> sum(fruits)
		  
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    sum(fruits)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> min(numbers)
		  
0
>>> max(numbers)
		  
9
>>> fruits("banana")
		  
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    fruits("banana")
TypeError: 'list' object is not callable
>>> fruits.append("banana")
		  
>>> fruits.append("mango")
		  
>>> fruits.append("ornge")
		  
>>> fruits.count("mango")
		  
2
>>> fruits.count("banana")
		  
2
>>> n=range(10)
		  
>>> n
		  
range(0, 10)
>>> for xin n:
		  
SyntaxError: invalid syntax
>>> for x in n:
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
>>> range(10,20)
		  
range(10, 20)
>>> m=range(10,20)
		  
>>> m
		  
range(10, 20)
>>> for x in m:
		  print(x)

		  
10
11
12
13
14
15
16
17
18
19
>>> e=[x*10 for x in a]
		  
>>> e
		  
[10, 20, 30]
>>> f=[x*2 for x in e]
		  
>>> f
		  
[20, 40, 60]
>>> g=range(25,50)
		  
>>> h=[x*x for x in g]
		  
>>> h
		  
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> h=[]
		  
>>> for x in g:
		  h.append(x)

		  
>>> h
		  
[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> h=[]
		  
>>> for x in g:
		  y=x*x
		  h.append(y)

		  
>>> h
		  
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> x=[100,200,300,400,500]
		  
>>> g=[y%7 for y in x]
		  
>>> g
		  
[2, 4, 6, 1, 3]
>>> g=[]
		  
>>> for y in x
		  
SyntaxError: invalid syntax
>>> g=[]
		  
>>> for y in x:
		  z=y%7
		  g.append(z)

		  
>>> z
		  
3
>>> 
		  
>>> 
		  
>>> 
		  
>>> a=range(99,109)
		  
>>> b=[x*x for x in a]
		  
>>> b
		  
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> nested=[[1,2,3][4,5,6],[7,8,9]]
		  
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    nested=[[1,2,3][4,5,6],[7,8,9]]
TypeError: list indices must be integers or slices, not tuple
>>> m=flat[[1,2,3],[4,5,6],[7,8,9]]
		  
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    m=flat[[1,2,3],[4,5,6],[7,8,9]]
NameError: name 'flat' is not defined
>>> x=[100,200,300,400,500]
		  
>>> g=[y%7 for y in x]
		  
>>> g
		  
[2, 4, 6, 1, 3]
>>> g[]
		  
SyntaxError: invalid syntax
>>> g=[]
		  
>>> for y in x:
		  z=y%7
		  g.append(a)

		  
>>> z
		  
3
>>> g
		  
[range(99, 109), range(99, 109), range(99, 109), range(99, 109), range(99, 109)]
>>> a
		  
range(99, 109)
>>> 
