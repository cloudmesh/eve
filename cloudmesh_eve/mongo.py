# TODO: complete
# for executing shell commands please do not reinvent the whele but use

# https://github.com/cloudmesh/client/blob/master/cloudmesh_client/common/Shell.py
# if commands are missing or are not working we can fix that in cloudmesh_client

from __future__ import print_function

import os


def log_print(msg):
    # temporarily used till we switch to real logger
    print(msg)


class mongo(object):
    def start(self, portnumber):
        """starts the mongo service."""
        print("not yet implemented")
        # subprocess.call(mongod --port portnumber)
        os.system('sudo service mongod start')
        log_print('mongod  ------  running')

    def stop(self):
        """stops the mongo service."""
        os.system('sudo service mongod stop')
        # subprocess.call(mongod --shutdown)
        log_print('mongodb  ------  stopped')

    def status(self, format=None):
        """returns the status of the service. if no parameter. if format
        is specified its returned in that fomat. txt, json, XML,
        allowed
        """
        output = commands.getoutput('ps -A')
        if 'mongod' in output:
            log_print('mongod  ------  running')
        else:
            log_print('mongod  ------  stopped')

    def reset(self):
        """stops the service and deletes the database, restarts the service."""
        os.system('sudo service mongod stop')
        log_print('mongodb  ------  stopped')

        # print("not yet implemented")
        pass

    def delete(self):
        """just deletes all data in the database"""
        log_print("not yet implemented")
        pass

    def pid(self):
        """returns the pid of the mongo db servier"""
        str = commands.getoutput("ps -A | grep mongod")
        charater = str.strip();
        log_print(charater.split(" ")[0])

    def log(self, path):
        """sets the log file to the given path"""
        log_print("not yet implemented")
        pass

# TODO: define test programs with nosetest
