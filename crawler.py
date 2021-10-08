import os
import csv
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Crawler:
    def __init__(self, season, tier):
        self.season = season
        self.tier = tier
        self.path = os.getcwd()
        self.dirname = "results"

    def get_bs_obj(self, match_id):
        url = f"https://press.kleague.com/new/app/DR_DlgGameSheet/GameResult4.asp?iptMeetYear={self.season}&iptMeetSeq={self.tier}&iptGameid={match_id}&iptMeetName=%ED%95%98%EB%82%98%EC%9B%90%ED%81%90%20K%EB%A6%AC%EA%B7%B81%20{self.season}"
        html = urlopen(url)
        bs_obj = BeautifulSoup(html, "html.parser")
        return bs_obj

    def create_folder(self):
        direct = os.path.join(self.path, self.dirname)
        print('\n', direct)
        if os.path.exists(direct):
            print("Folder Already Exists. Skip Create.")
        else:
            os.mkdir(direct)
            print("Folder Created.")

    def write_header(self, header, fname):
        print('\n', fname)
        if os.path.isfile(fname) is False:
            f = open(fname, 'a+', newline='')
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            print("File created. Write header")
            f.close()
        else:
            print('File already exists. Skip writing header')

    def drop_duplicate_rows(self, fname):
        df = pd.read_csv(fname)
        df = df.drop_duplicates()
        df.to_csv(fname, index=False)
        print("\nDrop duplicates Done.")




