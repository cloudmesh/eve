Cloudmesh Rest
==============

cd in the directory where the json object definitisn are located
There you can create a concatenation of the jsin objects
than you can convert them to the eve settings file.

::

    cms schema cat . all.json
    cms schema convert all.json


SEE THE CLASS WEB PAGE FOR PROPER DOCUMENTAION




WE ASSUME YOU DO THIS IN A VIRTUALENV
Please note that this has only be tested on OSX. it will be straight forward to port to Linux.


REST Service
------------

Development environment for cloudmesh to define simple REST services


Install Mongo
^^^^^^^^^^^^^

::

   brew update
   brew install mongodb

   # brew install mongodb --with-openssl


Managing Mongo
^^^^^^^^^^^^^^

::

    cms admin mongo start
    cms admin mongo info
    cms admin mongo status
    cms admin mongo stop

Manageing Eve
^^^^^^^^^^^^^

EVE SERVICE COMMANDS MOT YET IMPLEMENTED


Testing
^^^^^^^
::


  make setup    # install mongo and eve
  make install  # installs the code and integrates it into cmd5
  make deploy
  make test



TO DO
^^^^^

- [ ] add logger

- [ ] finish admin logic to start/stop eve services

