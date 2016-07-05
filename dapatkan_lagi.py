import requests
from bs4 import BeautifulSoup
import time
import csv
import pprint
import pandas as pd
pp = pprint.PrettyPrinter(indent=8)


df = pd.read_csv("datuk_dan_datin.csv")
hilang = [_id for _id in range(1,91194) if (_id not in df.Bil.values) and (_id % 20 is 0)]
df = pd.read_csv("datuk_dan_datin.csv")

complete_row = [ [bil,nama,anugerah,singkatan,tahun_kurniaan] for bil,nama,anugerah,singkatan,tahun_kurniaan in zip(df.Bil,df.Nama,df.Anugerah,df.Singkatan,df["Tahun Kurniaan"]) ]

for r in hilang:
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
