000000000000000000003++-**----------****Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sumlist(m):
	a=[]
	for x in range(1,m+1):
		a.append(x)
		b=sum(a)
	return b

>>> sumlist(10)
55
>>> sumlist(5)
15
>>> def functionname(lists,i):
	b=[]
	c=[]
	for x in lists:
		if x%i==0:
			b.append(x)
		else:
			c.append(x)
	print(b)
	print(c)

	
>>> d=[1,2,3,4,5]
>>> functionname(d,2)
[2, 4]
[1, 3, 5]
>>> e=[1,2,3,4,5,6,,8]
>>> e=[1,2,3,4,5,6,7,8]
>>> functionname(e,3)
[3, 6]
[1, 2, 4, 5, 7, 8]
>>> 
