#
# in our rest architecture we want to interface to the backend systems while
# using a secure rest service. I
# Internally we will use the many fnctions that cloudmesh_client provides.
# Before we use them we need to implement some elementary functions
# lets first do administrative functions in an admin commond

# pseudo code: task implement

from __future__ import print_function
from cloudmesh_client.shell.command import command
from cmd import Cmd
from cloudmesh.rest.command.admin import admin

class CMRestCmd(Cmd):


    @command
    def do_admin(self, args, arguments):
        """
        ::

          Usage:
                admin start
                admin stop
                admin reset
                admin db start
                admin db stop
                admin db backup
                admin db reset
                admin rest start
                admin rest stop

          Description:
                db start
                    starts the database service

                db stop
                    stops the database service

                db backup
                    creates abackup of the database

                db reset
                    resets the database

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)
        if "admin" in arguments and "start" in arguments:
            admin.start()
        elif "admin" in arguments and "stop" in arguments:
            admin.stop()
        ## add the others

if __name__ == '__main__':

        # open question should be we have single command "admin" and place both
        # functions in it



