from crawler import Crawler
import os
import re
import csv
import pprint
from myconstant import *
from starting_players import *
from substitute_players import *


class RosterCrawler(Crawler):
    def __init__(self, season, tier):
        super().__init__(season, tier)
        self.fname = os.path.join(self.path, self.dirname, f"{season}_kleague_{tier}_rosters.csv")
        self.header = roster_header

    def run(self):
        self.create_folder()
        self.write_header(header=roster_header, fname=self.fname)

        f = open(self.fname, "a+", newline='')
        csv_writer = csv.writer(f)
        match_id = 1

        while True:
            bs_obj = self.get_bs_obj(match_id=match_id)
            events = self.get_match_events(bs_obj=bs_obj, match_id=match_id)
            players = self.get_players(bs_obj=bs_obj, match_id=match_id, events=events)
            if players is None:
                break
            else:
                csv_writer.writerows(players)
                match_id += 1

                # 2021년 시즌 이벤트 빈 부분 예외처리
                if self.season == 2021 and match_id == 139:
                    match_id = 145
                elif self.season == 2021 and match_id == 152:
                    match_id = 153
                elif self.season == 2021 and match_id == 158:
                    match_id = 159
                elif self.season == 2021 and match_id == 163:
                    match_id = 164
                elif self.season == 2021 and match_id == 178:
                    match_id = 179

        f.close()
        self.drop_duplicate_rows(fname=self.fname)

    # 경기기록부 중간에 위치한 선발선수 크롤링
    def get_players(self, bs_obj, match_id, events):
        season = self.season
        tier = self.tier

        date = date_split(season, date_path(bs_obj))
        home_team_name = team_name_change(home_team_path(bs_obj))
        away_team_name = team_name_change(away_team_path(bs_obj))

        start_home_players = get_starting_players(bs_obj, match_id, events, date, tier, home_team_name, away_team_name)[0]
        start_away_players = get_starting_players(bs_obj, match_id, events, date, tier, home_team_name, away_team_name)[1]

        sub_home_players = get_substitute_players(bs_obj, match_id, events, date, tier, home_team_name, away_team_name)[0]
        sub_away_players = get_substitute_players(bs_obj, match_id, events, date, tier, home_team_name, away_team_name)[1]

        home_players = start_home_players + sub_home_players
        away_players = start_away_players + sub_away_players

        players = home_players + away_players

        # 날짜 없는 경기 필터링
        if len(date) < 5:
            players = None
            print(f"No Match Exist : {match_id}")
        else:
            print('\n')
            pprint.pprint(players)
        return players

    # 경기기록부의 오른쪽 이벤트 정보 크롤링
    def get_match_events(self, bs_obj, match_id):
        match_timeline = match_timeline_path(bs_obj)
        halftime = '전반'

        match_events = []
        for i, j in enumerate(match_timeline):

            if "전반 휴식" in str(j):
                halftime = '후반'

            # 사진 정보를 포함하는 경우
            if "gif" in str(j):
                event = str(j).split(".gif")[0].split("/")[-1]
                event_detail = j.text.strip()
                event_detail = event_detail.replace("\n\n", " ")

                # 선수이름 띄어쓰기 예외 사항 처리(선수이름에 띄어쓰기 존재할 경우 처리해 주어야됨)
                event_detail = space_in_name(event_detail)

                # 이벤트 상세정보를 포함한 경우
                if "(" in event_detail:

                    # 괄호 안의 상세정보의 공백 삭제
                    p = re.compile('\(.+\)')
                    m = p.search(event_detail).group()
                    event_detail = event_detail.replace(m, m.replace(' ', ''))
                    event_detail = event_detail.split(" ")

                    # 역방향인 요소의 순서가 다름 -> 첫번째 요소의 첫 글짜가 '('인 경우
                    try:
                        if event_detail[0][0] == "(":
                            info = event_detail[0]
                            back_number = event_detail[1]
                            player_name = event_detail[2]
                            minute = event_detail[3]

                        else:
                            minute = event_detail[0]
                            back_number = event_detail[1]
                            player_name = event_detail[2]
                            info = event_detail[3]
                    except:
                        continue

                # 이벤트 상세정보 포함하지 않은 경우 ex) 단독 득점
                else:

                    # 역방향 패턴에 매칭될 경우
                    if re.search('(\d+) (.+) (\d+)', event_detail) is not None:
                        event_detail = event_detail.split(" ")

                        back_number = event_detail[0]
                        player_name = event_detail[1]
                        minute = event_detail[2]
                        info = ""

                    # 정방향 패턴일 경우
                    else:
                        event_detail = event_detail.split(" ")

                        minute = event_detail[0]
                        back_number = event_detail[1]
                        player_name = event_detail[2]
                        info = ""

                # 다시 이름을 띄워줌(카드 시간 부여를 위해 원래 이름으로 저장되어야됨)
                player_name = return_name(player_name)

                # 문자열 처리
                info = info.replace('(', '')
                info = info.replace(')', '')

                match_event = [
                    match_id,
                    event,
                    halftime,
                    minute,
                    player_name,
                    back_number,
                    info
                ]
                # print(match_event)
                match_events.append(match_event)
        return match_events






