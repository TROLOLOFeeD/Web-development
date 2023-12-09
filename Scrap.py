from cgitb import text
from os import name
import requests
import lxml
import sqlite3
from bs4 import BeautifulSoup

class Group:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def name(self):
        print(name)
        print(num)

GList = list()

print("Just wait a minute")
def main():
    url = "https://www.istu.edu/schedule/"
    try:
        response = requests.get(url)
        doc = BeautifulSoup(response.text, 'lxml')
        links = doc.select("ul a")
        for link in links:
            href = link['href']
            # Разбиваем строку href на параметры
            params = href.split("?")
            if len(params) == 2:
                keyValuePairs = params[1].split("&")
                for pair in keyValuePairs:
                    keyValue = pair.split("=")
                    if len(keyValue) == 2 and keyValue[0] == "subdiv":
                        subdivValue = keyValue[1]
                        url2 = f"https://www.istu.edu/schedule/?subdiv={subdivValue}"
                        try:
                            # Получаем HTML-код страницы
                            response2 = requests.get(url2)
                            doc2 = BeautifulSoup(response2.text, 'html.parser')
                            # Находим все теги <a> внутри страницы
                            links2 = doc2.select("a[href]")
                            # Итерируемся по найденным ссылкам
                            for link2 in links2:
                                href2 = link2['href']
                                group_name = link2.text
                                # Проверяем, содержит ли href атрибут "group"
                                if "group=" in href2:
                                    groupValue = href2.split("group=")[1].split("&")[0]
                                    # group="$text $groupValue"
                                    GList.append(Group(group_name, groupValue))
                        except Exception as e:
                            print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

print ("Enter group name")
name = input()
for d in range (len(GList)):
    if name == GList[d].name:
        num = GList[d].num
url = f"https://www.istu.edu/schedule/?group={num}"
response = requests.get(url)
if response.status_code == 200:
    print('Request complete succesfully')
soup = BeautifulSoup(response.content, 'lxml')
days = soup.find_all('h3', class_='day-heading')
times = soup.find_all('div', class_='class-time')
infos = soup.find_all('div', class_='class-info')
preds = soup.find_all('div', class_='class-pred')
#for day in days:
#    day.text
    #print(day)
c_day = [tmp.text for tmp in days]
t = 0
for d in range(len(days)):
    print(c_day[d])

    #for t in range(len(times)):
    #    if (times[t].text>times[t+1].text):
    #        print (times[t].text)
    #    else:
    #        break

    
    #for k in range(len(times)):
    #    print(times[k].text)
    #    print (infos[j].text)
    #    j += 1
    #    print(preds[i*len(times)+k].text)
    #    print(infos[j].text)

#for i in range(len(times)):
#    print(times[i].text, " times ", i)
#for i in range(len(infos)):
#    print(infos[i].text, " info ", i)
#for i in range(len(preds)):
#    print(preds[i].text, " ][uy ", i)