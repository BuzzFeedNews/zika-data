#!/usr/bin/env python
import requests
import lxml.html
import pandas as pd
import re
import sys
import random

URL = "https://www.cdc.gov/zika/reporting/2017-case-counts.html"

INT_COLS = [ "symptomatic_disease_cases" , "presumptive_viremic_blood_donors" ]
COLS = [ "state_or_territory" ] + INT_COLS

paren_pat = re.compile(r"\([^\)]+\)") 

def parse_cell(text):
    return re.sub(paren_pat, "", text).strip()

def scrape():
    html = requests.get(URL, params={
        "_": random.random()
    }).content
    dom = lxml.html.fromstring(html)

    table = dom.cssselect("table")[0]
    trs = table.cssselect("tr")

    rows = [ [ parse_cell(td.text_content())
        for td in tr.cssselect("td:nth-child(1), td:nth-child(2), td:nth-child(4)") ] 
             for tr in trs ]

    data = [ row for row in rows[1:]
        if len(row) and not row[0] in [ "", "States", "Territories" ] ]

    df = pd.DataFrame(data, columns=COLS)
    for c in INT_COLS:
        df[c] = df[c].str.replace(",", "").str.strip("*").astype(int)

    return df

if __name__ == "__main__":
    df = scrape()
    df.to_csv(sys.stdout, index=False, encoding="utf-8")
