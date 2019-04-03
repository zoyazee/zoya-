Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hello():
	print("hello Akirachix")

	
>>> hello()
hello Akirachix
>>> def hello(name):
	print("hello {}".format (name))

	
>>> hello("Zoya")
hello Zoya
>>> hello("Joy")
hello Joy
>>> hello("Brenda")
hello Brenda
>>> hello("Elvis")
hello Elvis
>>> hello("Angel")
hello Angel
>>> def sum(a,b):
	answer=a+b
	return answer

>>> sum(10,15)
25
>>> sum(1000,1000)
2000
>>> sum(10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sum(10)
TypeError: sum() missing 1 required positional argument: 'b'
>>> sum(10,30,40)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sum(10,30,40)
TypeError: sum() takes 2 positional arguments but 3 were given
>>> def sum(a,b):
	answer=a/b
	return answer

>>> sum(100,5)
20.0
>>> sum(1000,100)
10.0
>>> def sum(a,b):
	answer=45*9
	return answer

>>> sum(a,b)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sum(a,b)
NameError: name 'a' is not defined
>>> def sum(a,b):
	answer=a*b
	return answer

>>> sum(45,9)
405
>>> sum(9,9)
81
>>> def sum(a,b):
	answer=a-b
	return answer

>>> sum(50,20)
30
>>> sum(999,100)
899
>>> def sum(a,b):
	answer=a%b
	return answer

>>> sum(99,8)
3
>>> sum(100,10)
0
>>> def hello(name,age):
	print("Hello{},you are () years old".format(name,age))

	
>>> hello(Zoya,22)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    hello(Zoya,22)
NameError: name 'Zoya' is not defined
>>> hello("zoya"22)
SyntaxError: invalid syntax
>>> hello("Zoya","22")
HelloZoya,you are () years old
>>> hello("Zoya",22)
HelloZoya,you are () years old
>>> def hello(name,YOB):
	age=2019-YOB
	print("Hello {},you are {} years old".format(name,age))

	
>>> hello("Zoya",1996)
Hello Zoya,you are 23 years old
>>> def hello(name.YOB):
	
SyntaxError: invalid syntax
>>> 
>>> def hello(name,YOB):
	age(2019-YOB)
	print("Hello{},you are {} years old".format(name,age))

	
>>> hello("Brenda",2001)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    hello("Brenda",2001)
  File "<pyshell#66>", line 2, in hello
    age(2019-YOB)
NameError: name 'age' is not defined
>>> def hello(name,YOB):
	age=2019-YOB
	print("Hello{},you are {} years old".format(name,age))

	
>>> hello("Brenda",2001)
HelloBrenda,you are 18 years old
>>> def squares(numbers):
	for number in numbers:
		print(number*number)

		
>>> x=[1,2,3,4,5]
>>> y=[100,200,300,400]
>>> squares(x)
1
4
9
16
25
>>> squares(Y)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    squares(Y)
NameError: name 'Y' is not defined
>>> squares(y)
10000
40000
90000
160000
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
		return a

	
>>> x=[1,2,3,4,5]
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
	return a

>>> x=[1,2,3,4,5]
>>> squares(x)
[1, 4, 9, 16, 25]
>>> y=[100,200,300,400,500]
>>> squares(y)
[10000, 40000, 90000, 160000, 250000]
>>> def tens(numbers):
	a=[]
	for number in numbers:
		s=number*10
		a.append(s)

		
>>> def tens(numbers):
	a=[]
	for number in numbers:
		s=number*10
		a.append(s)
	return a

>>> x=[1,2,3,4,5]
>>> tens(x)
[10, 20, 30, 40, 50]
>>> y=[100,200,300,400,500]
>>> tens(y)
[1000, 2000, 3000, 4000, 5000]
>>> 
