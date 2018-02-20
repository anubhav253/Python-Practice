Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=0
>>> type(a)
<type 'int'>
>>> a=5.2
>>> type(a)
<type 'float'>
>>> a=none

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=none
NameError: name 'none' is not defined
>>> a = None
>>> type(a)
<type 'NoneType'>
>>> a= True
>>> int(4.5)
4
>>> float(5)
5.0
>>> a = input("Enter the number:")
Enter the number:5
>>> print(a)
5
>>> print a
5
>>> name = raw_input("Name:")
Name:AK
>>> print name
AK
>>> str1 = "Anubhav"
>>> len(str1)
7
>>> str1[0]
'A'
>>> str1[0:5]
'Anubh'
>>> str1[0:7:2]
'Auhv'
>>> str1[1:]
'nubhav'
>>> str1[:6]
'Anubha'
>>> str1[0]='f'

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    str1[0]='f'
TypeError: 'str' object does not support item assignment
>>> del str1
>>> print str1

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print str1
NameError: name 'str1' is not defined
>>> str1="Anubhav"
>>> str1.upper
<built-in method upper of str object at 0x05D94E00>
>>> print str1
Anubhav
>>> str1.u

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    str1.u
AttributeError: 'str' object has no attribute 'u'
>>> str1.upper()
'ANUBHAV'
>>> str1.re

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    str1.re
AttributeError: 'str' object has no attribute 're'
>>> str1.replace('n', 'N')
'ANubhav'
>>> print 5*AK

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print 5*AK
NameError: name 'AK' is not defined
>>> print 5*"AK"
AKAKAKAKAK
>>> print "Anubhav","Kumar"
Anubhav Kumar
>>> print 2 > 3


