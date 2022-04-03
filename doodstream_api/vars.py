from bs4 import BeautifulSoup
import requests
import re

###########################################################
################# Fetching Base URL #######################
###########################################################
'''
    Fetching API base url directly from doodstream's API docs
    As doodstream frequently change their API base url, so to fight this issue we fetch it directly from doodstream's API docs
    '''
reqURL = "https://doodstream.com/api-docs"
base_url1 = requests.get(reqURL)
base_url = base_url1.text
soup = BeautifulSoup(base_url, features="lxml")
for div in soup.find('div', attrs={'class': 'd-flex align-items-center code-type px-3'}):
    next_txt = str(div).replace('\n', '')
    final_txt = ' '.join(next_txt.split())

match = re.search('.*?(.*\/)account\/info\?key={your_api_key}', final_txt)
try:
    base_url = match.group(1)
except AttributeError:
    base_url = match

    ##################################
