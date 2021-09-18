import requests
import bs4

result = requests.get("https://www.ebay.com.au/itm/164376839971?epid=17040739296&hash=item26459f8723:g:HF4AAOSwu4lg5TBX",verify=False)

#print the result
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)

'''
from requests_html import HTMLSession
session = HTMLSession()
given_url = "https://www.ebay.com.au/itm/164376839971?epid=17040739296&hash=item26459f8723:g:HF4AAOSwu4lg5TBX"
r = session.get(url=given_url)
print(r)
print (r.html)

#print(f'{len(items)} Results Found for: {given_url}')
'''
