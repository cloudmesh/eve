import yaml
import json
import os.path
import glob


for jpath in glob.glob('resources/samples/*.json'):
    base, ext = os.path.splitext(jpath)
    ypath = base + '.yml'

    with open(jpath) as fd:
        d = json.load(fd)

    with open(ypath, 'w') as fd:
        print ypath
        yaml.safe_dump(d, fd, default_flow_style=False)
