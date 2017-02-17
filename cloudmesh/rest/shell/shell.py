#
# in our rest architecture we want to interface to the backend systems while
# using a secure rest service. I
# Internally we will use the many fnctions that cloudmesh_client provides.
# Before we use them we need to implement some elementary functions
# lets first do administrative functions in an admin commond

# pseudo code: task implement

from __future__ import print_function

import textwrap
from cmd import Cmd

from cloudmesh_client.shell.command import command


class CMShell(Cmd):

    prompt = 'cms> '
    banner = textwrap.dedent("""
              +=======================================================+
              .   ____ _                 _                     _      .
              .  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   .
              . | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  .
              . | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | .
              .  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| .
              +=======================================================+
                                   Cloudmesh Shell
              """)

    @command
    def do_admin(self, args, arguments):
        """
        ::

          Usage:
                admin [db|rest] start
                admin [db|rest] stop
                admin db backup
                admin db reset

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
        if arguments["db"] and arguments["stop"]:

            print("PLEASE stop db")
            # m = Mongo()
            # m.stop()
        elif arguments["db"] and arguments["start"]:

            print("PLEASE start db")
            # m = Mongo()
            # m.start()

        elif arguments["rest"] and arguments["start"]:

            print("PLEASE start rest")
            # m = Eve()
            # m.start()

        elif arguments["rest"] and arguments["stop"]:

            print("PLEASE stop rest")
            # m = Eve()
            # m.stop()


        elif arguments["start"]:
            # start mong, start eve
            pass
        elif arguments["stop"]:
            # stop eve ; stop mongo
            pass


    # noinspection PyUnusedLocal
    def do_EOF(self, args):
        """
        ::

            Usage:
                EOF

            Description:
                Command to the shell to terminate reading a script.
        """
        return True

    # noinspection PyUnusedLocal
    def do_quit(self, args):
        """
        ::

            Usage:
                quit

            Description:
                Action to be performed whne quit is typed
        """
        return True

    do_q = do_quit

    def emptyline(self):
        return

def main():
    CMShell().cmdloop()


if __name__ == '__main__':
    main()


