#!/usr/bin/env python
import requests
import lxml.html

def scrape():
    res = requests.get("http://www.cdc.gov/zika/geo/active-countries.html")
    dom = lxml.html.fromstring(res.content)
    li_els = dom.cssselect(".list-block li")
    countries = [ li.text_content() for li in li_els ]
    return countries
    
if __name__ == "__main__":
    print("\n".join(scrape()))
