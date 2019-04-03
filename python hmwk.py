Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> for x in range (0,100):
	if x%9==0:
		a.append(x)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b=[]
>>> for x in range (0,100):
	if x%11==0:
		b.append(x)

		
>>> b
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c=a+b
>>> c
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> a=[]
>>> b=[]
>>> for x in range (0,100):
	if x%9==0:
		a.append(x)
	elif x%11==0:
		b.append(x)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b
[11, 22, 33, 44, 55, 66, 77, 88]
>>> c=a+b
>>> c
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 11, 22, 33, 44, 55, 66, 77, 88]
>>> c.sort()
>>> c
[0, 9, 11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88, 90, 99]
>>> 
>>> for x in range(2019,2119):
	if x%4==0:
		print(x)

		
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
2064
2068
2072
2076
2080
2084
2088
2092
2096
2100
2104
2108
2112
2116
>>> 
>>> students1 ={"name":"Aisha","yob":1998}
>>> students2 ={"name":"Joy","yob":1997}
>>> students3 ={"name":"Brenda","yob":1999}
>>> students4 ={"name":"Elvis","yob":2000}
>>> students5students1 ={"name":"Aisha","yob":1998}
>>> 
>>> 
>>> 
>>> student1 ={"name":"Zoya","yob":1998}
>>> student2 ={"name":"Joy","yob":1997}
>>> student3 ={"name":"Brenda","yob":1999}
>>> student4 ={"name":"Elvis","yob":2000}
>>> student5 ={"name":"Angel","yob":1995}
>>> students =[student1,student2,student3,student4,student5]
>>> students
[{'name': 'Zoya', 'yob': 1998}, {'name': 'Joy', 'yob': 1997}, {'name': 'Brenda', 'yob': 1999}, {'name': 'Elvis', 'yob': 2000}, {'name': 'Angel', 'yob': 1995}]
>>> for student in students:
	y=(2019-student["yob"])*365
	message="Dear friend {},you are {} days old".format(student["name"],y)
	print(message)

	
Dear friend Zoya,you are 7665 days old
Dear friend Joy,you are 8030 days old
Dear friend Brenda,you are 7300 days old
Dear friend Elvis,you are 6935 days old
Dear friend Angel,you are 8760 days old
>>> 
