# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:56:19 2023

@author: mckeo
"""
from bs4 import BeautifulSoup
import urllib.request, csv, re

from pprint import pprint

#from html_table_parser.parser import HTMLTableParser
from html.parser import HTMLParser

import pandas as pd
Link = 'https://www.hockey-reference.com/leagues/NHL_2023_skaters.html'

#opens a website and reads binary response (HTML contents)
def url_get_contents(targeturl):
    
    #make requets to website
    req = urllib.request.Request(targeturl)
    f = urllib.request.urlopen(req)
    #reading contents of the website
    return f.read()

#DEFINE HTML CONTENTS OF A URL    
xhtml = url_get_contents(Link).decode('utf-8')

'''
#defining the HTMLTableParser object
p = HTMLTableParser()
#feeding the html content in the HTMLTableParser object
p.feed(xhtml)
#now obtaining the data of the table required

#pprint(p.tables[0])
print('\n\nPANDAS DATAFRAME\n')
print(pd.DataFrame(p.tables[0]))

tablename = pd.read_html(Link)
pprint(tablename[0])

outputFile = 'D:/ScrapingTest.csv'
CSV = open(outputFile, 'w', newline = '')

writer = csv.writer(CSV)

writer.writerows(p.tables[0])
CSV.close()
'''
pz = HTMLParser()
parsed_obj = pz.feed(xhtml)
print(parsed_obj)

tsn_game_summary = 'https://www.tsn.ca/nhl/event/winnipeg-jets-toronto-maple-leafs-20230119?event_id=196081'
tsnlink = url_get_contents(tsn_game_summary)
soup2 = BeautifulSoup(tsnlink, 'lxml')
#beautfil soup links

req2 = urllib.request.Request(Link)
html_page = urllib.request.urlopen(req2)
soup = BeautifulSoup(html_page, 'lxml')

links = []
for link in soup.find_all('a'):
    
    links.append(link.get('href'))
    
print(links)

divs = []
for div in soup2.find_all('div'):
    divs.append(div.get('div class = "bms-event-advanced-stats__shots-container"'))

print(divs)






divs = soup.find_all("div", {'class':'cell'})


'''
#scoring location is in <div class="bms-event-advanced-stats__shots-container"><span title="Kyle Connor
Goal - 4:00 - 3rd" class="bms-event-advanced-stats__shot bms-event-advanced-stats__shot--goal" style="left: 82.3529%; top: 22.4719%;"></span><span title="Josh Morrissey
Shot On Goal - 18:50 - 1st" class="bms-event-advanced-stats__shot" style="left: 41.1765%; top: 65.1685%;"></span><span title="Morgan Barron
Shot On Goal - 18:47 - 1st" class="bms-event-advanced-stats__shot" style="left: 47.0588%; top: 13.4831%;"></span><span title="Neal Pionk
Shot On Goal - 17:37 - 1st" class="bms-event-advanced-stats__shot" style="left: 85.8824%; top: 65.1685%;"></span><span title="Mark Scheifele
Shot On Goal - 12:28 - 1st" class="bms-event-advanced-stats__shot" style="left: 69.4118%; top: 35.9551%;"></span><span title="Neal Pionk
Shot On Goal - 8:17 - 1st" class="bms-event-advanced-stats__shot" style="left: 69.4118%; top: 64.0449%;"></span><span title="Josh Morrissey
Shot On Goal - 5:35 - 1st" class="bms-event-advanced-stats__shot" style="left: 10.5882%; top: 42.6966%;"></span><span title="Mark Scheifele
Shot On Goal - 18:48 - 1st" class="bms-event-advanced-stats__shot" style="left: 48.2353%; top: 10.1124%;"></span><span title="Kevin Stenlund
Shot On Goal - 17:08 - 1st" class="bms-event-advanced-stats__shot" style="left: 52.9412%; top: 38.2022%;"></span><span title="Neal Pionk
Shot On Goal - 12:20 - 1st" class="bms-event-advanced-stats__shot" style="left: 91.7647%; top: 25.8427%;"></span><span title="Pierre-Luc Dubois
Shot On Goal - 8:40 - 1st" class="bms-event-advanced-stats__shot" style="left: 54.1176%; top: 7.86517%;"></span><span title="Pierre-Luc Dubois
Shot On Goal - 8:38 - 1st" class="bms-event-advanced-stats__shot" style="left: 50.5882%; top: 10.1124%;"></span><span title="Pierre-Luc Dubois
Shot On Goal - 8:36 - 1st" class="bms-event-advanced-stats__shot" style="left: 49.4118%; top: 8.98876%;"></span><span title="Kyle Connor
Shot On Goal - 8:21 - 1st" class="bms-event-advanced-stats__shot" style="left: 80%; top: 35.9551%;"></span><span title="Nikolaj Ehlers
Shot On Goal - 6:03 - 1st" class="bms-event-advanced-stats__shot" style="left: 68.2353%; top: 41.573%;"></span><span title="Pierre-Luc Dubois
Shot On Goal - 5:13 - 1st" class="bms-event-advanced-stats__shot" style="left: 77.6471%; top: 43.8202%;"></span><span title="Neal Pionk
Shot On Goal - 0:50 - 1st" class="bms-event-advanced-stats__shot" style="left: 70.5882%; top: 43.8202%;"></span><span title="Morgan Barron
Shot On Goal - 14:01 - 2nd" class="bms-event-advanced-stats__shot" style="left: 8.23529%; top: 23.5955%;"></span><span title="Kyle Connor
Shot On Goal - 19:18 - 2nd" class="bms-event-advanced-stats__shot" style="left: 80%; top: 11.236%;"></span><span title="Josh Morrissey
Shot On Goal - 19:14 - 2nd" class="bms-event-advanced-stats__shot" style="left: 17.6471%; top: 66.2921%;"></span><span title="Neal Pionk
Shot On Goal - 8:17 - 2nd" class="bms-event-advanced-stats__shot" style="left: 61.1765%; top: 53.9326%;"></span><span title="Mark Scheifele
Shot On Goal - 4:26 - 2nd" class="bms-event-advanced-stats__shot" style="left: 68.2353%; top: 33.7079%;"></span><span title="Brenden Dillon
Shot On Goal - 3:59 - 2nd" class="bms-event-advanced-stats__shot" style="left: 25.8824%; top: 65.1685%;"></span><span title="Cole Perfetti
Shot On Goal - 2:54 - 2nd" class="bms-event-advanced-stats__shot" style="left: 70.5882%; top: 59.5506%;"></span><span title="Neal Pionk
Shot On Goal - 2:38 - 2nd" class="bms-event-advanced-stats__shot" style="left: 38.8235%; top: 37.0787%;"></span><span title="Kyle Connor
Shot On Goal - 0:44 - 2nd" class="bms-event-advanced-stats__shot" style="left: 36.4706%; top: 31.4607%;"></span><span title="Nikolaj Ehlers
Shot On Goal - 0:36 - 2nd" class="bms-event-advanced-stats__shot" style="left: 34.1176%; top: 34.8315%;"></span><span title="Kyle Connor
Shot On Goal - 17:21 - 3rd" class="bms-event-advanced-stats__shot" style="left: 61.1765%; top: 37.0787%;"></span><span title="Pierre-Luc Dubois
Shot On Goal - 16:23 - 3rd" class="bms-event-advanced-stats__shot" style="left: 47.0588%; top: 13.4831%;"></span><span title="Kyle Connor
Shot On Goal - 13:24 - 3rd" class="bms-event-advanced-stats__shot" style="left: 49.4118%; top: 23.5955%;"></span><span title="Axel Jonsson-Fjallby
Shot On Goal - 0:32 - 3rd" class="bms-event-advanced-stats__shot" style="left: 11.7647%; top: 43.8202%;"></span><span title="Mark Scheifele
Shot On Goal - 17:00 - 3rd" class="bms-event-advanced-stats__shot" style="left: 41.1765%; top: 8.98876%;"></span><span title="Sam Gagner
Shot On Goal - 14:30 - 3rd" class="bms-event-advanced-stats__shot" style="left: 75.2941%; top: 1.1236%;"></span><span title="Nikolaj Ehlers
Shot On Goal - 12:27 - 3rd" class="bms-event-advanced-stats__shot" style="left: 50.5882%; top: 37.0787%;"></span><span title="Axel Jonsson-Fjallby
Shot On Goal - 10:26 - 3rd" class="bms-event-advanced-stats__shot" style="left: 48.2353%; top: 86.5169%;"></span><span title="Nikolaj Ehlers
Shot On Goal - 5:41 - 3rd" class="bms-event-advanced-stats__shot" style="left: 75.2941%; top: 32.5843%;"></span><span title="Josh Morrissey
Shot On Goal - 5:32 - 3rd" class="bms-event-advanced-stats__shot" style="left: 91.7647%; top: 28.0899%;"></span><span title="Josh Morrissey
Shot On Goal - 4:58 - 3rd" class="bms-event-advanced-stats__shot" style="left: 44.7059%; top: 64.0449%;"></span></div>

<div class="bms-event-advanced-stats__shots-container"><span title="Mitchell Marner
Goal - 13:49 - 2nd" class="bms-event-advanced-stats__shot bms-event-advanced-stats__shot--goal" style="left: 34.1176%; top: 24.7191%;"></span><span title="Auston Matthews
Goal - 0:08 - 2nd" class="bms-event-advanced-stats__shot bms-event-advanced-stats__shot--goal" style="left: 29.4118%; top: 37.0787%;"></span><span title="Auston Matthews
Goal - 3:47 - 2nd" class="bms-event-advanced-stats__shot bms-event-advanced-stats__shot--goal" style="left: 50.5882%; top: 28.0899%;"></span><span title="Mark Giordano
Goal - 17:33 - 3rd" class="bms-event-advanced-stats__shot bms-event-advanced-stats__shot--goal" style="left: 52.9412%; top: 15.7303%;"></span><span title="Auston Matthews
Shot On Goal - 7:11 - 1st" class="bms-event-advanced-stats__shot" style="left: 40%; top: 31.4607%;"></span><span title="William Nylander
Shot On Goal - 3:56 - 1st" class="bms-event-advanced-stats__shot" style="left: 31.7647%; top: 19.1011%;"></span><span title="William Nylander
Shot On Goal - 19:21 - 1st" class="bms-event-advanced-stats__shot" style="left: 77.6471%; top: 29.2135%;"></span><span title="Auston Matthews
Shot On Goal - 15:56 - 1st" class="bms-event-advanced-stats__shot" style="left: 50.5882%; top: 13.4831%;"></span><span title="Mark Giordano
Shot On Goal - 14:08 - 1st" class="bms-event-advanced-stats__shot" style="left: 21.1765%; top: 3.37079%;"></span><span title="Bobby McMann
Shot On Goal - 12:36 - 1st" class="bms-event-advanced-stats__shot" style="left: 15.2941%; top: 2.24719%;"></span><span title="John Tavares
Shot On Goal - 18:55 - 2nd" class="bms-event-advanced-stats__shot" style="left: 24.7059%; top: 48.3146%;"></span><span title="Morgan Rielly
Shot On Goal - 13:29 - 2nd" class="bms-event-advanced-stats__shot" style="left: 90.5882%; top: 19.1011%;"></span><span title="Morgan Rielly
Shot On Goal - 10:44 - 2nd" class="bms-event-advanced-stats__shot" style="left: 14.1176%; top: 51.6854%;"></span><span title="Bobby McMann
Shot On Goal - 9:02 - 2nd" class="bms-event-advanced-stats__shot" style="left: 64.7059%; top: 59.5506%;"></span><span title="Morgan Rielly
Shot On Goal - 7:51 - 2nd" class="bms-event-advanced-stats__shot" style="left: 12.9412%; top: 64.0449%;"></span><span title="Mark Giordano
Shot On Goal - 7:14 - 2nd" class="bms-event-advanced-stats__shot" style="left: 16.4706%; top: 62.9213%;"></span><span title="Zach Aston-Reese
Shot On Goal - 5:04 - 2nd" class="bms-event-advanced-stats__shot" style="left: 24.7059%; top: 33.7079%;"></span><span title="Calle Jarnkrok
Shot On Goal - 18:54 - 3rd" class="bms-event-advanced-stats__shot" style="left: 48.2353%; top: 16.8539%;"></span><span title="David Kampf
Shot On Goal - 18:08 - 3rd" class="bms-event-advanced-stats__shot" style="left: 20%; top: 56.1798%;"></span><span title="Auston Matthews
Shot On Goal - 10:44 - 3rd" class="bms-event-advanced-stats__shot" style="left: 47.0588%; top: 52.809%;"></span><span title="Calle Jarnkrok
Shot On Goal - 9:53 - 3rd" class="bms-event-advanced-stats__shot" style="left: 27.0588%; top: 34.8315%;"></span><span title="Bobby McMann
Shot On Goal - 9:18 - 3rd" class="bms-event-advanced-stats__shot" style="left: 37.6471%; top: 12.3596%;"></span><span title="Bobby McMann
Shot On Goal - 7:01 - 3rd" class="bms-event-advanced-stats__shot" style="left: 23.5294%; top: 38.2022%;"></span><span title="Pierre Engvall
Shot On Goal - 5:53 - 3rd" class="bms-event-advanced-stats__shot" style="left: 63.5294%; top: 11.236%;"></span><span title="Auston Matthews
Shot On Goal - 4:38 - 3rd" class="bms-event-advanced-stats__shot" style="left: 69.4118%; top: 42.6966%;"></span><span title="Auston Matthews
Shot On Goal - 4:37 - 3rd" class="bms-event-advanced-stats__shot" style="left: 57.6471%; top: 4.49438%;"></span><span title="Alexander Kerfoot
Shot On Goal - 0:44 - 3rd" class="bms-event-advanced-stats__shot" style="left: 20%; top: 38.2022%;"></span></div>
'''