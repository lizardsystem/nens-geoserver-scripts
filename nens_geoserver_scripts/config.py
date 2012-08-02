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


args = None


def hack_httplib():
    """gsconfig fails when dealing with store names (etc) that have
    spaces in their names, because it doesn't quote URLs. This gross
    hack makes sure they do. It will fail once properly encoded URLs
    are used, because then they'll be encoded twice."""

    from httplib2 import Http
    old_request = Http.request

    def request(self, url, *args, **kwargs):
        import urllib
        url = urllib.quote(url, safe=':/')
        return old_request(self, url, *args, **kwargs)
    Http.request = request
hack_httplib()


def get_arg_parser(description=None):
    parser = argparse.ArgumentParser(description)
    parser.add_argument("server",
                         help="which server configuration to use")
    parser.add_argument("-c", "--configfile",
                         help="path to config file",
                         default="~/geoserver.cfg")
    return parser


def parse(parser):
    global args
    args = parser.parse_args()
    return args


def get_args():
    return args


def read_config_file():
    config_file = os.path.expanduser(args.configfile)
    parser = ConfigParser.ConfigParser()
    parser.read(config_file)

    config = dict()
    for section in parser.sections():
        config[section] = dict(parser.items(section))

    return config


def get():
    config = read_config_file()
    server = args.server

    if server in config:
        options = config[server]

        return {
            'service_url': options.get('url', ''),
            'username': options.get('username', ''),
            'password': options.get('password', ''),
            }
    else:
        print "No such server configuration: %s." % (server,)
        sys.exit(1)
