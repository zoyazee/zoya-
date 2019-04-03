Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1 = {"name":"Sharon","balance":400}
>>> customer2 = {"name":"Everlyne","balance":2500}
>>> customer3 = {"name":"Mercy","balance":300}
>>> customer4 = {"name":"joy","balance":2000}
>>> customer5 = {"name":"Zoya","balance":10000}
>>> customers = [customer1,customer2,customer3,customer4,customer5]
>>> customers
[{'name': 'Sharon', 'balance': 400}, {'name': 'Everlyne', 'balance': 2500}, {'name': 'Mercy', 'balance': 300}, {'name': 'joy', 'balance': 2000}, {'name': 'Zoya', 'balance': 10000}]
>>> for customer in cusomers
SyntaxError: invalid syntax
>>> for customer in cusomers:
	sms = "Hi{},your balance is {}".formart(customer["name"],customer["balance"])
	sms

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for customer in cusomers:
NameError: name 'cusomers' is not defined
>>> for customer in cusomers:
	sms = "Hi{},your balance is {}".format(customer["name"],customer["balance"])
	sms

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for customer in cusomers:
NameError: name 'cusomers' is not defined
>>> for customer in cusomers:
	sms = "Hi{},your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for customer in cusomers:
NameError: name 'cusomers' is not defined
>>> for customer in customers:
	sms = "Hi{},your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
HiSharon,your balance is 400
HiEverlyne,your balance is 2500
HiMercy,your balance is 300
Hijoy,your balance is 2000
HiZoya,your balance is 10000
>>> for customer in customers:
	loan = customer["balance"]/ 2.9
	sms = "Dear{}, your balance is {},qualifying for a loan of shs.()".formart(customer["name"],customer["balance"],customer["loan"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 3, in <module>
    sms = "Dear{}, your balance is {},qualifying for a loan of shs.()".formart(customer["name"],customer["balance"],customer["loan"])
AttributeError: 'str' object has no attribute 'formart'
>>> for customer in customers:
	loan = customer["balance"]/ 2.9
	sms = "Dear{}, your balance is {},qualifying for a loan of shs.()".format(customer["name"],customer["balance"],customer["loan"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    sms = "Dear{}, your balance is {},qualifying for a loan of shs.()".format(customer["name"],customer["balance"],customer["loan"])
KeyError: 'loan'
>>> for customer in customers:
	loan = customer["balance"]/ 2.9
	sms = "Dear{}, your balance is {},qualifying for a loan of shs.{}".format(customer["name"],customer["balance"],loan)
	print(sms)

	
DearSharon, your balance is 400,qualifying for a loan of shs.137.93103448275863
DearEverlyne, your balance is 2500,qualifying for a loan of shs.862.0689655172414
DearMercy, your balance is 300,qualifying for a loan of shs.103.44827586206897
Dearjoy, your balance is 2000,qualifying for a loan of shs.689.6551724137931
DearZoya, your balance is 10000,qualifying for a loan of shs.3448.2758620689656
>>> for x in range (0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> for x in range (0,10):
	if x%3!=0:
		print(x)

		
1
2
4
5
7
8
>>> for x in range (0,10):
	if x%3==0:
		print("{} is divisible by 3".format(x))

		
0 is divisible by 3
3 is divisible by 3
6 is divisible by 3
9 is divisible by 3
>>> for x in range (0,10):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> for x in range (0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	elif x%5==0:
		print("{} is not divisible 5".format(x))
	else:
		print("{} is not divisible by 3 or 5".formart(x))

		
0 is divisible by 3
Traceback (most recent call last):
  File "<pyshell#49>", line 7, in <module>
    print("{} is not divisible by 3 or 5".formart(x))
AttributeError: 'str' object has no attribute 'formart'
>>> for x in range (0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	elif x%5==0:
		print("{} is not divisible 5".format(x))
	else:
		print("{} is not divisible by 3 or 5".format(x))

		
0 is divisible by 3
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divisible by 3
4 is not divisible by 3 or 5
5 is not divisible 5
6 is divisible by 3
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divisible by 3
10 is not divisible 5
11 is not divisible by 3 or 5
12 is divisible by 3
13 is not divisible by 3 or 5
14 is not divisible by 3 or 5
15 is divisible by 3
16 is not divisible by 3 or 5
17 is not divisible by 3 or 5
18 is divisible by 3
19 is not divisible by 3 or 5
>>> for x in range(0,100):
	if x%7==0:
		print(x)

		
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
>>> for x in range(0,20):
	if x%==0 and x%5==0:
		print(x)
		
SyntaxError: invalid syntax
>>> for x in range(0,20):
	if x%3==0 and x%5==0:
		print(x)

		
0
15
>>> for x in range(0,20):
	if x%3==0 or x%5==0:
		print(x)

		
0
3
5
6
9
10
12
15
18
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> 
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> for x in range (900,950):
	if x%3==0 and x%5==0:
		print("{} fizzbuzz".format(x))
	elif x%3==0:
		print("{} buzz".format(x))
	else x%5==0:
		
SyntaxError: invalid syntax
>>> for x in range (900,950):
	if x%3==0 and x%5==0:
		print("{} fizzbuzz".format(x))
	elif x%3==0:
		print("{} buzz".format(x))
	else:
		print("{} fizz".format(x))

		
900 fizzbuzz
901 fizz
902 fizz
903 buzz
904 fizz
905 fizz
906 buzz
907 fizz
908 fizz
909 buzz
910 fizz
911 fizz
912 buzz
913 fizz
914 fizz
915 fizzbuzz
916 fizz
917 fizz
918 buzz
919 fizz
920 fizz
921 buzz
922 fizz
923 fizz
924 buzz
925 fizz
926 fizz
927 buzz
928 fizz
929 fizz
930 fizzbuzz
931 fizz
932 fizz
933 buzz
934 fizz
935 fizz
936 buzz
937 fizz
938 fizz
939 buzz
940 fizz
941 fizz
942 buzz
943 fizz
944 fizz
945 fizzbuzz
946 fizz
947 fizz
948 buzz
949 fizz
>>> for x in range (900,950):
	if x%3==0 and x%5==0:
		print("fizzbuzz")
	elif x%3==0:
		print("buzz")
	elif x%5==0:
		print("fizz")
	else:
		print(x)

		
fizzbuzz
901
902
buzz
904
fizz
buzz
907
908
buzz
fizz
911
buzz
913
914
fizzbuzz
916
917
buzz
919
fizz
buzz
922
923
buzz
fizz
926
buzz
928
929
fizzbuzz
931
932
buzz
934
fizz
buzz
937
938
buzz
fizz
941
buzz
943
944
fizzbuzz
946
947
buzz
949
>>> 
