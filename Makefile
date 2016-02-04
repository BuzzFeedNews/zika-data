default:

cdc:
	./scripts/scrape-cdc-list.py > data/parsed/cdc/cdc-active-transmission-countries.txt

ecdc:
	./scripts/scrape-ecdc-list.py > data/parsed/ecdc/ecdc-local-transmission-countries.csv
