import requests
import  os
import  json
if __name__ == '__main__':
    word = input('Please input to translate\n')
    post_url = 'https://fanyi.baidu.com/sug'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    data = {
        'kw':word
    }

    response = requests.post(url = post_url,data = data,headers = headers)
    translation_dic = response.json()
    try:
        print(translation_dic['data'][0]['v'])
    except IndexError:
        print('I\'s a wrong word!')
    os.system('pause')
    #永久储存
    #file_name = word + '.json'
    #with open(file_name,'w',encoding='utf-8') as f:
        #json.dump(obj=translation_dic,fp = f,ensure_ascii=False)
        #print('Successfully saved!')
