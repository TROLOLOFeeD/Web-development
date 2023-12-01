from os import name
import requests
import lxml
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
for i in range (len(GList)):
    if name == GList[i].name:
        num = GList[i].num
url = f"https://www.istu.edu/schedule/?group={num}"
response = requests.get(url)
if response.status_code == 200:
    print('Request complete succesfully')
soup = BeautifulSoup(response.content, 'lxml')
days = soup.find_all('h3', class_='day-heading')
times = soup.find_all('div', class_='class-time')
infos = soup.find_all('div', class_='class-info')
preps = soup.find_all('a')
preds = soup.find_all('div', class_='class-pred')
#for day in days:
#    day.text
    #print(day)
c_day = [blyat.text for blyat in days]
for i in range(len(days)):
    print(c_day[i])
    for i in range(len(times)):
        print(times[i].text)
        print(infos[i].text, ' ', preps[i].text)
        print(preds[i].text)
        i += 1
        print(infos[i].text)

        