import requests
import json

if __name__ =="__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data={
       ' on': 'true',
        'page': '1',
       ' pageSize': '15',
       ' productName': '',
       ' conditionType':' 1',
       ' applyname':'',
       ' applysn': ''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/94.0.4606.71 Safari/537.36Edg/94.0.992.38'
    }
    # 获取企业的ID
    ID_list = []
    idlist=requests.post(url= url,data = data,headers = headers).json()
    for dic in idlist['list']:
        ID_list.append(dic['ID'])
    print(ID_list)
    # 获取企业的详情页数据
    all_info=[]
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

    for id in ID_list:
        data={
            'id' : id
        }
        detilinfo = requests.post(url = post_url,data = data,headers = headers).json()
        all_info.append(detilinfo)
        print(detilinfo)
    fp = open('./allinfo.json','w',encoding = 'utf-8')
    json.dump(all_info,fp = fp,ensure_ascii=False )
    print("数据已保存")