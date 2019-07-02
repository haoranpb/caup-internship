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

wind_dict = {
    '0级': '0.0-0.2',
    '1级': '0.3-1.5',
    '2级': '1.6-3.3',
    '3级': '3.4-5.4',
    '4级': '5.5-7.9',
    '5级': '8.0-10.7',
    '6级': '10.8-13.8',
    '7级': '13.9-17.1'
}

webpage = requests.get('https://www.tianqi.com/xujiahui/', headers=Headers)
soup = BeautifulSoup(webpage.text, 'lxml')
element = soup.find('dd', attrs={'class': 'shidu'}).text
temperature = next(soup.find('p', attrs={'class': 'now'}).children).text
pm = soup.find('dd', attrs={'class': 'kongqi'}).text

index_1 = element.find('湿度')
index_2 = element.find('风向')
index_3 = element.find('紫外线')

humidity = element[index_1 + 3: index_2 - 1]
wind = element[index_2 + 3: index_3]
ray = element[index_3 + 4: ]
wind_direction, wind_speed = wind.split()

index_1 = pm.find('PM')
index_2 = pm.find('日出')
pm = pm[index_1 + 4: index_2]

with open('./xuhui.txt', 'w', encoding='utf-8') as file:
    file.write('PM2.5(ug/m3) ' + pm + '\n')
    file.write('环境湿度(%) ' + humidity + '\n')
    file.write('空气温度(℃) ' + temperature + '\n')
    file.write('风向(度) ' + wind_direction + '\n')
    file.write('风速(m/s) ' + wind_dict[wind_speed])