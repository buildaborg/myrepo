# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:56:19 2023

@author: mckeo
"""

import urllib.request

from pprint import pprint

from html_table_parser.parser import HTMLTableParser

import pandas as pd
Link = 'https://www.hockey-reference.com/players/m/mcdavco01.html'

#opens a website and reads binary response (HTML contents)
def url_get_contents(targeturl):
    
    #make requets to website
    req = urllib.request.Request(targeturl)
    f = urllib.request.urlopen(req)
    #reading contents of the website
    return f.read()

#DEFINE HTML CONTENTS OF A URL    
xhtml = url_get_contents(Link).decode('utf-8')
#defining the HTMLTableParser object
p = HTMLTableParser()
#feeding the html content in the HTMLTableParser object
p.feed(xhtml)
#now obtaining the data of the table required

#pprint(p.tables[0])
print('\n\nPANDAS DATAFRAME\n')
print(pd.DataFrame(p.tables))

tables = pd.read_html(Link)
pprint(tables)

