#
# in our rest architecture we want to interface to the backend systems while
# using a secure rest service. I
# Internally we will use the many fnctions that cloudmesh_client provides.
# Before we use them we need to implement some elementary functions
# lets first do administrative functions in an admin commond

# pseudo code: task implement

from __future__ import print_function

import os.path
import pkgutil
import pydoc
import sys
import textwrap
from cmd import Cmd

from cloudmesh_client.shell.command import command
from cloudmesh_client.shell.command import PluginCommand

import cloudmesh
from cloudmesh.rest.server. mongo import Mongo

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
                                Cloudmesh Rest Shell
              """)

    @command
    def do_info(self, args, arguments):
        """
        ::

          Usage:
                info [help]

          Description:
                info
                    provides internal info about the shell and its packages

        """
        pkgpath = os.path.dirname(cloudmesh.__file__)
        modules = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]

        print("Modules:")
        # print (modules)

        if arguments["help"]:
            for name in modules:
                p = "cloudmesh." + name

                strhelp = pydoc.render_doc(p, "Help on %s" + "\n" + 79 * "=")
                print(strhelp)

        else:
            for name in modules:
                p = "cloudmesh." + name
                print("*", p)

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
            m = Mongo()
            m.stop()
        elif arguments["db"] and arguments["start"]:

            print("PLEASE start db")
            m = Mongo()
            m.start()

        elif arguments["rest"] and arguments["start"]:

            print("PLEASE start rest")
            # m = Eve()
            # m.start()

        elif arguments["rest"] and arguments["stop"]:

            print("PLEASE stop rest")
            # m = Eve()
            # m.stop()


        elif arguments["start"]:
            m = Mongo()
            r = m.start()
            print(r)

            # start mong, start eve
            pass
        elif arguments["stop"]:
            m = Mongo()
            r = m.stop()
            print(r)

            # stop eve
            pass

        elif arguments["status"]:
            m = Mongo()
            r = m.status()
            print(r)

    def preloop(self):
        """adds the banner to the preloop"""


        lines = textwrap.dedent(self.banner).split("\n")
        for line in lines:
            # Console.cprint("BLUE", "", line)
            print(line)

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

#def main():
#    CMShell().cmdloop()

def inheritors(klass):
    subclasses = set()
    work = [klass]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses

# noinspection PyBroadException
def main():
    """cms.

    Usage:
      cms --help
      cms [--echo] [--debug] [--nosplash] [-i] [COMMAND ...]

    Arguments:
      COMMAND                  A command to be executed

    Options:
      --file=SCRIPT  -f  SCRIPT  Executes the script
      -i                 After start keep the shell interactive,
                         otherwise quit [default: False]
      --nosplash    do not show the banner [default: False]
    """

    def manual():
        print(main.__doc__)

    args = sys.argv[1:]

    arguments = {
        '--echo': '--echo' in args,
        '--help': '--help' in args,
        '--debug': '--debug' in args,
        '--nosplash': '--nosplash' in args,
        '-i': '-i' in args}

    echo = arguments["--echo"]
    if arguments['--help']:
        manual()
        sys.exit()

    for a in args:
        if a in arguments:
            args.remove(a)

    arguments['COMMAND'] = [' '.join(args)]

    commands = arguments["COMMAND"]
    if len(commands) > 0:
        if ".cm" in commands[0]:
            arguments["SCRIPT"] = commands[0]
            commands = commands[1:]
        else:
            arguments["SCRIPT"] = None

        arguments["COMMAND"] = ' '.join(commands)
        if arguments["COMMAND"] == '':
            arguments["COMMAND"] = None

    # noinspection PySimplifyBooleanCheck
    if arguments['COMMAND'] == []:
        arguments['COMMAND'] = None

    splash = not arguments['--nosplash']
    debug = arguments['--debug']
    interactive = arguments['-i']
    script = arguments["SCRIPT"]
    command = arguments["COMMAND"]

    #context = CloudmeshContext(
    #    interactive=interactive,
    #    debug=debug,
    #    echo=echo,
    #    splash=splash)

    cmd = CMShell()

    # add commands


    print (inheritors(PluginCommand))

    if script is not None:
        cmd.do_exec(script)

    try:
        if echo:
            print("cm>", command)
        if command is not None:
            cmd.precmd(command)
            stop = cmd.onecmd(command)
            cmd.postcmd(stop, command)
    except Exception as e:
        print("ERROR: executing command '{0}'".format(command))
        print(70 * "=")
        print(e)
        print(70 * "=")

    if interactive or (command is None and script is None):
        cmd.cmdloop()





if __name__ == '__main__':
    main()


