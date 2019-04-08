"""
    Crawl information from https://www.tianqi.com/xujiahui/
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime

webpage = requests.get('https://www.tianqi.com/xujiahui/')
soup = BeautifulSoup(webpage.text, 'lxml')
element = soup.find('dd', attrs={'class': 'shidu'}).text
temperature = next(soup.find('p', attrs={'class': 'now'}).children).text

index_1 = element.find('湿度')
index_2 = element.find('风向')
index_3 = element.find('紫外线')

humidity = element[index_1 + 3: index_2]
wind = element[index_2 + 3: index_3]
ray = element[index_3 + 4: ]
with open('./data.txt', 'w', encoding='utf-8') as file:
    file.write(humidity + '\n')
    file.write(wind + '\n')
    file.write(ray + '\n')
    file.write(temperature + '\n')
    file.write(str(datetime.now()) + '\n')
