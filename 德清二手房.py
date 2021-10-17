import requests
from lxml import etree
if __name__ =="__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }

    # 爬取页面源码数据
    url = 'https://deqing.58.com/ershoufang/'
    page_text = requests.get(url= url,headers = headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//section[@class="list"]/div')
    fp =open('58德清.txt','w',encoding='utf-8')
    for div in div_list:
        title= div.xpath('.//div[@class="property-price"]/p/span/text()')
        name = div.xpath('.//div[@class="property-content-title"]/h3/text()')[0]
        avep =  div.xpath('.//div[@class="property-price"]/p/text()')
        title.append(avep[1])
        title.append(str(name))

        print(title)
        fp.write("房源总价： "+title[0]+' '+ title[1] +'， \t房源均价：'+title[2]+'， 房源标题：'+title[3]+'\n')
