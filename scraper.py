import requests
from bs4 import BeautifulSoup


resq = requests.get('https://en.wikipedia.org/wiki/Python.html')


data = BeautifulSoup(resq.text, "html5lib")
print(data.title)
print("Status code is", resq.status_code)

inputd = input("Enter the data you wish to find: ")
datavar = data.find_all(inputd)

def WriteData():

    with open('parserdata.txt', "w") as myfile:
            fi = myfile
            fi.write(str(datavar))
            fi.close()
            print("Data has been recorded")


WriteData()


