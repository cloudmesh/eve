import glob
import json

class Elements(object):
    def __init__(self, directory, filename, kind):

        import yaml
        import os.path

        settings = {}
        if kind is "yml":
            for file in glob.glob(os.path.join(directory, '*.yml')):
                with open(file) as fd:
                    d = yaml.load(fd)
                    settings.update(d)
        elif kind is "json":
            print("not implemented yet")
        else:
            print ("kind", kind, "not supported")
            return None

        with open(filename, 'w') as fd:
            json.dump(settings, fd, indent=4)


'''            
y2j.py:
import yaml
import json

import sys

yfile = sys.argv[1]
y = open(yfile).read().strip()
d = yaml.load(y)
print json.dumps(d)
'''
