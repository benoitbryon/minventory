#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line


def main(argv=None):
    """Execute Django command line within the context of project."""
    if argv is None:
        argv = sys.argv
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "{package}.settings".format(package=__package__))
    execute_from_command_line(argv)


if __name__ == "__main__":
    main()
