# Tests to see if a page is up/link works.

import requests, urllib, bs4

internal_links = []
external_links = []

def testLink(linksList):
    for l in linksList:
        linktesting = requests.get(l, headers={'User-Agent': 'Mozilla/5.0'})
        try:     # put this try block in so it won't crash
            linktesting.raise_for_status()
        except Exception as exc:     # throws exception
            print('Dead link found!\n%s' % (exc))


url = 'https://ls1tech.com/'
page = requests.get(url)
linkSoup = bs4.BeautifulSoup(page.text,'html.parser')

for atag in linkSoup.findAll("a"):
    link = atag.attrs.get("href")
    if link == "" or link is None:
        continue
    if link[:4] == "http":
        # External
        if link not in external_links:
            external_links.append(link)
    else:
        # Internal
        if link[0] != "/":
            link = "/"+link
        if link not in internal_links:
            internal_links.append(url+link)

print("Testing internal links..")
testLink(internal_links)
print("Testing external links..")
testLink(external_links)