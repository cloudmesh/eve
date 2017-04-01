"""
The admin command for the REST services
"""
from __future__ import print_function

from pprint import pprint

from cloudmesh.common.util import banner
from cloudmesh.common.util import path_expand
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

from cloudmesh.rest.mongo import Mongo
from cloudmesh.rest.service import RestService

class AdminCommand(PluginCommand):
    """
    The admin command to manage the REST service
    """
    @command
    def do_admin(self, args, arguments):
        """
        ::

          Usage:
                admin [db|rest] start
                admin [db|rest] stop
                admin [db|rest] status
                admin [db|rest] info
                admin db backup
                admin db reset
                admin settings FILENAME

          Description:
               
                db start
                    starts the database service

                db stop
                    stops the database service

                db backup
                    creates a backup of the database

                db reset
                    resets the database

                rest start
                    starts the database service

                rest stop
                    stops the database service

                start
                    starts all services

                stop
                    stops all services

                settings FILENAME
                    copies the eve settings file specified by the FILENAME to
                    ~/.cloudmesh/db/settings.py and uses it upon start of the 
                    eve service. 

                With the help from the admin command it is possible to start a 
                rest service using mongodb as a backend. The objects need to be 
                defined first and configuration files need to be placed before 
                the service can be used.

                The following is show caseing the creation of objects and the 
                start of the related services.

                First, edit a file called settings.json that defines example objects 
                as documented in evegenie. An example file is included in the source 
                code fo cloudmesh.rest at 

                  https://github.com/cloudmesh/rest/blob/master/sample.json

                This example can than be integrated into the cloudmesh rest service 
                while executing the following command sequence

                  admin settings sample.json
                  
                This will generate a sample.settings.py file and copy it to 
                
                  ~/.cloudmesh/db/settings.py

                To start the services after you have defined and placed your objects 
                into the db directory, you can use the commands

                   admin start

                To stop the service yo can use the command

                   admin stop

                In case you need to add new objects you need to first reset the db, which
                while delete all existing objects in the db.

                   admin reset

                Than you need to modify your object definitions and start the server as 
                previously explained, e.g.

                    emacs sample.json  # edit the objects sample
                    admin settings sample.json 
                    admin start

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        pprint(arguments)
        #
        # TODO: use Console.msg
        #

        def _manage_service(service, arguments):
            banner(service.name)
            if arguments.stop:
                service.stop()
            elif arguments.start:
                service.start()
            elif arguments.info:
                service.info()
            print(service.status())

        if arguments.db:

            service = Mongo()
            _manage_service(service, arguments)

        elif arguments.rest:

            service = RestService()
            _manage_service(service, arguments)

        elif arguments.start or arguments.stop or arguments.status or arguments.info:

            m = Mongo()
            e = RestService()
            for service in [e, m]:
                print(service.name)
                _manage_service(service, arguments)

        elif arguments.settings:
            if arguments.FILENAME is None:
                filename = "~/.cloudmesh/db/settings.py"
            filename = path_expand(arguments.FILENAME)

            # if ends in json
            #    create settings.py file first
            #    copy settings.py to ~/.cloudmesh/db

            # e = RestService(settings=filename)
            # copying and handleing .py or .json extension  may be included in RestService method

        elif arguments.backup:

            print("not yet implemented")
            # Create backup dir and copy files into it including settings.py and sample.json
