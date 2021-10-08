# K리그 경기기록부의 해당하는 웹페이지의 각 정보별 경로

# 날짜 경로
def date_path(bs_obj):
    path = bs_obj.findAll("td")[4].get_text()
    return path


# 전반전 시간 경로
def time_first_half_path(bs_obj):
    path = bs_obj.findAll("table")[2].findAll("td")[3].get_text()
    return path


# 후반전 시간 경로
def time_second_half_path(bs_obj):
    path = bs_obj.findAll("table")[2].findAll("td")[15].get_text()
    return path


# 날씨 경로
def weather_path(bs_obj):
    path = bs_obj.findAll("table")[2].findAll("td")[13].text.split('/')[1].strip()
    return path


# 경기장 경로
def pitch_path(bs_obj):
    path = bs_obj.findAll("table")[2].findAll("td")[13].text.split('/')[0].strip()
    return path


# 홈팀 이름 경로
def home_team_path(bs_obj):
    path = bs_obj.findAll("table")[8].findAll("td")[0].get_text()
    return path


# 홈팀 스코어 결로
def home_team_score_path(bs_obj):
    path = bs_obj.findAll("table")[8].findAll("td")[1].get_text()
    return path


# 어웨이 이름 경로
def away_team_path(bs_obj):
    path = bs_obj.findAll("table")[8].findAll("td")[8].get_text()
    return path


# 어웨이 스코어 경로
def away_team_score_path(bs_obj):
    path = bs_obj.findAll("table")[8].findAll("td")[7].get_text()
    return path


# 선발 선수 테이블 경로
def starting_players_path(bs_obj):
    path = bs_obj.findAll("table")[19].findAll("tr")
    return path


# 교체 선수 테이블 경로
def substitute_players_path(bs_obj):
    path = bs_obj.findAll("table")[23].findAll("tr")
    return path


# 선수 이벤트(경고, 교체 ,골) 오른쪽 기록 테이블 경로
def match_timeline_path(bs_obj):
    path = bs_obj.findAll("table")[-2].findAll("tr")
    return path
