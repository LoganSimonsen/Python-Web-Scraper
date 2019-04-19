# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
site = 'https://floridaman.com/'

hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site, headers=hdr)

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(req)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# iterate through elements and build new HTML element with href
# for a in soup.find_all('a', rel='bookmark'):
#     print("<li><a target='_blank' href='" +
#           a['href']+"'>"+a.text+"</a></li><hr>")

for a in soup.find_all('a', rel='bookmark'):
    print(str(a)+"<hr>")
