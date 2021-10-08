from pretreatment import *
from kleague_page_path import *


def get_starting_players(bs_obj, match_id, events, date, tier, home_team_name, away_team_name):
    home_players = []
    away_players = []

    # 경기기록부의 있는 선발선수 크롤링
    for i, j in enumerate(starting_players_path(bs_obj)):
        if len(j) == 45 or len(j) == 53:
            starting_player_info = j.get_text().split('\n')

            # GK선수의 크롤링 부분의 길이가 달라 GK 부분처리
            if len(starting_player_info) == 46:
                home_player_sub_in = ''
                home_player_sub_out = starting_player_info[1].strip()
                home_player_yellow = starting_player_info[2].strip()
                home_player_red = starting_player_info[3].strip()
                home_player_name = starting_player_info[20].strip()
                home_player_number = starting_player_info[21].strip()
                home_player_position = starting_player_info[22].strip()

                away_player_position = starting_player_info[-23].strip()
                away_player_number = starting_player_info[-22].strip()
                away_player_name = starting_player_info[-21].strip()
                away_player_yellow = starting_player_info[-4].strip()
                away_player_red = starting_player_info[-3].strip()
                away_player_sub_out = starting_player_info[-2].strip()
                away_player_sub_in = ''

                # 옐로카드 레드카드 시간 부여
                home_player_yellow = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red, events)[
                        0]
                home_player_red = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red, events)[
                        1]

                away_player_yellow = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red, events)[
                        0]
                away_player_red = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red, events)[
                        1]

                home_player = [
                    date,
                    tier,
                    match_id,
                    home_team_name,
                    'H',
                    home_player_number,
                    home_player_position,
                    home_player_name,
                    '1',
                    home_player_sub_out,
                    home_player_sub_in,
                    home_player_yellow,
                    home_player_red
                ]
                home_players.append(home_player)

                away_player = [
                    date,
                    tier,
                    match_id,
                    away_team_name,
                    'A',
                    away_player_number,
                    away_player_position,
                    away_player_name,
                    '1',
                    away_player_sub_out,
                    away_player_sub_in,
                    away_player_yellow,
                    away_player_red
                ]
                away_players.append(away_player)

            # 나머지 필드 플레이어 크롤링
            if len(starting_player_info) == 28:
                home_player_sub_in = ''
                home_player_sub_out = starting_player_info[1].strip()
                home_player_yellow = starting_player_info[2].strip()
                home_player_red = starting_player_info[3].strip()
                home_player_name = starting_player_info[11].strip()
                home_player_number = starting_player_info[12].strip()
                home_player_position = starting_player_info[13].strip()

                away_player_position = starting_player_info[-14].strip()
                away_player_number = starting_player_info[-13].strip()
                away_player_name = starting_player_info[-12].strip()
                away_player_yellow = starting_player_info[-4].strip()
                away_player_red = starting_player_info[-3].strip()
                away_player_sub_out = starting_player_info[-2].strip()
                away_player_sub_in = ''

                home_player_yellow = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red, events)[
                        0]
                home_player_red = \
                    card_events_time(home_player_name, home_player_number, home_player_yellow, home_player_red, events)[
                        1]

                away_player_yellow = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red, events)[
                        0]
                away_player_red = \
                    card_events_time(away_player_name, away_player_number, away_player_yellow, away_player_red, events)[
                        1]

                home_player = [
                    date,
                    tier,
                    match_id,
                    home_team_name,
                    'H',
                    home_player_number,
                    home_player_position,
                    home_player_name,
                    '1',
                    home_player_sub_out,
                    home_player_sub_in,
                    home_player_yellow,
                    home_player_red
                ]
                home_players.append(home_player)

                away_player = [
                    date,
                    tier,
                    match_id,
                    away_team_name,
                    'A',
                    away_player_number,
                    away_player_position,
                    away_player_name,
                    '1',
                    away_player_sub_out,
                    away_player_sub_in,
                    away_player_yellow,
                    away_player_red
                ]
                away_players.append(away_player)
    return home_players, away_players
