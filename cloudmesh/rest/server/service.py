#!/usr/bin/env python

from eve import Eve

from cloudmesh.rest.server.settings import eve_settings

def main():
    app = Eve(settings=eve_settings)
    app.run()

if __name__ == '__main__':
    main()


