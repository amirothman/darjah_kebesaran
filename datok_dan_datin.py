import requests
from bs4 import BeautifulSoup
import time
import csv
import pprint
import pandas as pd
pp = pprint.PrettyPrinter(indent=8)


df = pd.read_csv("datuk_dan_datin.csv")
continue_previous = df.Bil.iloc[-1]
# 'Bil', 'Nama', 'Anugerah', 'Singkatan', 'Tahun Kurniaan'
complete_row = [ [bil,nama,anugerah,singkatan,tahun_kurniaan] for bil,nama,anugerah,singkatan,tahun_kurniaan in zip(df.Bil,df.Nama,df.Anugerah,df.Singkatan,df["Tahun Kurniaan"]) ]
#for r in range(0,50,20):
#for r in range(0,91194,20):
for r in range(continue_previous,91194,20):
    res = requests.post("http://www.istiadat.gov.my/index.php/component/semakanlantikanskp", data={"start":r})
    soup = BeautifulSoup(res.text, 'html.parser')
    rows_from_single_page = []
    for tr in soup.find_all("tr"):
        if len(tr.find_all("td")) == 5:
            row = [td.get_text().replace(u'\xa0', u' ') for td in tr.find_all("td")]
            rows_from_single_page.append(row)

    pp.pprint(rows_from_single_page)
    complete_row = complete_row + rows_from_single_page[1:]

    complete_row_dict = [{"Bil":row[0],"Nama":row[1],"Anugerah":row[2],"Singkatan":row[3],"Tahun Kurniaan":row[4]} for row in complete_row]

    df = pd.DataFrame(complete_row_dict)

    df.to_csv("datuk_dan_datin.csv")
