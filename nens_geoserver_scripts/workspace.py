# Copyright Nelen & Schuurmans 2012.
# Distributed under the terms of the GPL, version 3. See the file LICENSE.rst.

from geoserver import catalog

from nens_geoserver_scripts import config


def main():
    parser = config.get_arg_parser("Ping a server.")
    parser.add_argument("workspace", nargs='?', default=None)
    config.parse(parser)

    cat = catalog.Catalog(**config.get())

    workspace_arg = config.get_args().workspace

    if config.get_args().workspace:
        workspace = cat.get_workspace(workspace_arg)

        stores = cat.get_stores(workspace=workspace)
        print("Workspace {0} contains {1} stores:"
              .format(workspace.name, len(stores)))

        for store in stores:
            print "    %s" % (store.name,)

            resources = store.get_resources()
            for resource in resources:
                print "        %s" % (str(resource.name),)
    else:
        workspaces = cat.get_workspaces()

        if not workspaces:
            print "No workspaces found."
        else:
            print "%d workspaces found:" % (len(workspaces),)
            for workspace in workspaces:
                print "    {0}".format(workspace.name)

if __name__ == '__main__':
    main()
