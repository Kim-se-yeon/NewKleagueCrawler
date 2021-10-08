import os
import csv
from myconstant import *
from pretreatment import *
from kleague_page_path import *
from crawler import Crawler


class RecordCrawler(Crawler):
    def __init__(self, season, tier):
        super().__init__(season, tier)
        self.fname = os.path.join(self.path, self.dirname, f"{season}_Kleague_{tier}_records.csv")
        self.header = record_header

    def run(self):
        self.create_folder()
        self.write_header(header=record_header, fname=self.fname)

        f = open(self.fname, "a+", newline='')
        csv_writer = csv.writer(f)
        match_id = 190

        while True:
            bs_obj = self.get_bs_obj(match_id=match_id)
            record = self.get_record(bsObj=bs_obj, match_id=match_id)
            if record is None:
                break
            else:
                csv_writer.writerow(record)
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

    # 경기 기록부의 맨 윗쪽 테이블에 있는 경기정보 크롤링
    def get_record(self, bsObj, match_id):
        season = self.season
        tier = self.tier
        match_id = match_id

        date = date_split(season, date_path(bsObj))

        time_first_half = time_first_half_path(bsObj)
        s1_start = time_start_split(time_first_half)
        s1_end = time_end_split(time_first_half)
        s1_dur = time_dur_split(time_first_half)

        time_second_half = time_second_half_path(bsObj)
        s2_start = time_start_split(time_second_half)
        s2_end = time_end_split(time_second_half)
        s2_dur = time_dur_split(time_second_half)

        weather = weather_path(bsObj)
        weather_id = get_weather_id(weather)

        pitch = pitch_path(bsObj)
        pitch_id = get_pitch_id(pitch)

        home_team = team_name_change(home_team_path(bsObj))
        home_team_id = get_team_id(home_team)
        home_team_score = home_team_score_path(bsObj)

        away_team = team_name_change(away_team_path(bsObj))
        away_team_id = get_team_id(away_team)
        away_team_score = away_team_score_path(bsObj)

        record = [
            tier,
            match_id,
            date,
            s1_start,
            s1_end,
            s1_dur,
            s2_start,
            s2_end,
            s2_dur,
            weather,
            weather_id,
            pitch,
            pitch_id,
            home_team,
            home_team_id,
            home_team_score,
            away_team,
            away_team_id,
            away_team_score,
        ]

        # 날짜 없으면 필터링
        if len(date) < 5:
            record = None
            print(f"No Match Exist : {match_id}")
        else:
            print(record)
        return record
