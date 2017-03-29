{ pkgs
, buildPythonPackage
, fetchurl
, extras ? []
, ...
}:

with pkgs;
with pythonPackages;

rec {

  cerberus = buildPythonPackage {
      name = "cerberus-0.9.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/c1/7a/65f3aa48279cda81208ccca4c932e63fedaf02f80f1fb6a482a7b8d8f239/Cerberus-0.9.2.tar.gz";
        sha256 = "b122c7b2cbf856ea2587e187fac968fc8dcd49d47aa1f239abd9eaa0ed86a7ce";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  click = buildPythonPackage {
      name = "click-6.7";
      src = fetchurl {
        url = "https://pypi.python.org/packages/95/d9/c3336b6b5711c3ab9d1d3a80f1a3e2afeb9d8c02a7166462f6cc96570897/click-6.7.tar.gz";
        sha256 = "f15516df478d5a56180fbf80e68f206010e6d160fc39fa508b65e035fd75130b";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  configparser = buildPythonPackage {
      name = "configparser-3.5.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/7c/69/c2ce7e91c89dc073eb1aa74c0621c3eefbffe8216b3f9af9d3885265c01c/configparser-3.5.0.tar.gz";
        sha256 = "5308b47021bc2340965c371f0f058cc6971a04502638d4244225c49d80db273a";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  coverage = buildPythonPackage {
      name = "coverage-4.3.4";
      src = fetchurl {
        url = "https://pypi.python.org/packages/6e/33/01cb50da2d0582c077299651038371dba988248058e03c7a7c4be0c84c40/coverage-4.3.4.tar.gz";
        sha256 = "eaaefe0f6aa33de5a65f48dd0040d7fe08cac9ac6c35a56d0a7db109c3e733df";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  detox = buildPythonPackage {
      name = "detox-0.10.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/43/09/104095be078149e441ef926112521ec4bb5796a7828850167f7d0d95ab50/detox-0.10.0.tar.gz";
        sha256 = "33b704c2a5657366850072fb2aa839df14dd2e692c0c1c2642c3ac30d5c0baec";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ tox eventlet ];
      doCheck = false;
    }
    ;
  enum-compat = buildPythonPackage {
      name = "enum-compat-0.0.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/95/6e/26bdcba28b66126f66cf3e4cd03bcd63f7ae330d29ee68b1f6b623550bfa/enum-compat-0.0.2.tar.gz";
        sha256 = "939ceff18186a5762ae4db9fa7bfe017edbd03b66526b798dd8245394c8a4192";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ enum34 ];
      doCheck = false;
    }
    ;
  enum34 = buildPythonPackage {
      name = "enum34-1.1.6";
      src = fetchurl {
        url = "https://pypi.python.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl";
        sha256 = "6bd0f6ad48ec2aa117d3d141940d484deccda84d4fcd884f5c3d93c23ecd8c79";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  eve = buildPythonPackage {
      name = "eve-0.7.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/0d/a7/aba6602133893103c6695ec532bb008de520be9c85b0ffffa17d23270732/Eve-0.7.2.tar.gz";
        sha256 = "b0f1cebeec71c58d3b732f4655412f60ac75f25194ff29aa25f68ee1d5ff1760";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ cerberus events simplejson flask-pymongo ];
      doCheck = false;
    }
    ;
  eventlet = buildPythonPackage {
      name = "eventlet-0.20.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/5b/3a/a72c3c03382c4c32bfafdb5cf51979d066caa496c8e9d8ecbb9f9153bda8/eventlet-0.20.1-py2.py3-none-any.whl";
        sha256 = "d52b953b66d488e5aa1e4181c21f61e8a8a35255de49b73e7b35c22290cb9e29";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ enum-compat greenlet ];
      doCheck = false;
    }
    ;
  events = buildPythonPackage {
      name = "events-0.2.2";
      src = fetchurl {
        url = "https://pypi.python.org/packages/56/81/4d1d71a8553d8f294560b9a6f9fe584e65289c9f6b8753b5d352511c2d58/Events-0.2.2.tar.gz";
        sha256 = "1d09f09d5ab496815e9bfd2194546d75fd54b8e76703f4fd83314080de94b86d";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  flake8 = buildPythonPackage {
      name = "flake8-3.3.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/cd/a6/1fe37679be3b224c96d8b64782d724d6a2c4212c8ddd914572fb8317a298/flake8-3.3.0-py2.py3-none-any.whl";
        sha256 = "83905eadba99f73fbfe966598aaf1682b3eb6755d2263c5b33a4e8367d60b0d1";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [ pyflakes enum34 pycodestyle configparser mccabe ];
      doCheck = false;
    }
    ;
  flask = buildPythonPackage {
      name = "flask-0.12";
      src = fetchurl {
        url = "https://pypi.python.org/packages/4b/3a/4c20183df155dd2e39168e35d53a388efb384a512ca6c73001d8292c094a/Flask-0.12.tar.gz";
        sha256 = "93e803cdbe326a61ebd5c5d353959397c85f829bec610d59cb635c9f97d7ca8b";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ itsdangerous werkzeug jinja2 click ];
      doCheck = false;
    }
    ;
  flask-pymongo = buildPythonPackage {
      name = "flask-pymongo-0.4.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/04/41/7070930eb72f79c69efaa7289635160b20e568b873428304e19dff235244/Flask-PyMongo-0.4.1.tar.gz";
        sha256 = "75862daece1c979a9eab5f9d1e32eb781775842273b629ae5d1cb28e6953df78";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ flask pymongo ];
      doCheck = false;
    }
    ;
  greenlet = buildPythonPackage {
      name = "greenlet-0.4.12";
      src = fetchurl {
        url = "https://pypi.python.org/packages/be/76/82af375d98724054b7e273b5d9369346937324f9bcc20980b45b068ef0b0/greenlet-0.4.12.tar.gz";
        sha256 = "e4c99c6010a5d153d481fdaf63b8a0782825c0721506d880403a3b9b82ae347e";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  itsdangerous = buildPythonPackage {
      name = "itsdangerous-0.24";
      src = fetchurl {
        url = "https://pypi.python.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz";
        sha256 = "cbb3fcf8d3e33df861709ecaf89d9e6629cff0a217bc2848f1b41cd30d360519";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  jinja2 = buildPythonPackage {
      name = "jinja2-2.9.5";
      src = fetchurl {
        url = "https://pypi.python.org/packages/71/59/d7423bd5e7ddaf3a1ce299ab4490e9044e8dfd195420fc83a24de9e60726/Jinja2-2.9.5.tar.gz";
        sha256 = "702a24d992f856fa8d5a7a36db6128198d0c21e1da34448ca236c42e92384825";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ markupsafe ];
      doCheck = false;
    }
    ;
  markupsafe = buildPythonPackage {
      name = "markupsafe-0.23";
      src = fetchurl {
        url = "https://pypi.python.org/packages/c0/41/bae1254e0396c0cc8cf1751cb7d9afc90a602353695af5952530482c963f/MarkupSafe-0.23.tar.gz";
        sha256 = "a4ec1aff59b95a14b45eb2e23761a0179e98319da5a7eb76b56ea8cdc7b871c3";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  mccabe = buildPythonPackage {
      name = "mccabe-0.6.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/87/89/479dc97e18549e21354893e4ee4ef36db1d237534982482c3681ee6e7b57/mccabe-0.6.1-py2.py3-none-any.whl";
        sha256 = "ab8a6258860da4b6677da4bd2fe5dc2c659cff31b3ee4f7f5d64e79735b80d42";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  pluggy = buildPythonPackage {
      name = "pluggy-0.4.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/38/e2/b23434f4030bbb1af3bcdbb2ecff6b11cf2e467622446ce66a08e99f2ea9/pluggy-0.4.0.zip";
        sha256 = "dd841b5d290b252cf645f75f3bd37ceecfa0f36394ab313e4f785fe68a4081a4";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  psutil = buildPythonPackage {
      name = "psutil-5.2.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/b8/47/c85fbcd23f40892db6ecc88782beb6ee66d22008c2f9821d777cb1984240/psutil-5.2.1.tar.gz";
        sha256 = "fe0ea53b302f68fca1c2a3bac289e11344456786141b73391ed4022b412d5455";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  py = buildPythonPackage {
      name = "py-1.4.33";
      src = fetchurl {
        url = "https://pypi.python.org/packages/2a/a5/139ca93a9ffffd9fc1d3f14be375af3085f53cc490c508cf1c988b886baa/py-1.4.33.tar.gz";
        sha256 = "1f9a981438f2acc20470b301a07a496375641f902320f70e31916fe3377385a9";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  pycodestyle = buildPythonPackage {
      name = "pycodestyle-2.3.1";
      src = fetchurl {
        url = "https://pypi.python.org/packages/e4/81/78fe51eb4038d1388b7217dd63770b0f428370207125047312886c923b26/pycodestyle-2.3.1-py2.py3-none-any.whl";
        sha256 = "6c4245ade1edfad79c3446fadfc96b0de2759662dc29d07d80a6f27ad1ca6ba9";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  pyflakes = buildPythonPackage {
      name = "pyflakes-1.5.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/5b/b7/dcd6ebc826065ca4ccd2406aac4378e1df6eb91124625d45d520219932a1/pyflakes-1.5.0.tar.gz";
        sha256 = "aa0d4dff45c0cc2214ba158d29280f8fa1129f3e87858ef825930845146337f4";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  pygments = buildPythonPackage {
      name = "pygments-2.2.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/02/ee/b6e02dc6529e82b75bb06823ff7d005b141037cb1416b10c6f00fc419dca/Pygments-2.2.0-py2.py3-none-any.whl";
        sha256 = "78f3f434bcc5d6ee09020f92ba487f95ba50f1e3ef83ae96b9d5ffa1bab25c5d";
      };
      format = "wheel";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  pymongo = buildPythonPackage {
      name = "pymongo-3.4.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/82/26/f45f95841de5164c48e2e03aff7f0702e22cef2336238d212d8f93e91ea8/pymongo-3.4.0.tar.gz";
        sha256 = "d359349c6c9ff9f482805f89e66e476846317dc7b1eea979d7da9c0857ee2721";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  simplejson = buildPythonPackage {
      name = "simplejson-3.10.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/40/ad/52c1f3a562df3b210e8f165e1aa243a178c454ead65476a39fa3ce1847b6/simplejson-3.10.0.tar.gz";
        sha256 = "953be622e88323c6f43fad61ffd05bebe73b9fd9863a46d68b052d2aa7d71ce2";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  tox = buildPythonPackage {
      name = "tox-2.6.0";
      src = fetchurl {
        url = "https://pypi.python.org/packages/8a/fa/f54d9623b623168fb2a0ae301f27a0bdd3f4a3b74e7232d3e537d84e3191/tox-2.6.0.tar.gz";
        sha256 = "916498d2971f44a76baf3773a700f775c2f51aa6cc20be1828309148fc412252";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [ py pluggy virtualenv ];
      doCheck = false;
    }
    ;
  werkzeug = buildPythonPackage {
      name = "werkzeug-0.11.15";
      src = fetchurl {
        url = "https://pypi.python.org/packages/fe/7f/6d70f765ce5484e07576313897793cb49333dd34e462488ee818d17244af/Werkzeug-0.11.15.tar.gz";
        sha256 = "455d7798ac263266dbd38d4841f7534dd35ca9c3da4a8df303f8488f38f3bcc0";
      };
      format = "setuptools";
      buildInputs = [  ];
      propagatedBuildInputs = [  ];
      doCheck = false;
    }
    ;
  

}