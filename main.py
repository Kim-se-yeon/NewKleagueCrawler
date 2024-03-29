from official_rosters_crawler import *
from official_records_crawler import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    RecordCrawler(season=2021, tier=1).run()
    RosterCrawler(season=2021, tier=1).run()

    #RecordCrawler(season=2021, tier=2).run()
    #RosterCrawler(season=2021, tier=2).run()



'''

    - 예외사항 -

2021 k리그2 pitch_id 누락 (김천 종합, 대전 한밭 종합)
2019 k리그1 pitch_id 누락 (성남 종합, 양산 종합, 진주 종합, 울산 종합, 제주 종합)
2019 k리그2 pitch_id 누락 (천안 종합)
2018 k리그1 pitch_id 누락 (대구 스타디움, 순천 팖마, 김해 운동장)
2018 k리그2 pitch_id 누락 (부산 아시아드)
2017 k리그1 pitch_id 누락 (전주종합, 평창 알펜시아)

2020 k리그1 이벤트 75, 158의 날씨정보 미기입
2020 k리그2 이벤트 30의 날씨정보 미기입

2020 k리그1 이벤트 157의 황현수 선수 옐로카드 예외사항 발생(오른쪽 기록테이블 누락)
2020 k리그2 이벤트 7의 임창균 선수 옐로카드 예외사항 발생(오른쪽 기록테이블 누락)
2020 k리그2 이벤트 129의 오승훈, 진성욱, 원기종 선수 옐로카드 예외사항 발생(오른쪽 기록테이블 누락)
2019 k리그1 이벤트 167의 백동규 선수 옐로카드 예외사항 발생(오른쪽 기록테이블 누락)
2019 k리그1 이벤트 193의 김광석 선수 옐로카드 예외사항 발생(오른쪽 기록테이블 누락)

2021 k리그1 이벤트 154 오른쪽 기록테이블에 선수 이외에 코치진 옐로카드….
2021 k리그1 이벤트중에 중간에 이벤트에 기록이 안된 경기 139~144, 152, 158…

선수이름에 띄어쓰기가 있는 선수 아벤트 크롤링이 안뎀


    - 예외사항 처리 방안 -

- pitch_id 누락된 값들을 0으로 임의로 부여함 
- 날씨 정보가 미기입된 부분도 0값으로 부여함
- 선수 옐로카드 예외사항은 찾아본 바에 의하면 후반 마지막 추가시간 부근에 경고를 받은경우 누락되어서 후반45로 예외값 처리
- 코치옐로카드는 상관없다고 판단하여 제외
- 이벤트에 기록이 안된 경기는 제외 (2021시즌에 한함)
- 띄어쓰기 있는 선수는 처리 과정에서는 붙이고 나중에 다시 띄어줌

'''