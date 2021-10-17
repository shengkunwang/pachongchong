import requests
from lxml import etree
if __name__ =="__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }

    # 爬取页面源码数据
    url = 'https://sh.58.com/ershoufang/'
    page_text=requests.get(url= url,headers = headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//section[@class="list"]/div')
    fp =open('58.txt','w',encoding='utf-8')
    for div in div_list:
        title= div.xpath('.//div[@class="property-price"]/h3/text()')
        title = div.xpath('.//div[@class="property-price"]/p[2]/text()')[0]
        print(title)
        fp.write(title+'\n')

