[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.46641.svg)](http://dx.doi.org/10.5281/zenodo.46641)

# Zika Data Guide

This repository contains data — and pointers to data — related to the 2015–16 Zika virus outbreak. Please feel free to [suggest additions and/or modifications](#suggestions-or-questions).

- [Global Data](#global-data)
    - [Zika Virus](#zika-virus)
    - [Mosquitoes](#mosquitoes)
- [Country-Specific Data](#country-specific-data)
    - [Brazil](#brazil)
    - [Colombia](#colombia)
    - [United States](#united-states)
- [Additional Resources](#additional-resources)

This repository also contains [archived PDFs](pdfs/) and [data extracted from the resources below](data/parsed). For a full list of files, [see `files.md`](files.md).

## Global Data

#### Zika Virus

- The Centers for Disease Control and Prevention (CDC) is maintaining a list of "[Countries and territories with active Zika virus transmission](http://www.cdc.gov/zika/geo/active-countries.html)."

- The Pan American Health Organization is maintaining a [similiar list](http://www.paho.org/hq/index.php?option=com_content&view=article&id=11603&Itemid=41696).

- The European Centre for Disease Prevention and Control is tracking [countries and territories with local Zika transmission](http://ecdc.europa.eu/en/healthtopics/zika_virus_infection/zika-outbreak/Pages/Zika-countries-with-transmission.aspx) and classifying them into several categories.

- The World Health Organization is not yet publishing structured data, but publishes a [page of Zika outbreak news](http://www.who.int/csr/don/archive/disease/zika-virus-infection/en/).

- HealthMap.org is [mapping news and social-media alerts](http://www.healthmap.org/zika/) about Zika.

- Wikipedia's [page on the outbreak](https://en.wikipedia.org/wiki/Zika_virus_outbreak_in_the_Americas_\(2015%E2%80%93present\)) includes a referenced table of confirmed case counts since April 2015, by country.

#### Mosquitoes

[Per the WHO](http://www.who.int/csr/disease/zika/en/), "Zika virus is transmitted to people through the bite of an infected mosquito from the Aedes genus, mainly Aedes aegypti in tropical regions. This is the same mosquito that transmits dengue, chikungunya and yellow fever."

- [The global compendium of *Aedes aegypti* and *Ae. albopictus* occurrence](http://www.nature.com/articles/sdata201535). [Data, as CSV files, available here](http://datadryad.org/resource/doi:10.5061/dryad.47v3c). Published 2015-07-07 in *Nature Scientific Data*.
    - "A global geographic database of known occurrences of *Ae. aegypti* and *Ae. albopictus* between 1960 and 2014 [...] derived from peer-reviewed literature and unpublished studies including national entomological surveys and expert networks. [...] This is the first comprehensive global database of *Ae. aegypti* and *Ae. albopictus* occurrence, consisting of 19,930 and 22,137 geo-positioned occurrence records respectively."


## Country-Specific Data

#### Brazil

- Brazil's health ministry is publishing [reports on Zika and microcephaly](http://portalsaude.saude.gov.br/index.php/o-ministerio/principal/leia-mais-o-ministerio/197-secretaria-svs/20799-microcefalia). The [latest report](http://portalsaude.saude.gov.br/images/pdf/2016/fevereiro/23/coes-microcefalia-informe-epidemiologico14-se07-2016-fev2016-14.pdf) covers through 2016-02-20.

#### Colombia

- Colombia's national institute of health is publishing [Zika-related reports](http://www.ins.gov.co/Noticias/ZIKA/Forms/AllItems.aspx), including regional counts of suspected Zika samples sent to the agency for testing, and case counts by municipality.
    - The [latest regional data](http://www.ins.gov.co/Noticias/ZIKA/reporte%20zika-03.pdf) covers 2015-09-01 through 2016-02-02.
    - The [latest municipal data](http://www.ins.gov.co/Noticias/ZIKA/CONTEO%20CASOS%20ZIKA%20MUNICIPIOS%20SE%2006%202016.pdf) through the 6th epidemiological week of 2016, which ended 2016-02-13. __Note:__ The national totals in this data [*seem* to be a few cases higher than the sum of the municipal cases](../../issues/6).


#### United States

The CDC is keeping a list of "[laboratory-confirmed Zika virus disease cases reported to ArboNET by [U.S.] state or territory](http://www.cdc.gov/zika/geo/united-states.html)".

Not many individual U.S. states are currently publishing structured data on Zika. But some do maintain Zika information pages, which might contain relevant data in the future. A partial list:

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

## Additional Resources

- A team of public health researchers are [standardizing official Zika data from several countries](https://github.com/cdcepi/zika).

- Scientific American [mapping the known U.S. cases](http://www.scientificamerican.com/article/zika-virus-threatens-u-s-from-abroad1/) and the locations where the virus in those cases was contracted.

## Acknowledgements

Special thanks to [Torsten Wurm](https://twitter.com/thelonevirologi), [@benparkergit](https://github.com/benparkergit), [@pushthings4ward](https://github.com/pushthings4ward), and [Matt Osborn](https://github.com/mattosborn).

## Suggestions or Questions?

Please [file an issue](https://github.com/BuzzFeedNews/zika-data/issues) or email jeremy.singer-vine@buzzfeed.com.

For more open-source data, methodologies, analyses, guides, and tools from BuzzFeed News, see [BuzzFeedNews/everything](https://github.com/BuzzFeedNews/everything).
