import requests
from lxml import etree
import os

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }

    url = 'https://pic.netbian.com/4kmeinv/'
    '''
    处理中文乱码的两种方式
    一、将response编码方式改变
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page = response.text 
    '''

    page = requests.get(url = url,headers = headers).text

    tree = etree.HTML(page)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    if not os.path.exists('./爬取的图'):
        os.mkdir('./爬取的图')
    for li in li_list:

        # xpath 返回的是一个列表

        img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt') [0]+ '.jpg'
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        print(img_src,img_name)
        img_data = requests.get(url = img_src,headers = headers).content # 二进制数据 为.content格式
        img_path = '爬取的图/'+ img_name
        with open(img_path,'wb') as fp:  #wb ：以为进制形式写入
            fp.write(img_data)
            print(img_name + '下载成功')
    print('图片下载完成')


