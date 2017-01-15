Install Mongo
-----------

::
   
   brew update
   brew install mongodb

   # brew install mongodb --with-openssl


Create db dir
----------

::

   mkdir -p ~/.cloudmesh/data/db
   mongod --dbpath ~/.cloudmesh/data/db --bind_ip 127.0.0.1


Try it out
-------

make deploy
make test

testing validation
--------------

python schema.py


