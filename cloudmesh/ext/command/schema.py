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
            
                schema DIRECTORY FILENAME
                
          Description:
               

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        pprint(arguments)

        if arguments.schema:
            directory = arguments.DIRECTORY
            filename = arguments.FILENAME
            elements = Elements(directory, filename)
