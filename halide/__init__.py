'''
A simple app to serve static content from a directory

To serve static files from a subdirectory named ``static`` inside the parent
directory ``/path/to/static/files``, create a ``halite.conf`` with the
following config items::

    [global]
    environment: 'production'
    log.screen: True
    # log.error_file: 'halide.log'

    tree.cpapp: cherrypy.Application(cpapp.Root())

    [/]
    tools.staticdir.root = "/path/to/static/files"

    [/static]
    tools.staticdir.on = True
    tools.staticdir.dir = "static"

Run the app::

    $ cherryd -i cpapp -c halite.conf

'''
import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return '''\
<html>
    <head>
        <title>Halite</title>
    </head>

    <body>
        <h1>Halite</h1>
    </body>
</html>
'''