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

def parse_cbs_poll(team):
    dfs = pd.read_html("https://www.cbssports.com/college-football/rankings/", header=0)[2]
    print("CBSSports 130:")
    print(dfs[dfs['Team'].str.contains(team)])

def parse_rcfb_poll(team):
    dfs = pd.read_html("https://poll.redditcfb.com/", header=0)[0]
    print("r/CFB Poll:")
    print(dfs[dfs['Team'].str.contains(team)])

def parse_all_polls(team):
    parse_coaches_poll(team)
    parse_cbs_poll(team)
    parse_rcfb_poll(team)

while True:
    result = input("What team?")
    parse_all_polls(result)
