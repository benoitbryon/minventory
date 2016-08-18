#!/usr/bin/env python
import argparse

from eve import Eve
import yaml


def main():
    """Command line interface (CLI) to run web server."""
    parser = argparse.ArgumentParser(description='Inventory API server.')
    parser.add_argument(
        '--settings',
        dest='settings',
        action='store',
        default='etc/{}.yaml'.format(__package__),
        help='Path to YAML settings file.')
    args = parser.parse_args()

    with open(args.settings) as settings_file:
        settings_dict = yaml.load(settings_file)

    app = Eve(settings=settings_dict)
    app.run()


if __name__ == "__main__":
    main()
