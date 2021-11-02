import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'

result = requests.get(url)
# print(result) #성공 200
doc = BeautifulSoup(result.text, 'html.parser')

url_list = doc.select('ul.list_news2 a.link_txt')
# print(len(url_list))

for i, href in enumerate(url_list):
    #기사 1건의 제목과 본문을 수집하는 코드
    #print(href['href']) # ['필요한 정보']
    new_url = href['href']

    result = requests.get(new_url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')
    contents.pop(-1)
    content = ''
    for info in contents:
        content += info.get_text()

    print('■■ NEWS -> {} ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(i+1))
    print('# URL: {}'.format(new_url))
    print('# TITLE: {}'.format(title))
    print('# CONTENTS: {}'.format(content))