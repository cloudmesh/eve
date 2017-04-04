import glob
from cloudmesh.common.util import readfile
import json

class Elements(object):

    def __init__(self, directory, filename):

        import yaml
        import os.path

        settings = {}

        for file in glob.glob(os.path.join(directory, '*.yml')):
            with open(file) as fd:
                d = yaml.load(fd)
                settings.update(d)

            with open(filename, 'w') as fd:
                json.dump(settings, fd, indent=4)
    #
    # def __init__(self, directory, filename):
    #
    #     settings = {}
    #
    #     for file in glob.glob(directory + "/*.json"):
    #         print ("F", file)
    #         content = readfile(file)
    #
    #         d = json.loads(content)
    #         print ("--------")
    #         print (d)
    #         print ("--------")
    #
    #         settings.update(d)
    #
    #     print (json.dumps(settings, indent=4))
    #
    #     with open (filename, "w") as f:
    #         f.write(json.dumps(settings, indent=4))