# TODO: complete
# for executing shell commands please do not reinvent the whele but use

# https://github.com/cloudmesh/client/blob/master/cloudmesh_client/common/Shell.py
# if commands are missing or are not working we can fix that in cloudmesh_client

from __future__ import print_function

import os

from cloudmesh_client.common.Shell import Shell
from cloudmesh_client.common.util import grep
import shutil
import errno
from pymongo import MongoClient

def log_print(msg):
    # temporarily used till we switch to real logger
    print('mongod:' + msg)

def create_dir(path):
    os.system("mkdir -p " + path)

class Mongo(object):
    """
    Manage mongod service.
    """

    def __init__(self, port=27017):
        """
        sets up a mongo d service
        :param port: the prort number. default set to 5000
        """
        self.parameters = {}
        self.parameters['port'] = port
        self.parameters['dbpath'] = "~/.cloudmesh/data/db"
        self.parameters['bind_ip'] = "127.0.0.1"
        self.parameters['logpath'] = "~/.cloudmesh/data/mongo.log"
        create_dir(self.parameters['dbpath'])
        print(self.parameters)


    def clean(self):
        """
        Removes the database and the log files
        :return:
        """
        shutil.rmtree(self.parameters['dbpath'])
        shutil.rmtree(self.parameters['logpath'])
        create_dir(self.parameters['dbpath'])


    def kill(self):
        """
        killall mongod
        :return:
        """
        os.system("killall mongod")
        self.clean()


    def start(self):
        """starts the mongo service."""
        command = 'mongod --port {port} -dbpath {dbpath} -bind_ip {bind_ip} --fork --logpath {logpath}' \
            .format(**self.parameters)
        command_list = command.split(' ')
        create_dir(self.parameters['dbpath'])
        print(command)
        os.system("ulimit -n 1024")
        os.system(command)

        # print (command_list)
        # r = Shell.execute(command)

        # print(r)
        log_print('started')
        self.status()

    def stop(self):
        """stops the mongo service."""
        r = Shell.execute('mongod stop'.split(' '))
        print(r)
        # subprocess.call(mongod --shutdown)
        log_print('stopped')
        self.status()        

    def status(self, format=None):
        """returns the status of the service. if no parameter. if format
        is specified its returned in that fomat. txt, json, XML,
        allowed
        """
        output = Shell.ps = ('-A')
        print (output)
        if 'mongod' in output:
            log_print('running')
        else:
            log_print('stopped')

    def reset(self):
        """stops the service and deletes the database, restarts the service."""
        r = Shell.execute('mongod stop'.split(' '))
        print (r)
        log_print('stopped')
        # client.drop_database(databasename); how is this differentfrom deleting the collection?

        # print("not yet implemented")


    def delete(self):
        """deletes all data in the database."""
        try:
            client = MongoClient(host='localhost', port=self.parameters['port'] )
            # TODO: bug database is not defined
			db=client.get_database(database)
            collectionsnames = db.collection_names()

            for singlecollectionname in collectionsnames:
                log_print("deleting: " + singlecollectionname)
                db.get_collection(singlecollectionname).remove({})

        # BUG EXCEPTION MISSING
        except:
            log_print("problem deleting")

    def pid(self):
        """returns the pid of the mongo db servier"""
        """ cloudmesh has a working code for that no need to reinvent the wheel"""
        output = Shell.ps=('-A')
        print (output)
        pid = grep("mongod").strip().split(' ')[0]
        return pid

    def log(self, path):
        """sets the log file to the given path"""
        self.parameters['logpath'] = path  # TODO: define test programs with nosetest

if __name__ == "__main__":
    m = Mongo()
    m.start()
