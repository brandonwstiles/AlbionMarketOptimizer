from bs4 import BeautifulSoup
import requests

url = 'https://www.albiononline2d.com/en/item/id/T4_RUNE'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
#[s.extract() for s in content('td')]
info = content.findAll('td')

print(content)