#Author: Jack Schwarz
#Date 6/5/2020
#Version: 0.0.1

import requests
import io
from bs4 import BeautifulSoup
import pandas as pd

teamSelection = ""
url = "https://www.usatoday.com/sports/ncaaf/polls/amway-coaches-poll/"
page = requests.get(url)

def parse_coaches_poll(team):
    dfs = pd.read_html("https://www.usatoday.com/sports/ncaaf/polls/amway-coaches-poll/", header=0)[0]
    print("Coaches Poll:")
    print(dfs[dfs['Team'].str.contains(team)])


while True:
    result = input("What team?")
    parse_coaches_poll(result)