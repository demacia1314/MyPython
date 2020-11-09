import requests
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
#处理url携带的参数:封装到字典中
query = input('input to search')
param = {
    'query':query
}
#UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
response = requests.get(url = url,params=param,headers = headers)
page_text = response.text
file_name = query+'.html'
with open(file_name,'w',encoding='utf-8') as f:
    f.write(page_text)
print('Successfully Saved!')