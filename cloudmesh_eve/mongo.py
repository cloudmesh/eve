# TODO: complete
# for executing shell commands please do not reinvent the whele but use

# https://github.com/cloudmesh/client/blob/master/cloudmesh_client/common/Shell.py
# if commands are missing or are not working we can fix that in cloudmesh_client

import subprocess
import commands
import os
from pymongo import MongoClient

class mongo(object):

    def start(portnumber):
        os.system('sudo service mongod start')
	output1 = commands.getoutput('ps -A')
	if 'mongod' in output1 :
	    print 'mongod  ------  running'
	else:
	    os.system("systemctl start mongodb");
	    output2 = commands.getoutput('ps -A')
	    if 'mongod'  in output2:
		print 'mongod  ------  running'
	    else:
		print 'mongod  ------  stopped'


    def stop():
        os.system('sudo service mongod stop')
	output1 = commands.getoutput('ps -A')
	if 'mongod' in output1 :
	    os.system("systemctl stop mongodb");
	    output2 = commands.getoutput('ps -A')
	    if 'mongod' in output2:
		print 'mongod  ------  running'
	    else:
		print 'mongod  ------  stopped'
	else:
	    status="stopped"
	    print 'mongod  ------  stopped'



    def status(format=None):
        """returns the status of the service. if no parameter. if format
        is specified its returned in that fomat. txt, json, XML,
        allowed
        """
	output = commands.getoutput('ps -A')
	if 'mongod' in output :
	    print 'mongod  ------  running'
	else:
            print 'mongod  ------  stopped'


    def reset(databasename):
        client= MongoClient(host='localhost',port=27017)
	client.drop_database(databasename);
	os.system('sudo service mongod stop')
	# os.system('sudo service mongod start')
	output = commands.getoutput('ps -A')
	if 'mongod' in output :
	    print 'mongod  ------  running'
	else:
	    print 'mongod  ------  stopped'


	#restarting the service
	# os.system('sudo service mongod restart')
	# output1 = commands.getoutput('ps -A')
	# if 'mongod' in output1 :
	#     print 'mongod  ------  running'
	# else:
	#     print 'mongod  ------  stopped'


	#stopping the service
	os.system('sudo service mongod stop')
	output2= commands.getoutput('ps -A')
	if 'mongod' in output2 :
	    os.system("systemctl stop mongodb");
	    output21 = commands.getoutput('ps -A')
	    if 'mongod' in output21:
		print 'mongod  ------  running'
	    else:
		print 'mongod  ------  stopped'
	else:
	    status="stopped"
	    print 'mongod  ------  stopped'

	#starting the service
	os.system('sudo service mongod start')
	output3 = commands.getoutput('ps -A')
	if 'mongod' in output3 :
	    print 'mongod  ------  running'
	else:
	    os.system("systemctl start mongodb");
	    output31 = commands.getoutput('ps -A')
	    if 'mongod'  in output31:
		print 'mongod  ------  running'
	    else:
		print 'mongod  ------  stopped'




    def delete():
        """just deletes all data in the database"""
        print("not yet implemented")
        pass

    
    def pid():
        """returns the pid of the mongo db servier"""
	str= commands.getoutput("ps -A | grep mongod")
	charater = str.strip();
	print (charater.split(" ")[0])
        
	
    def log(path):
        """sets the log file to the given path"""
        print("not yet implemented")
        pass
    
#TODO: define test programs with nosetest


