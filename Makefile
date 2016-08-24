# Reference card for usual actions in development environment.
#
# For standard installation, see INSTALL.
# For details about development environment, see CONTRIBUTING.rst.
#
TOX ?= tox
GORUN ?= gorun.py


#: help - Display callable targets.
.PHONY: 
help:
	@echo "Reference card for usual actions in development environment."
	@echo "Here are available targets:"
	@egrep -o "^#: (.+)" [Mm]akefile  | sed 's/#: /* /'


#: clean - Basic cleanup, mostly temporary files.
.PHONY: clean
clean:
	# Clean API stuff.
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '__pycache__' -delete
	rm -rf *.egg-info
	# Remove empty directories.
	find . -type d -empty -delete


#: maintainer-clean - Destroy ALL what can be rebuilt.
.PHONY: maintainer-clean
maintainer-clean: clean


#: develop - Install development environment.
.PHONY: develop
develop:
	mkdir -p var
	pip install tox
	pip install -e .


#: db - Run API's database storage.
.PHONY: db
db:
	docker-compose up mongo


#: api - Run API's demo server.
.PHONY: api
api: develop
	minventoryapi


#: ui - Run UI's demo server.
ui:
	echo "UI is currently made of one static file. Just open 'ui.html' in your browser."


#: loaddata - Backup current data then load demo data.
loaddata: dumpdata


#: dumpdata - Backup data.
dumpdata:
	mkdir -p var


#: sphinx - Build Sphinx documentation in var/docs/html
sphinx:
	$(TOX) -e sphinx


#: readme - Build standalone documentation files (README, CONTRIBUTING...).
readme:
	$(TOX) -e readme


#: documentation - Build standalone documentation files and Sphinx docs.
documentation: sphinx readme


#: watch - Watch in-development files and automatically build them on update.
.PHONY: watch
watch: develop
	$(TOX) -e watch
