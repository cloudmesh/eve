#!/usr/bin/env python

from eve import Eve
import imp
import os

# http://stackoverflow.com/questions/301134/dynamic-module-import-in-python
#once this works we want to move load_from_file to common.util
def load_from_file(filepath):
    class_inst = None
    expected_class = 'MyClass'

    mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    if hasattr(py_mod, expected_class):
        class_inst = getattr(py_mod, expected_class)()

    return class_inst

class Service(object):

    def load_settings(filename):
        self.settings = filename
        load_from_file(filename)
        # dynamically import settings form the filename specified
        #from cloudmesh.rest.server.settings import eve_settings
        
    def __init__(self, settings=None):
        # TODO: reads the OBJECT.settings.py file and sets up the eve service withi it

        # if settings is None:
        # settings = path_expand("~/.cloudmesh/db/object.settings.py")
        self.load_settings(settings)

    def start(self):
        # TODO: implement
        print("NOT YET IMPLEMENTED")

    def stop(self):
        # TODO: implement
        print("NOT YET IMPLEMENTED")

    def status(self):
        # TODO: implement
        print("NOT YET IMPLEMENTED")

    def reset(self, settings=None):
        # TODO: implement
        print("NOT YET IMPLEMENTED")
        # reinitializes eve with a new settings

    def run(self):
        self.app = Eve(settings=self.settings)
        self.app.run()
        
        
def main():
    app = Eve(settings=eve_settings)
    app.run()

if __name__ == '__main__':
    main()


