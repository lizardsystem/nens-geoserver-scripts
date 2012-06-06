# Copyright Nelen & Schuurmans 2012.
# Distributed under the terms of the GPL, version 3. See the file LICENSE.rst.

"""This module does two things: it reads the config file (by default,
~/geoserver.cfg), and it parses command line arguments.

Command line arguments can be accessed with the arg() function, config
options with the get() option.
"""

import argparse
import ConfigParser
import os
import sys

_parser = argparse.ArgumentParser()
_parser.add_argument("server",
                     help="which server configuration to use")
_parser.add_argument("-c", "--configfile",
                     help="path to config file",
                     default="~/geoserver.cfg")
_args = _parser.parse_args()

CONFIG_FILE = os.path.expanduser(_args.configfile)

CONFIG = {}


def read_config_file():
    parser = ConfigParser.ConfigParser()
    parser.read(CONFIG_FILE)

    for section in parser.sections():
        CONFIG[section] = dict(parser.items(section))

read_config_file()


def get():
    if _args.server in CONFIG:
        options = CONFIG[_args.server]

        return {
            'url': options.get('url', ''),
            'username': options.get('username', ''),
            'password': options.get('password', ''),
            }
    else:
        print "No such server configuration: %s." % (_args.server,)
        sys.exit(1)
