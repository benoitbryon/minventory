"""Root loader for Django settings.

Settings are loaded from the following locations, in order:

* ``minventoryapi.settings.default`` module;
* YAML file as configured as environment variable DJANGO_SETTINGS_FILE

"""
import os

from django_confit import load_file, load_module


# Default conventions depend on sys.platform.
settings_file = os.environ.get(
    'DJANGO_SETTINGS_FILE',
    os.path.join('etc', 'minventoryapi.yaml'),
)

# Load settings from conventional locations.
raw_settings = {}
raw_settings.update(load_module('minventoryapi.settings.default'))
raw_settings.update(load_file(open(settings_file)))

# Update globals, because that's the way Django uses DJANGO_SETTINGS_MODULE.
globals().update(raw_settings)
