Cloudmesh Rest
==============

WE ASSUME YOU DO THIS IN A VIRTUALENV

REST Service
------------

Development environment for cloudmesh to define simple REST services


Install Mongo
^^^^^^^^^^^^^

::
   
   brew update
   brew install mongodb

   # brew install mongodb --with-openssl


Create db dir
^^^^^^^^^^^^^

::

   mkdir -p ~/.cloudmesh/data/db
   mongod --dbpath ~/.cloudmesh/data/db --bind_ip 127.0.0.1


Try it out
^^^^^^^^^^

Just uses firt python environment::

  make deploy
  make test

testing validation
^^^^^^^^^^^^^^^^^^

python schema.py


TO DO
^^^^^

- [ ] insert data

curl -d '{"name": "myCLuster",	"label": "c0","ip": "127.0.0.1","memoryGB": 16}' -H 'Content-Type: application/json'  http://127.0.0.1:5000/computer

- [ ] add logger

- [ ] finish admin logic to start/stop mongo and eve services

Cloudmesh Rest SHell
---------------------

uninstall previous versions of cloudmeh shell

do this multiple times toll you get a warning it can not find it::

  pip uninstall cloudmesh_client

Install cloudmesh_client::

  pip install cloudmesh_client

install the rest shell::

  python setup.py install

Run the shell::

   cms

Do help on the admin command

   (cmd) admin help

Todo:

- [ ] add prompt cms>
- [ ] add EOF
- [ ] add q qommand to quit
- [ ] implement the logic for the admin command
