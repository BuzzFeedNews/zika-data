default:

cdc:
	./scripts/scrape-cdc-list.py > data/parsed/cdc/cdc-active-transmission-countries.txt
	./scripts/scrape-cdc-state-case-counts.py > data/parsed/cdc/cdc-state-case-counts-latest.csv

ecdc:
	./scripts/scrape-ecdc-list.py > data/parsed/ecdc/ecdc-local-transmission-countries.csv
