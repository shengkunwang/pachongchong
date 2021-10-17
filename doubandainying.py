import requests
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    data = {
       'type':'5',
        'interval_id':'100:90',
        'action':'',
        'start':'0',
        'limit':' 10'
    }

    headers = {
        'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }

    response = requests.get(url = url, params= data,headers = headers)
    page = response.json()
    print(page)
    fp = open('./douban.json','w',encoding = 'utf-8')
    json.dump(page,fp = fp,ensure_ascii=False)

    print('排名保存成功')