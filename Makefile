default:

cdc:
	./scripts/scrape-cdc-list.py > data/parsed/cdc/cdc-active-transmission-countries.txt

colombia:
	./scripts/parse-colombia.py < pdfs/colombia/colombia-2016-01-22.pdf > data/parsed/colombia/colombia-2016-01-22.csv
