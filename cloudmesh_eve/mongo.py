# TODO: complete
# for executing shell commands please do not reinvent the whele but use

# https://github.com/cloudmesh/client/blob/master/cloudmesh_client/common/Shell.py
# if commands are missing or are not working we can fix that in cloudmesh_client

from __future__ import print_function
from cloudmesh_client.common.util import grep
from cloudmesh_client.common.Shell import Shell
import os


def log_print(msg):
    # temporarily used till we switch to real logger
    print(msg)


class mongo(object):
    def start(self, portnumber):
        """starts the mongo service."""
        print("not yet implemented")
        # subprocess.call(mongod --port portnumber)
        r = Shell.execute('sudo service mongod start'.split(' '))
        log_print('mongod  ------  running')

    def stop(self):
        """stops the mongo service."""
        r = Shell.execute('sudo service mongod stop'.split(' '))
        # subprocess.call(mongod --shutdown)
        log_print('mongodb  ------  stopped')

    def status(self, format=None):
        """returns the status of the service. if no parameter. if format
        is specified its returned in that fomat. txt, json, XML,
        allowed
        """
        output = Shell.ps = ('-A')
        if 'mongod' in output:
            log_print('mongod  ------  running')
        else:
            log_print('mongod  ------  stopped')

    def reset(self):
        """stops the service and deletes the database, restarts the service."""
        r = Shell.execute('sudo service mongod stop'.split(' '))
        log_print('mongodb  ------  stopped')

        # print("not yet implemented")
        pass

    def delete(self):
        """just deletes all data in the database"""
        log_print("not yet implemented")
        pass

    def pid(self):
        """returns the pid of the mongo db servier"""
        output = Shell.ps=('-A')
        pid = grep("mongod").strip().split(' ')[0]
        return pid

    def log(self, path):
        """sets the log file to the given path"""
        log_print("not yet implemented")
        pass

# TODO: define test programs with nosetest
