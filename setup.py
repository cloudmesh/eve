#!/usr/bin/env python
# ----------------------------------------------------------------------- #
# Copyright 2017, Gregor von Laszewski, Indiana University                #
#                                                                         #
# Licensed under the Apache License, Version 2.0 (the "License"); you may #
# not use this file except in compliance with the License. You may obtain #
# a copy of the License at                                                #
#                                                                         #
# http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#
# See the License for the specific language governing permissions and     #
# limitations under the License.                                          #
# ------------------------------------------------------------------------#

from setuptools import find_packages, setup
import io

def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split()


#requiers = readfile ('requirements.txt')
#git+git://github.com/nicolaiarocci/eve.git@develop
requiers = """
pygments
tox
detox
coverage
flake8
cloudmesh_client
""".split("\n")

dependency_links = ['http://github.com/nicolaiarocci/eve.git@develop']

version = readfile("VERSION")[0].strip()
readme = readfile('README.rst')

NAME = "cloudmesh"
DESCRIPTION = "A REST service for cloudmesh"
AUTHOR = "Gregor von Laszewski, I524"
AUTHOR_EMAIL = "laszewski@gmail.com"
URL = "https://github.com/cloudmesh/rest"
LONG_DESCRIPTION = "\n".join(readme)


setup \
(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    version="1.0.0",
    license="Apache 2.0",
    url=URL,
    packages=find_packages(),
    #package_data={
    #    "cloudmesh.data": [
    #        "templates/cloudmesh/data.txt",
    #    ]
    #},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=requiers,
    dependency_links = dependency_links,
    # test_suite="runtests.runtests",
    tests_require=[
        "flake8",
        "coverage",
    ],
    zip_safe=False,
    namespace_packages=['cloudmesh'],
    entry_points={
        'console_scripts': [
            'cms = cloudmesh.rest.shell.shell:main',
            'eved = cloudmesh.rest.server.service:main',
        ],
    },
)
