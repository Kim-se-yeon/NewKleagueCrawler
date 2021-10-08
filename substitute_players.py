from pretreatment import *
from kleague_page_path import *


def get_substitute_players(bs_obj, match_id, events, date, tier, home_team_name, away_team_name):
    home_players = []
    away_players = []

    # 경기기록부의 교체선수 크롤링
    for i, j in enumerate(substitute_players_path(bs_obj)):
        sub_player_info = j.get_text().split('\n')

        # 교체선수중에 첫번째 줄에 노락샌 배경으로 퍼센트가 들어간 선수 크롤링
        if len(sub_player_info) == 37:
            # 노란색 배경이 왼쪽에 있는 경우
            if sub_player_info[12] == '':

                home_player_sub_in = sub_player_info[1].strip()
                home_player_yellow = sub_player_info[2].strip()
                home_player_red = sub_player_info[3].strip()
                home_player_name = sub_player_info[20].strip()
                home_player_number = sub_player_info[21].strip()
                home_player_position = sub_player_info[22].strip()

                # 교체되고 다시 교체되는 경우
                home_player_sub_out = substitute_and_substitute(home_player_sub_in)[1]
                home_player_sub_in = substitute_and_substitute(home_player_sub_in)[0]

                # 옐로카드 레드카드 시간 부여
                home_player_yellow = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                     events)[0]
                home_player_red = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                     events)[1]

                # 대기를 SUB으로 변환
                home_player_position = sub_replace(home_player_position)

                home_player = [
                    date,
                    tier,
                    match_id,
                    home_team_name,
                    'H',
                    home_player_number,
                    home_player_position,
                    home_player_name,
                    '0',
                    home_player_sub_out,
                    home_player_sub_in,
                    home_player_yellow,
                    home_player_red
                ]
                if home_player_position != '':
                    home_players.append(home_player)

                away_player_position = sub_player_info[-14].strip()
                away_player_number = sub_player_info[-13].strip()
                away_player_name = sub_player_info[-12].strip()
                away_player_yellow = sub_player_info[-4].strip()
                away_player_red = sub_player_info[-3].strip()
                away_player_sub_in = sub_player_info[-2].strip()

                away_player_sub_out = substitute_and_substitute(away_player_sub_in)[1]
                away_player_sub_in = substitute_and_substitute(away_player_sub_in)[0]

                away_player_yellow = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                     events)[0]
                away_player_red = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                     events)[1]

                away_player_position = sub_replace(away_player_position)

                away_player = [
                    date,
                    tier,
                    match_id,
                    away_team_name,
                    'A',
                    away_player_number,
                    away_player_position,
                    away_player_name,
                    '0',
                    away_player_sub_out,
                    away_player_sub_in,
                    away_player_yellow,
                    away_player_red
                ]
                if away_player_position != '':
                    away_players.append(away_player)

            # 노란색 배경이 오른쪽에 있는 경우
            if sub_player_info[-18] == '':
                home_player_sub_in = sub_player_info[1].strip()
                home_player_yellow = sub_player_info[2].strip()
                home_player_red = sub_player_info[3].strip()
                home_player_name = sub_player_info[11].strip()
                home_player_number = sub_player_info[12].strip()
                home_player_position = sub_player_info[13].strip()

                home_player_sub_out = substitute_and_substitute(home_player_sub_in)[1]
                home_player_sub_in = substitute_and_substitute(home_player_sub_in)[0]

                home_player_yellow = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                     events)[0]
                home_player_red = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                     events)[1]

                home_player_position = sub_replace(home_player_position)

                home_player = [
                    date,
                    tier,
                    match_id,
                    home_team_name,
                    'H',
                    home_player_number,
                    home_player_position,
                    home_player_name,
                    '0',
                    home_player_sub_out,
                    home_player_sub_in,
                    home_player_yellow,
                    home_player_red
                ]
                if home_player_position != '':
                    home_players.append(home_player)

                away_player_position = sub_player_info[-23].strip()
                away_player_number = sub_player_info[-22].strip()
                away_player_name = sub_player_info[-21].strip()
                away_player_yellow = sub_player_info[-4].strip()
                away_player_red = sub_player_info[-3].strip()
                away_player_sub_in = sub_player_info[-2].strip()

                away_player_sub_out = substitute_and_substitute(away_player_sub_in)[1]
                away_player_sub_in = substitute_and_substitute(away_player_sub_in)[0]

                away_player_yellow = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                     events)[0]
                away_player_red = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                     events)[1]

                away_player_position = sub_replace(away_player_position)

                away_player = [
                    date,
                    tier,
                    match_id,
                    away_team_name,
                    'A',
                    away_player_number,
                    away_player_position,
                    away_player_name,
                    '0',
                    away_player_sub_out,
                    away_player_sub_in,
                    away_player_yellow,
                    away_player_red
                ]
                if away_player_position != '':
                    away_players.append(away_player)

        # 노란색 배경이 양쪽에 있는 경우
        elif len(sub_player_info) == 46:
            home_player_sub_in = sub_player_info[1].strip()
            home_player_yellow = sub_player_info[2].strip()
            home_player_red = sub_player_info[3].strip()
            home_player_name = sub_player_info[20].strip()
            home_player_number = sub_player_info[21].strip()
            home_player_position = sub_player_info[22].strip()

            home_player_sub_out = substitute_and_substitute(home_player_sub_in)[1]
            home_player_sub_in = substitute_and_substitute(home_player_sub_in)[0]

            home_player_yellow = \
                card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                 events)[0]
            home_player_red = \
                card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                 events)[1]

            home_player_position = sub_replace(home_player_position)

            home_player = [
                date,
                tier,
                match_id,
                home_team_name,
                'H',
                home_player_number,
                home_player_position,
                home_player_name,
                '0',
                home_player_sub_out,
                home_player_sub_in,
                home_player_yellow,
                home_player_red
            ]
            if home_player_position != '':
                home_players.append(home_player)
            away_player_position = sub_player_info[-23].strip()
            away_player_number = sub_player_info[-22].strip()
            away_player_name = sub_player_info[-21].strip()
            away_player_yellow = sub_player_info[-4].strip()
            away_player_red = sub_player_info[-3].strip()
            away_player_sub_in = sub_player_info[-2].strip()

            away_player_sub_out = substitute_and_substitute(away_player_sub_in)[1]
            away_player_sub_in = substitute_and_substitute(away_player_sub_in)[0]

            away_player_yellow = \
                card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                 events)[0]
            away_player_red = \
                card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                 events)[1]

            away_player_position = sub_replace(away_player_position)

            away_player = [
                date,
                tier,
                match_id,
                away_team_name,
                'A',
                away_player_number,
                away_player_position,
                away_player_name,
                '0',
                away_player_sub_out,
                away_player_sub_in,
                away_player_yellow,
                away_player_red
            ]
            if away_player_position != '':
                away_players.append(away_player)

        # 나머지 경우
        else:
            # 교체선수가 꽉 차 있지 않는 예외상황 존재하여 try문으로 한번 제외
            try:
                home_player_sub_in = sub_player_info[1].strip()
                home_player_yellow = sub_player_info[2].strip()
                home_player_red = sub_player_info[3].strip()
                home_player_name = sub_player_info[11].strip()
                home_player_number = sub_player_info[12].strip()
                home_player_position = sub_player_info[13].strip()

                # 교체되고 다시 교체되는 경우
                home_player_sub_out = substitute_and_substitute(home_player_sub_in)[1]
                home_player_sub_in = substitute_and_substitute(home_player_sub_in)[0]

                # 옐로카드 레드카드 시간 부여
                home_player_yellow = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                     events)[0]
                home_player_red = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red,
                                     events)[1]

                # 대기를 SUB으로 변환
                home_player_position = sub_replace(home_player_position)

                home_player = [
                    date,
                    tier,
                    match_id,
                    home_team_name,
                    'H',
                    home_player_number,
                    home_player_position,
                    home_player_name,
                    '0',
                    home_player_sub_out,
                    home_player_sub_in,
                    home_player_yellow,
                    home_player_red
                ]
                if home_player_position != '':
                    home_players.append(home_player)
            except:
                continue

            try:
                away_player_position = sub_player_info[-14].strip()
                away_player_number = sub_player_info[-13].strip()
                away_player_name = sub_player_info[-12].strip()
                away_player_yellow = sub_player_info[-4].strip()
                away_player_red = sub_player_info[-3].strip()
                away_player_sub_in = sub_player_info[-2].strip()

                away_player_sub_out = substitute_and_substitute(away_player_sub_in)[1]
                away_player_sub_in = substitute_and_substitute(away_player_sub_in)[0]

                away_player_yellow = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                     events)[0]
                away_player_red = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red,
                                     events)[1]

                away_player_position = sub_replace(away_player_position)

                away_player = [
                    date,
                    tier,
                    match_id,
                    away_team_name,
                    'A',
                    away_player_number,
                    away_player_position,
                    away_player_name,
                    '0',
                    away_player_sub_out,
                    away_player_sub_in,
                    away_player_yellow,
                    away_player_red
                ]
                if away_player_position != '':
                    away_players.append(away_player)
            except:
                continue
    return home_players, away_players
