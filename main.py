# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # UA伪装：让爬虫对应的请求载体身份标识伪装成一款浏览器
    headers = {
       'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }

    url = 'https://www.sogou.com/web'
    kw = input('enter your explore word:')
    param = {
        'query':kw
    }
    response =requests.get(url=url,params=param,headers=headers)
    page = response.text

    fileName = kw+'.html'
    with open(fileName,'w',encoding = 'utf-8')  as fp:
        fp.write(page)
    print("网页保存成功")