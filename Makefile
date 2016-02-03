default:

cdc:
	./scripts/scrape-cdc-list.py > data/parsed/cdc/cdc-active-transmission-countries.txt

ecdc:
	./scripts/scrape-ecdc-list.py > data/parsed/ecdc/ecdc-local-transmission-countries.csv

colombia:
	./scripts/parse-colombia.py < pdfs/colombia/colombia-2016-01-22.pdf > data/parsed/colombia/colombia-2016-01-22.csv
