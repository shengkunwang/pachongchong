import requests
from lxml import etree

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }

    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url = url, headers = headers).text

    tree = etree.HTML(page_text)

    a_city = []
    hot_city = tree.xpath('//div[@class = "hot"]/div[2]/ul/li')
    for city in hot_city:
        hot_city_name = city.xpath('./a/text()')
        # print(hot_city_name)
        a_city.append(hot_city_name)
   # 按照字母分类爬取到数组，每个开头字母城市为一个数组
   #  all_citys = tree.xpath('//div[@class= "all"]/div[2]/ul')
   #  for city in all_citys:
   #      city_name = city.xpath('./div[2]/li/a/text()')

    all_citys = tree.xpath('//div[@class= "all"]/div[2]/ul/div[2]/li') # 每个城市单独一个数组
    for city in all_citys:
        city_name = city.xpath('./a/text()')[0]
        a_city.append(city_name)
    print(len(a_city),a_city)

    # 对于xpath表达式可以用或运算符，将上面两个式子合并
    # citys = tree.xpath('//div[@class = "hot"]/div[2]/ul/li| //div[@class= "all"]/div[2]/ul/div[2]/li')
    # for city in citys:
    #     city_name = city.xpath('./a/text()')[0]
    #     a_city.append(city_name)
    # print(len(a_city), a_city)