import requests
if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    id_list = []
    pages = 6#需要爬取的页数
    for page in range(1,pages+1):
        data = {
            'on': 'true',
            'page': page,
            'pageSize': 15,
            'productName':'',
            'conditionType': 1,
            'applyname':'',
            'applysn':''
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for dict in json_ids['list']:
            id_list.append(dict['ID'])


    url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

    for id in id_list:
        data2 = {
            'id': id
        }
        response = requests.post(url = url2,data = data2,headers = headers)
        print(response.json(),'\n')

