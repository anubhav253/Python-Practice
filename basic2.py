Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print 2 > 3
False
>>> a = []
>>> --list

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    --list
TypeError: bad operand type for unary -: 'type'
>>> //list
SyntaxError: invalid syntax
>>> a = [1,2,3,4]
>>> type(a)
<type 'list'>
>>> print a
[1, 2, 3, 4]
>>> a
[1, 2, 3, 4]
>>> a[-1]
4
>>> a[0]
1
>>> a[0] = 10
>>> a
[10, 2, 3, 4]
>>> a.appe

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.appe
AttributeError: 'list' object has no attribute 'appe'
>>> a.append(20)
>>> a
[10, 2, 3, 4, 20]
>>> a.insert
<built-in method insert of list object at 0x04DB3440>
>>> a.insert(a[1],50)
>>> a
[10, 2, 50, 3, 4, 20]
>>> a.remove(4)
>>> a
[10, 2, 50, 3, 20]
>>> a.append(2)
>>> a.remove(2)
>>> a
[10, 50, 3, 20, 2]
>>> a.remove(a)

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.remove(a)
ValueError: list.remove(x): x not in list
>>> a.remove(2)
>>> a
[10, 50, 3, 20]
>>> a.pop()
20
>>> a
[10, 50, 3]
>>> a.sort()
>>> a
[3, 10, 50]
>>> a.reverse()
>>> a
[50, 10, 3]
>>> b = [20,25,32]
>>> a.append(b)
>>> a
[50, 10, 3, [20, 25, 32]]
>>> a[3]
[20, 25, 32]
>>> a[3].b[0]

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a[3].b[0]
AttributeError: 'list' object has no attribute 'b'
>>> a[3][1]
25
>>> a.extend(b)
>>> a
[50, 10, 3, [20, 25, 32], 20, 25, 32]
>>> del a[3]
>>> a
[50, 10, 3, 20, 25, 32]
>>> a.append('Anubhav')
>>> a.sort()
>>> a
[3, 10, 20, 25, 32, 50, 'Anubhav']
>>> os = ('Android','iOS','WP')
>>> os
('Android', 'iOS', 'WP')
>>> os[1]
'iOS'
>>> os[0]= 'Indus'

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    os[0]= 'Indus'
TypeError: 'tuple' object does not support item assignment
>>> divmod(9564,23)
(415, 19)
>>> divmod(94,5)
(18, 4)
>>> a,b = divmod(23,5)
>>> a
4
>>> b
3
>>> os = ('Android','iOS','WP',1,2,3)
>>> os.sort()

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    os.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> os = ['Android','iOS','WP',1,2,3]
>>> os.sort()
>>> os
[1, 2, 3, 'Android', 'WP', 'iOS']
>>> os = ['Android','iOS','WP',1,2,3,'Delhi']
>>> os.sort()
>>> os
[1, 2, 3, 'Android', 'Delhi', 'WP', 'iOS']
>>> dict1 = {'fname' : 'Divyansh', 'major' : 'CSE'}
>>> fname = key

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    fname = key
NameError: name 'key' is not defined
>>> major = value

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    major = value
NameError: name 'value' is not defined
>>> dict1
{'major': 'CSE', 'fname': 'Divyansh'}
>>> dict1['city'] = 'Jaipur'
>>> dict1
{'city': 'Jaipur', 'major': 'CSE', 'fname': 'Divyansh'}
>>> list1[1,2,3,4,5,6,6,7,8]

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list1[1,2,3,4,5,6,6,7,8]
NameError: name 'list1' is not defined
>>> list1 = [1,2,3,4,5,6,6,7,8]
>>> list1
[1, 2, 3, 4, 5, 6, 6, 7, 8]
>>> if list1[1] == 2:
	print('Hello')
else:
	print('Not Found')

Hello
>>> if list1[-1] == 8
SyntaxError: invalid syntax
>>> if list1[-1] == 8:
	print 'Hi'

Hi
>>> num = 10
>>> while num < 20:
	print num
	num = num+1

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
>>> list1 = [1,2,4,3,5,4,36,4,2,4]
>>> 4 in list1
True
>>> 9 in list1
False
>>> 4 not in list1
False
>>> 4 and 5 in list1
True
>>> 4 and 9 in list1
False
>>> while list1 > 0:
	if(list1 == 4):
		del(4)
		
SyntaxError: can't delete literal
>>> while list1 > 0:
	if(list1 == 4):
		list1.remove(4)

	

Traceback (most recent call last):
  File "<pyshell#95>", line 2, in <module>
    if(list1 == 4):
KeyboardInterrupt

>>> while(4 in list1):
	list1.remove(4)

>>> list1
[1, 2, 3, 5, 36, 2]
>>> while list1 > 0:
	if(list1 == 4):
		list1.remove(4)


Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    while list1 > 0:
KeyboardInterrupt




>>> while(4 in list1):
	del(4)
	
SyntaxError: can't delete literal
>>> while list1<len(list1):
	if(list1 == 4):
		list1.remove(4)

>>> list1
[1, 2, 3, 5, 36, 2]
>>> while list1<len(list1):
	if(list1 == 2):
		list1.remove(2)

>>> list1
[1, 2, 3, 5, 36, 2]
>>> for item in list1:
	print item

1
2
3
5
36
2
>>> def add(a,b):
	return a+b

>>> add(4,5)
9
>>> def add1(a,b)
SyntaxError: invalid syntax
>>> def add1(a,b):
	print a+b

>>> add1(3,4)
7
>>> print add1(4,5)
9
None
>>> def add2(a,b,c=10):
	return a+b+c

>>> add2(4,5)
19
>>> add2(4,5,6)
15
>>> import math
>>> math.sqrt(18)
4.242640687119285
>>> from math import sqrt
>>> sqrt(25)
5.0
>>> from math import sqrt as jpr
>>> jpr(25)
5.0
>>> a = [1,2]
>>> b = [1,2]
>>> a is b
False
>>> a == b
True
>>> a is a
True
>>> c = a
>>> a is c
True
>>> a = [1,2,3]
>>> [x**2 for x in a]
[1, 4, 9]
>>> [x>2 for x in a]
[False, False, True]
>>> [x+1 for x in [x**2 for x in a]]
[2, 5, 10]
>>> import smtplib
>>> 
