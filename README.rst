##########
minventory
##########

`minventory` provides RESTful IT management service.

Basically, it consists in:

* an API, i.e. a server-side application that holds data about machines and IP
  addresses;

* an UI, i.e. a client-side application that displays data using server's API.


****************
Running the demo
****************

* Get the code: ``git clone git@github.com:benoitbryon/minventory.git && cd minventory/``
* Run API: ``make api`` (`virtualenv`_ and Python2 recommended)

Optionally, you can load demo data with ``make loaddata``.

.. note:: At this stage, UI hardcodes API's endpoint, i.e. localhost:8000.

Inspect the service:

* UI lives in file ``ui.html`` in code's root folder. Just open it in a
  browser.
* API is served at http://localhost:8000.
* API documentation lives at http://localhost:8000/docs/.


******
Status
******

`minventory` is at early prototype stage!

Primary goal is to meet expectations of project's initial users, so that they
can easily import existing data, review the advantages of a RESTful API, then
prioritize their needs before further development.


**********
Ressources
**********

* Code repository: https://github.com/benoitbryon/minventory


.. _`virtualenv`: https://virtualenv.pypa.io/
