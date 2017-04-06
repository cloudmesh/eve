"""
The admin command for the REST services
"""
from __future__ import print_function

from pprint import pprint

from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

from cloudmesh.rest.elements import Elements


class SchemaCommand(PluginCommand):
    """
    The admin command to manage the REST service
    """

    @command
    def do_scheam(self, args, arguments):
        """
        ::

          Usage:
            
                schema evegenie DIRECTORY FILENAME
                schema cat DIRECTORY FILENAME
                
          Description:
               

          Arguments:
              FILENAME   a filename
              DIRECTORY  the derectory where the schma objects are defined

          Options:
              -h     help

        """
        pprint(arguments)

        if arguments.schema and arguments.cat:
            directory = arguments.DIRECTORY
            filename = arguments.FILENAME
            elements = Elements(directory, filename)

        if arguments.schema and arguments.evegenie:
            # directory = arguments.DIRECTORY
            # d = glob.glob(...)
            # filename = arguments.FILENAME
            # elements = ExampleToSpec(directory, filename)


            print("Not Implemented")
