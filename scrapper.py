# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 00:04:18 2018

@author: DEVIL
"""

#scrapping table from website

import urllib2
#specify url
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
#Return html to variable page
page = urllib2.urlopen(url)
#using beautifulsoup to fetching data
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
#finding table in url
right = soup.find('table', class_ = 'table')
#empty list to store data in table
A = []
B = []
C = []
D = []
E = []

for row in right.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].find(text=True))
        B.append(cells[1].text.strip())
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))

#storing columns in a dataframe
import pandas as pd
df = pd.DataFrame(A,columns=['Pos'])
df['Team']=B
df['Matches']=C
df['Points']=D
df['Rating']=E