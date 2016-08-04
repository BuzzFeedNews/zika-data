#!/usr/bin/env python
import requests
import lxml.html
import pandas as pd
import sys

URL = "http://ecdc.europa.eu/en/healthtopics/zika_virus_infection/zika-outbreak/Pages/Zika-countries-with-transmission.aspx"

columns = [
    "country",
    "areas",
    "current_zika_transmission",
]

def scrape():
    html = requests.get(URL).content
    dom = lxml.html.fromstring(html)
    table = dom.cssselect(".ms-rteTable-1")[-1]
    rows = table.cssselect("tr")[1:]
    data = [ [ td.text_content().strip()
        for td in tr.cssselect("td, th") ]
            for tr in rows ]
    df = pd.DataFrame(data, columns=columns)[columns]
    return df

if __name__ == "__main__":
    df = scrape()
    df.to_csv(sys.stdout, index=False, encoding="utf-8")
