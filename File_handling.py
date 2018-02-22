Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fp = open("demo.txt")

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fp = open("demo.txt")
IOError: [Errno 2] No such file or directory: 'demo.txt'
>>> import os
>>> os.getcwd()
'C:\\Python27'
>>> fp = open("demo.txt")

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fp = open("demo.txt")
IOError: [Errno 2] No such file or directory: 'demo.txt'
>>> fp = open("demo.txt")
>>> type(fp)
<type 'file'>
>>> fp.read()
'Forsk techno\nJECRC\ncse\nit\n'
>>> print fp
<open file 'demo.txt', mode 'r' at 0x05943180>
>>> fp.read("r")

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fp.read("r")
TypeError: an integer is required
>>> fp.read(r)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fp.read(r)
NameError: name 'r' is not defined
>>> fp.seek(0,0)
>>> fp.readline()
'Forsk techno\n'
>>> fp.readline()
'JECRC\n'
>>> fp.seek(0,0)
>>> fp.readline()
'Forsk techno\n'
>>> fp.readlines()
['JECRC\n', 'cse\n', 'it\n']
>>> fp.close()
>>> fp = open("demo1.txt", 'w')
>>> fp.write("Machine Learning in JECRC")
>>> fp.close()
>>> fp = open("demo.txt")
>>> 
>>> for line in fp:
	print line

Forsk techno

JECRC

cse

it

>>> import numpy

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import numpy
ImportError: No module named numpy
>>> import pandas

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import pandas
ImportError: No module named pandas
>>> import numpy
>>> import pandas
>>> from datetime import time
>>> import urllib
>>> import sklearn

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    import sklearn
ImportError: No module named sklearn
>>> import zlib
>>> import zipfile
>>> import zipfile
>>> import numpy
>>> import numpy
>>> import datetime
>>> time
<type 'datetime.time'>
>>> datetime.time
<type 'datetime.time'>
>>> a = datetime.time
>>> a
<type 'datetime.time'>
>>> currenDate = now.strftime("%Y-%m-%d")

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    currenDate = now.strftime("%Y-%m-%d")
NameError: name 'now' is not defined
>>> now = datetime.datetime.now()
>>> currenDate = now.strftime("%Y-%m-%d")
>>> currentDate

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    currentDate
NameError: name 'currentDate' is not defined
>>> currenDate
'2018-02-13'
>>> datetime.time
<type 'datetime.time'>
>>> import datetime
>>> ex = datetime.datetime.now()
>>> ex = ex + datetime.timedelta(minutes=30)
>>> response.set_cookie(key, guid, expires=ex)

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    response.set_cookie(key, guid, expires=ex)
NameError: name 'response' is not defined
>>> 
