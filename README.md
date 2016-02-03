# Zika Data Guide

This repository contains data — and pointers to data — related to the 2015–16 Zika virus outbreak. Please feel free to [suggest additions and/or modifications](#suggestions-or-questions).

- [Global Data](#global-data)
    - [Zika Virus](#zika-virus)
    - [Mosquitoes](#mosquitoes)
- [Country-Specific Data](#country-specific-data)
    - [Brazil](#brazil)
    - [Colombia](#colombia)
    - [United States](#united-states)

This repository also contains [archived PDFs](pdfs/) and [data extracted from the resources below](data/parsed). For a full list of files, [see `files.md`](files.md).

## Global Data

#### Zika Virus

- The Centers for Disease Control and Prevention (CDC) is maintaining a list of "[Countries and territories with active Zika virus transmission](http://www.cdc.gov/zika/geo/index.html)."

- The Pan American Health Organization is maintaining a [similiar list](http://www.paho.org/hq/index.php?option=com_content&view=article&id=11603&Itemid=41696).

- The World Health Organization is not yet publishing structured data, but publishes a [page of Zika outbreak news](http://www.who.int/csr/don/archive/disease/zika-virus-infection/en/).

- HealthMap is using automated parsing to [map global Zika cases](http://www.healthmap.org/zika/) from online sources.

- Wikipedia has a referenced table of figures for [Zika cases since 2015](https://en.wikipedia.org/wiki/Zika_virus_outbreak_in_the_Americas_(2015%E2%80%93present)).

#### Mosquitoes

[Per the WHO](http://www.who.int/csr/disease/zika/en/), "Zika virus is transmitted to people through the bite of an infected mosquito from the Aedes genus, mainly Aedes aegypti in tropical regions. This is the same mosquito that transmits dengue, chikungunya and yellow fever."

- [The global compendium of *Aedes aegypti* and *Ae. albopictus* occurrence](http://www.nature.com/articles/sdata201535). csv data [here](http://datadryad.org/resource/doi:10.5061/dryad.47v3c). Published 2015-07-07 in *Nature Scientific Data*.
    - "A global geographic database of known occurrences of *Ae. aegypti* and *Ae. albopictus* between 1960 and 2014 [...] derived from peer-reviewed literature and unpublished studies including national entomological surveys and expert networks. [...] This is the first comprehensive global database of *Ae. aegypti* and *Ae. albopictus* occurrence, consisting of 19,930 and 22,137 geo-positioned occurrence records respectively."

#### Spread prediction

- [Anticipating the international spread of Zika virus from Brazil](http://www.thelancet.com/journals/lancet/article/PIIS0140-6736(16)00080-5/fulltext). Published 2016-01-16 in *The Lancet*
    - A short paper on the anticipated spread of Zika using mosquito data, worldwide temperature proflies and international traveller destinations.

## Country-Specific Data

#### Brazil

- Brazil's health ministry is publishing [reports on Zika and microcephaly](http://portalsaude.saude.gov.br/index.php/o-ministerio/principal/leia-mais-o-ministerio/197-secretaria-svs/20799-microcefalia). The [latest covers through 2016-01-30](http://portalsaude.saude.gov.br/images/pdf/2016/fevereiro/02/COES-Microcefalias---Informe-Epidemiol--gico-11---SE-04-2016---02jan2016---18h51-VDP.pdf).

#### Colombia

- Colombia's national institute of health is publishing [Zika-related reports](http://www.ins.gov.co/Noticias/ZIKA/Forms/AllItems.aspx), including regional counts of suspected Zika samples sent to the agency for testing. The [latest covers 2015-09-01 through 2016-01-29](http://www.ins.gov.co/Noticias/ZIKA/reporte%20zika-02.pdf).


#### United States

Not many U.S. states are currently publishing structured data on Zika. But some do maintain Zika information pages, which might contain relevant data in the future. A partial list:

- California
    - [Information page](https://www.cdph.ca.gov/HealthInfo/discond/Pages/Zika.aspx)
    - ["Travel-Associated Cases of Zika Virus in California"](https://www.cdph.ca.gov/HealthInfo/discond/Documents/TravelAssociatedCasesofZikaVirusinCA.pdf), updated every Friday.

- Florida
    - [Information page](http://www.floridahealth.gov/diseases-and-conditions/zika-virus/index.html?utm_source=flhealthIndex)

- Virginia
    - [Information page](http://www.vdh.virginia.gov/epidemiology/Zika/index.htm)

- Texas
    - [Information page](https://www.dshs.state.tx.us/idcu/disease/arboviral/zika/)
    - [News updates](https://www.dshs.state.tx.us/news/updates.shtm)

In the meantime, Scientific American is collecting unstructured data (e.g., news releases) from state health departments, and [mapping the known U.S. cases](http://www.scientificamerican.com/article/zika-virus-threatens-u-s-from-abroad1/).

## Acknowledgements

Special thanks to [Torsten Wurm](https://twitter.com/thelonevirologi) and [@benparkergit](https://github.com/benparkergit).

## Suggestions or Questions?

Please [file an issue](https://github.com/BuzzFeedNews/zika-data/issues) or email jeremy.singer-vine@buzzfeed.com.
