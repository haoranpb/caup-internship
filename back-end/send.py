import json
import requests


Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}
form_data = {
    'UserName': 'jllot',
    'UserPassword': 'jllot12345',
    'returnUrl': '',
    'RememberMe': 'true',
    'RememberMe': 'false'
}

s = requests.Session()

# 获取气象站 cookie
r = s.get('http://cloud.ssiot.com/Login/jlst', headers=Headers)
r = s.post('http://cloud.ssiot.com/Login/jlst', data=form_data, headers=Headers)
# 获取气象站数据
r = s.get('http://cloud.ssiot.com/Ajax/Get/AjaxGetJsonLastDataByNodenolist.ashx?filter=GetLastDataByNodenolistalarm&nodenos=1866', headers=Headers)
datas = json.loads(r.text)

direction = ''
speed = ''
for data in datas['Rows']:
    if data['ShortName'] == '风向':
        direction = data['Data']
    elif data['ShortName'] == '风速':
        speed = data['Data']
    else:
        pass

requests.get('http://www.wf-bldgtech.com/wdata_check2.php? \
    id=WFupload&pw=m23dwq&nid=5&wspeed=' + str(speed) + '&direct=' + str(direction))
# http://www.wf-bldgtech.com/wdata_check2.php?id=WFupload&pw=m23dwq&nid=7&wspeed=1.3&direct=2
