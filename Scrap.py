from ast import List
from urllib import response
import lxml
import requests
from bs4 import BeautifulSoup
import sqlite3

#class for link id group with group name
class Group:
	def __init__(self, name, num):
		self.name = name
		self.num = num
	def name(self):
		print(name)
		print(num)

GList = list()
#fillin group list
def main():
	url = "https://www.istu.edu/schedule/"
	try:
		response = requests.get(url)
		doc = BeautifulSoup(response.text, 'lxml')
		links = doc.select("ul a")
		for link in links:
			href = link['href']
			# split the href line into parameters
			params = href.split("?")
			if len(params) == 2:
				keyValuePairs = params[1].split("&")
				for pair in keyValuePairs:
					keyValue = pair.split("=")
					if len(keyValue) == 2 and keyValue[0] == "subdiv":
						subdivValue = keyValue[1]
						url2 = f"https://www.istu.edu/schedule/?subdiv={subdivValue}"
						try:
							# gettin HTML-code of page
							response2 = requests.get(url2)
							doc2 = BeautifulSoup(response2.text, 'html.parser')
							# searchin all <a> selectors on a page
							links2 = doc2.select("a[href]")
							# iterate through found links
							for link2 in links2:
								href2 = link2['href']
								group_name = link2.text
								# checkin if the href contains "group" attribute
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
#input group name and searchin its id
name = input()
for d in range (len(GList)):
    if name == GList[d].name:
        num = GList[d].num
url = f"https://www.istu.edu/schedule/?group={num}"
#gettin group schedule
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
days = soup.find_all('h3', class_='day-heading')
it = soup.find_all('div', class_='class-lines')
items = soup.find_all('div', class_='class-line-item')
#create database with schedule
conn = sqlite3.connect('schedule.db')
cursor = conn.cursor()
conn.commit()
# cursor.execute("DROP TABLE schedule;")

cursor.execute('''
	CREATE TABLE IF NOT EXISTS schedule (
		id INTEGER PRIMARY KEY,
		day TEXT,
		time_id TEXT,
		subject TEXT,
		room TEXT,
		info TEXT)
	''')
#selecting the necessary elements (i need to separate double pairs)
for item in items:
	subject = item.find('div', class_='class-pred').text
	info = item.find('div', class_='class-info').text
	room = item.find('div', class_='class-aud').text
	#fillin the database
	cursor.execute('''INSERT INTO schedule (subject, room, info)
		VALUES (?, ?, ?)
		''', (subject, room, info))
#also fillin the db with days (also i need pack days by their pairs)
for day in days:
	cursor.execute('''INSERT INTO schedule (day)
		VALUES (?)
		''', (day.text,))

#save an close db
conn.commit()
conn.close()