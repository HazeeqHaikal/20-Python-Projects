import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "https://www.codewithtomi.com/"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
title = soup.find_all("h2", {"class": "post-title"})
# filter title to get only content 
count = 1 
t = PrettyTable(["Number", 'Content'])

for i in title:
    t.add_row([count, i.text])
    count += 1

print(t)