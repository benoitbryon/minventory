# Reference card for usual actions in development environment.
#
# For standard installation, see INSTALL.
# For details about development environment, see CONTRIBUTING.rst.
#


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
	pip install -e .
	minventoryapi migrate


#: api - Run API's demo server.
.PHONY: api
api: develop
	minventoryapi runserver 0.0.0.0:8000


#: ui - Run UI's demo server.
ui:
	echo "UI is currently made of one static file. Just open 'ui.html' in your browser."


#: loaddata - Backup current data then load demo data.
loaddata: dumpdata
	minventoryapi loaddata demo.json


#: dumpdata - Backup data.
dumpdata:
	mkdir -p var
	minventoryapi dumpdata --indent=4 --format=json inventory > var/data-`date -Iseconds`.json
