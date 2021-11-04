# 영화리뷰, 점수, 작성자, 날짜정보 수집

import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=14450&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=2'
result = requests.get(url)
print(result)

doc = BeautifulSoup(result.text, 'html.parser')

review_list = doc.select('div.score_result > ul > li')
#print(len(review_list)) -> 10

for i, one in enumerate(review_list):
    print('#############################')

    #review score 수집
    #{}.format 방식은 비추

    review = one.select('div.score_reple > p > span')[-1].get_text().strip()

    #j = 0
    #if len(review_select) == 2:
    #    j = 1
    #review = review_select[j].get_text()

    #평점 수정
    score = one.select('div.star_score > em')[0].get_text()

    # 수집된 정보 출력
    print('SCORE => {}'.format(score))
    print('REVIEW => {}'.format(review))