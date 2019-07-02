"""
    Crawl information from https://www.tianqi.com/xujiahui/
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime

Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

webpage = requests.get('https://www.tianqi.com/xujiahui/', headers=Headers)
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
