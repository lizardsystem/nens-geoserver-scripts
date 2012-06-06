# Copyright Nelen & Schuurmans 2012.
# Distributed under the terms of the GPL, version 3. See the file LICENSE.rst.

from geoserver import catalog

from nens_geoserver_scripts import config

def main():
    cat = catalog.Catalog(**config.get())
    print "Server called successfully. %d layers present." % (len(cat.get_layers()),)

if __name__ == '__main__':
    main()
