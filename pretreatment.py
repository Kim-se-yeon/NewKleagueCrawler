# 날짜 변환 (split 이외에 다른 방법이 있을꺼라 판단됨)
def date_split(season, date):
    if date == '[번]':
        return
    else:
        date = str(season) + ((date.split('] ')[1]).split('(')[0].replace('/', ""))
    return date


# 경기 시작 시간, 종료 시간, 경기 총 시간 나누기
def time_start_split(time):
    try:
        if time == '':
            return
        else:
            s1_start = time.split(' ~')[0]
    except:
        return
    return s1_start


def time_end_split(time):
    try:
        if time == '':
            return
        else:
            s1_end = (time.split('~ ')[1]).split(' (')[0]
    except:
        return
    return s1_end


def time_dur_split(time):
    try:
        if time == '':
            return
        else:
            s1_dur = (time.split('( ')[1]).split(' )')[0]
    except:
        return
    return s1_dur


# 날씨 정보에 id 부여
def get_weather_id(weather):
    weather_type = {'맑음': '1',
                    '흐림': '2',
                    '비': '3',
                    '흐리고 비': '4',
                    '눈': '5',
                    '': '0'
                    }
    return weather_type.get(weather)


# 경기장 id 부여
def get_pitch_id(pitch):
    pitch_id = {'잠실 올림픽': '1',
                '수원 종합': '4',
                '광양 전용': '5',
                '부천 종합': '8',
                '부산 구덕': '9',
                '안양 종합': '10',
                '포항 스틸야드': '14',
                '강릉 종합': '25',
                '춘천 송암': '41',
                '울산 문수': '68',
                '수원 월드컵': '69',
                '대전 월드컵': '70',
                '전주 월드컵': '71',
                '광주 월드컵': '73',
                '상주 시민': '80',
                '서울 월드컵': '82',
                '탄천 종합': '84',
                '제주 월드컵': '85',
                '창원 축구센터': '91',
                '인천 전용': '95',
                '안산 와스타디움': '103',
                '아산 이순신': '112',
                'DGB대구은행파크': '114',
                '광주 전용': '117',
                '김천 종합': '0',
                '성남 종합': '0',
                '양산 종합': '0',
                '진주 종합': '0',
                '울산 종합': '0',
                '제주 종합': '0',
                '천안 종합': '0',
                '대구 스타디움': '0',
                '대전 한밭 종합': '0',
                '순천 팔마': '0',
                '김해 운동장': '0',
                '부산 아시아드': '0',
                '전주종합': '0',
                '평창 알펜시아': '0',
                '': '0'
                }
    return pitch_id.get(pitch)


# 팀이름 단축
def team_name_change(team):
    team_name = {'FC서울': '서울',
                 '서울 이랜드': '서울E',
                 'FC안양': '안양',
                 '강원FC': '강원',
                 '경남FC': '경남',
                 '광주FC': '광주',
                 '대구FC': '대구',
                 '대전 하나 시티즌': '대전',
                 '부산 아이파크': '부산',
                 '부천FC': '부천',
                 '김천 상무': '상주',
                 '상주 상무': '상주',
                 '성남FC': '성남',
                 '수원 삼성': '수원',
                 '수원FC': '수원F',
                 '안산 그리너스': '안산',
                 '울산 현대': '울산',
                 '인천 Utd': '인천',
                 '전남 드래곤즈': '전남',
                 '전북 현대': '전북',
                 '제주 Utd': '제주',
                 '충남 아산 FC': '아산',
                 '포항 스틸러스': '포항',
                 '아산 무궁화': '아산'
                 }
    return team_name.get(team)


# 팀당 아이디 부여
def get_team_id(team):
    team_id = {'울산': 'K01',
               '수원': 'K02',
               '포항': 'K03',
               '제주': 'K04',
               '전북': 'K05',
               '부산': 'K06',
               '전남': 'K07',
               '성남': 'K08',
               '서울': 'K09',
               '대전': 'K10',
               '대구': 'K17',
               '인천': 'K18',
               '경남': 'K20',
               '강원': 'K21',
               '광주': 'K22',
               '상주': 'K23',
               '부천': 'K26',
               '안양': 'K27',
               '수원F': 'K29',
               '서울E': 'K31',
               '안산': 'K32',
               '아산': 'K34'
               }
    return team_id.get(team)


# 옐로카드 레드카드 시간 부여
def card_events_time(player_name, player_number, player_yellow, player_red, events):
    if (player_yellow == '1' or '2') or (player_red == '1'):
        for k in range(len(events)):
            if player_name == events[k][4] and player_number == events[k][5] and events[k][1] == 'yellow_card':
                player_yellow = str(events[k][2]) + events[k][3]
            elif player_name == events[k][4] and player_number == events[k][5] and events[k][1] == 'yellow_card_two':
                player_red = str(events[k][2]) + events[k][3]
            elif player_name == events[k][4] and events[k][1] == 'red_card':
                player_red = str(events[k][2]) + events[k][3]
            # 선수 옐로카드 예외사항은 찾아본 바에 의하면 후반 마지막 추가시간 부근에 경고를 받은경우 누락되어서 후반45로 예외값 처리
            elif player_yellow == '1':
                player_yellow = '후빈45'
    return player_yellow, player_red


# 교체되고 다시 교체되는 경우
def substitute_and_substitute(sub):
    if len(sub) > 8:
        sub_in = sub.split(')')[0] + ')'
        sub_out = sub.split(')')[1] + ')'
    else:
        sub_in = sub
        sub_out = ''
    return sub_in, sub_out


# 대기를 SUB으로 변환
def sub_replace(player_position):
    if player_position == '대기':
        player_position = 'SUB'
    return player_position


# 이벤트 처리에서 선수이름이 띄어져 있는 경우 예외 처리
def space_in_name(event_detail):
    if event_detail.find('수쿠타 파수') is not None:
        event_detail = event_detail.replace('수쿠타 파수', '수쿠타파수')

    if event_detail.find('브루노 누네스') is not None:
        event_detail = event_detail.replace('브루노 누네스', '브루노누네스')
    return event_detail


# 이벤트 처리에서 선수이름을 다시 띄어줌
def return_name(player_name):
    if player_name.find('수쿠타파수') is not None:
        player_name = player_name.replace('수쿠타파수', '수쿠타 파수')

    if player_name.find('브루노누네스') is not None:
        player_name = player_name.replace('브루노누네스', '브루노 누네스')
    return player_name
