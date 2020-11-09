import requests
import  os
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    location = input('Please input a location or keyword to search\n')
    data = {
        'cname':'',
        'pid':'',
        'keyword': location,
        'pageIndex': 1,
        'pageSize': 10
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    response = requests.post(url = url,data = data,headers = headers)

    print(response.text)
    os.system('pause')
