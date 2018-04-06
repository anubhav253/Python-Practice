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