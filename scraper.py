import requests
from bs4 import BeautifulSoup




resq = requests.get('https://en.wikipedia.org/wiki/Python.html')
print("Status code is", resq.status_code)

data = BeautifulSoup(resq.text, "html5lib")
print(data.title)


datavar = data.find_all("div")



def WriteData():
    fi = open("parserdata4.txt", "x")
    fi.write(str(datavar))
    fi.close()
    print("Txt has been made")

WriteData()

