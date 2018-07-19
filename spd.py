import urllib.request
from lxml import etree

url = 'https://www.xin.com/xian/sn_v21/h/'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}

req = urllib.request.Request(url=url,headers=headers)
resp  = urllib.request.urlopen(req)

html = resp.read().decode()

html_1 = etree.HTML(html)

lujing = html_1.xpath('//a[@class="aimg"]/img/@data-original')
lujing1 = html_1.xpath('//a[@class="aimg"]/@title')

  # 车辆信息

with open(r'./title_1.txt', 'w') as f:
        for a in lujing1:
            f.write(a + '\n')
