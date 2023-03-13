# Scrapper which can create a json file for all valid url present on given input url


# import all required libraries

import requests
from bs4 import BeautifulSoup
import json
import validators

# parsing url to get document
url = input("URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# scrapping all links on the url
links = soup.find_all('a')

# Checking for valid links 
valid_links = []
for link in links:
    # to check if the link is a None
    if link.get('href') is not None:
        # to check if the link is a valid URL
        if validators.url(link.get('href')):
            valid_links.append(link.get('href'))
    
# Writting all urls in json file     
with open('sitemap.json', 'w') as f:
   json.dump(valid_links, f)


#Scrapper for every url in json file, all the data scrapped will be stored in txt file


with open('sitemap.json', 'r') as f:
  sitemap = json.load(f)

for link in sitemap:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    # title without icluding tags 
    title = soup.title.string
    # content with tags
    p = soup.find_all('p')
    h1 = soup.find_all('h1')
    h2 = soup.find_all('h2')
    h3 = soup.find_all('h3')
    h4 = soup.find_all('h4')
    h5 = soup.find_all('h5')
    h6 = soup.find_all('h6')
    a = soup.find_all('a')

    # we can easily scrap anything by defining any tags

    # writing all title in a text file 
    with open('file.txt', 'w') as file:
        file.write(title)
        file.write("/n")
        file.close()



    
 
