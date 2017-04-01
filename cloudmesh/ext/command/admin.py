from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.rest.mongo import Mongo
from cloudmesh.rest.service import Service


class AdminCommand(PluginCommand):

    @command
    def do_admin(self, args, arguments):
        """
        ::

          Usage:
                admin [db|rest] start
                admin [db|rest] stop
                admin db backup
                admin db reset
                admin status
                admin settings FILENAME

          Description:
               
                db start
                    starts the database service

                db stop
                    stops the database service

                db backup
                    creates abackup of the database

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
                    copies the eve settings file speccified by the FILENAME to
                    ~/.cloudmesh/db/settings.py and uses it upon start of the 
                    eve service. 

                With the help from the admin command it is possible to start a 
                rest service using mongodb as a backend. The objects need to be 
                defined first and configuration files need to be placed before 
                the service can be used.

                The following is showcaseing the creation of objects and the 
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
        arguments = dotdict(arguments)
        print(arguments)
        if arguments.db and arguments.stop:

            print("PLEASE stop db")
            # m = Mongo()
            # m.stop()

        elif arguments.db and arguments.start:

            print("PLEASE start db")

            #m = Mongo()
            #m.start()

        elif arguments.rest and arguments.start:

            print("PLEASE start rest")
            # if db not started start it
            # m = Eve()
            # m.start()

        elif arguments.rest and arguments.stop:

            print("PLEASE stop rest")
            # m = Eve()
            # m.stop()


        elif arguments.start:
            #m = Mongo()
            #r = m.start()
            print(r)

            # start mong, start eve
            pass
        elif arguments.stop:
            #m = Mongo()
            #r = m.stop()
            print(r)

            # stop eve
            pass

        elif arguments.status:
            #m = Mongo()
            #r = m.status()
            print(r)



