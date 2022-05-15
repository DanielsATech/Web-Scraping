import requests
from bs4 import BeautifulSoup



resq = requests.get('https://en.wikipedia.org/wiki/Python.html')
print("Status code is", resq.status_code)

data = BeautifulSoup(resq.text, "html5lib")
print(data.title)
print(data.find_all('div'))