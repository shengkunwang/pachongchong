import requests
import json

if __name__ == '__main__':
    # 指定URL
    url = 'https://fanyi.baidu.com/sug'
    word = input('enter a word: ')
    # 使用字典进行灵活输入
    data ={
        'kw':word
    }
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }
    # post 请求参数处理
    response = requests.post(url = url,data =data,headers = headers)
    page = response.json()
    print(page)

    # 保存数据
    filename = word+'.json'
    fp=open(filename,'w',encoding = 'utf-8' )
    json.dump(page,fp=fp,ensure_ascii=False)
    print("翻译结果已保存")