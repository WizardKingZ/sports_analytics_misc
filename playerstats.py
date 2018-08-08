from bs4 import BeautifulSoup
import requests
import os
from constants import *

## this script is example to get single player seasonal stat by passing players info

fileName = 'stat.txt'

output = open(fileName, 'w')

#url = r"http://espn.go.com/nba/player/stats/_/id/2745/brandon-bass"
url = r"http://espn.go.com/nba/player/stats/_/id/2745/seasontype/3/brandon-bass"

r = requests.get(url)
soup = BeautifulSoup(r.text)

# get player bio
def getBio():
    bio_table = soup.find('div', class_=BIO)
    #print table.prettify()

    info_lookUp = [INFO, METADATA+SPACE+FLOAT_LEFT]

    for item in info_lookUp:
        ul = bio_table.find('ul', class_=item)
        lst = ul.find_all('li')
        for each in lst:
            span = each.find('span')
            if not span == None:
                print span.text
                print each.text.split(span.text)[1]
            else:
                print each.text


stats_string = [TITLE+SPACE+PLAYER_STAT, CONTAINER+SPACE+TABLE+SPACE+M_PLAYER_STAT, CONTENT]

player_stat_table = soup.find('div', class_='article')
#print player_stat_table.prettify()
title = player_stat_table.find('div', class_=stats_string[0]).text
print title
# print stats
contents = player_stat_table.find('div', class_=stats_string[1]).find_all('div', stats_string[2])
print len(contents)
counter = 1
for each in contents:
    print counter
    #result = ''
    #print '------------------------------'
    #print '------------------------------'
    trs = each.find_all('tr')
    print len(trs)
    for eachRow in trs:
        #row = ''
        #print eachRow.prettify()
        tds = eachRow.find_all('td')
        print len(tds)
        for eachCol in tds:
            output.write(eachCol.text + '\t')
        #row+= row + eachCol.text + '\t'
        output.write('\n')
    output.write('\n')
    counter = counter + 1

output.close()
#print row