from bs4 import BeautifulSoup
import requests
import teams
from constants import *

def getStats(city, name, sports):
	url = ESPN+sports+'/team/stats/_/name/'+city+SLASH+name
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
		
	#print(soup.prettify())

	tables = soup.find_all('div', class_ =CONTAINER+SPACE+LEADERS)

	table = tables[0]

	categories = table.find_all('div', class_=CONTAINER+SPACE+STAT)
	print '--------------------------'
	print city +  '  ' + name + '      ' + sports
	print '--------------------------'
	for each in categories:
		each.find('div', class_=HEADER)
		print each.find('h4').text

		lis = each.find_all('li')
		for li in lis:
			print li.text

# getMoney function could be replaced by getTeamStats
def getMoney(city, name, sports, stat_type, stat_subtype, season):
    players = {}
    url =ESPN+sports+'/team/'+stat_type+'/_/name/'+city +SLASH+name
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    div1 = soup.find_all('div', class_=CONTAINER+SPACE+TABLE+SPACE+BODY)
    div2 = div1[0].find('div' ,class_=CONTENT)
    t = div2.find('table', class_=HEAD)
    rows = t.find_all('tr')
    counter = 1
    for item in rows:
        col = item.find_all('td')
        s = ''
        subcounter = 1
        for attr in col:
            if subcounter == 2 and counter > 2:
                players[attr.text] = attr.a['href']
            s += attr.text + '\t'
            subcounter = subcounter + 1
        counter = counter + 1
    return players

def getTeamStats(city, name, sports, stat_type, stat_subtype, season):
    fileName = city+'_'+name+'_'+sports+'_'+stat_type+'_'+stat_subtype+'_'+ season.replace('/', '_')+'.txt'
    output = open(fileName, 'w')
    url =ESPN+sports +'/team/'+stat_type+'/_/name/'+city +SLASH +season+name
    print url
    r = requests.get(url)
    soup = BeautifulSoup(r.text.decode('utf-8','ignore'))

    div = soup.find_all('div', class_=CONTENT)

    for each in div:
        trs = each.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            for td in tds:
                print td.text
                text = td.text
                if text != u'\xa0':
                    output.write(text+'\t')
                elif text == u'\xa0':
                    output.write('\t')
            output.write('\n')
        output.write('\n')
    output.close()

def getAll(sports):
    a = teams.find_all(sports)
    bundle = a['prefix_2']
    allTeams = {}
    for each in bundle:
        #getStats(each, bundle[each], sports)
        allTeams[bundle[each]] = getMoney(each, bundle[each], sports, '', '', '')
    return allTeams

#teams = getAll('nba')
#print teams

getTeamStats('bos', 'boston-red-sox', 'mlb', TEAM_STAT_TYPE_LIST[0], '', '2013')
