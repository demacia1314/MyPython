import requests

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': 24,
        'interval_id': '100:90',
        'start':0,
        'limit':1#需要爬取的电影数
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    response  = requests.get(url = url,params=params,headers = headers)
    print(response.json())