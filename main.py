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

html_string = """
<table>
  <thead>
    <tr>
      <th>Programming Language</th>
      <th>Creator</th> 
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C</td>
      <td>Dennis Ritchie</td> 
      <td>1972</td>
    </tr>
    <tr>
      <td>Python</td>
      <td>Guido Van Rossum</td> 
      <td>1989</td>
    </tr>
    <tr>
      <td>Ruby</td>
      <td>Yukihiro Matsumoto</td> 
      <td>1995</td>
    </tr>
  </tbody>
</table>
"""

def parse_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response, "html.parser")
    return soup

#result = parse_url(url)

dfs = pd.read_html(url, header=0)[0]
print(dfs)





#print(soup.prettify())

#result = soup.find_all(class_="gnt_sp_pl_tbl")


#for elem in result:
#    elemPrint = elem.find('td', class_= "gnt_sp_td")
#    print(elem.text, end='\n'*2)
#   print('\n')

#print("What team would you like the ranking for?")



#while True:
#    choice = input("Enter Team Name:")
#    print("Getting info for " + choice + "...")
#    break