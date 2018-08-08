import copper
import pandas as pd
import requests
from bs4 import BeautifulSoup
#copper.project.path = '../../'


def find_all(sport):
    url = 'http://espn.go.com/'+sport+'/teams'
    r = requests.get(url)

    soup = BeautifulSoup(r.text)
    tables = soup.find_all('ul', class_='medium-logos')

    teams = []
    teams_urls = []
    prefix_1 = []
    prefix_2 = {}
    for table in tables:
        lis = table.find_all('li')
        for li in lis:
            info = li.h5.a
            teams.append(info.text)
            url = info['href']
            teams_urls.append(url)
            prefix_1.append(url.split('/')[-2])
            prefix_2[url.split('/')[-2]] = url.split('/')[-1]


    dic = {'url': teams_urls, 'prefix_2': prefix_2, 'prefix_1': prefix_1, 'info': teams}
    return dic



