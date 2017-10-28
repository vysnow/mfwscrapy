SQ		?=	chenzhou
VENV	=	.venv
SCRAPER	=	./mfwscraper
PYTHON	=	.venv/bin/python3
SCRAPY	=	../.venv/bin/scrapy

env:
	python3 -m venv $(VENV)

shell:
	$(PYTHON) manage.py shell

prepare:
	$(PYTHON) -m pip install --requirement requirements.txt

crawl:
	cd $(SCRAPER) && $(SCRAPY) crawl mdd -a q=$(SQ)

migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

serve:
	$(PYTHON) manage.py runserver