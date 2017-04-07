class YmlToSpec(object):
    def __init__(self, infile, outfile=None):
        self.execute(infile, outfile)

    def execute(self, infile, outfile):
        pass


'''
#########################


yfile = sys.argv[1]
base, _ = splitext(yfile)
texfile = base + '.tex'

if exists(texfile):
    mkdesc = ['pandoc', '--to', 'rst', '--wrap', 'none', texfile]
    description = check_output(mkdesc).strip()
else:
    description = 'FIXME'


example = yaml.load(open(yfile))

################################################################ typeify

assert len(example) == 1, example


def typeit(value):
    if isinstance(value, str) or isinstance(value, unicode):
        return 'string'

    elif isinstance(value, int):
        return 'int'

    elif isinstance(value, float):
        return 'float'

    elif isinstance(value, bool):
        return 'bool'

    elif isinstance(value, list):
        assert len(value) > 0
        subtype = typeit(value[0])
        return 'list of %s' % subtype

    elif isinstance(value, dict):
        return 'dict'

    else:
        raise NotImplementedError(type(value), value)


name = example.keys()[0]
definition = dict()
definition[name] = dict()
for attr, value in example[name].iteritems():
    definition[name][attr] = {'type': typeit(value)}

definition[name]['__description'] = description
definition[name]['__example'] = example[name]

print yaml.dump(definition, default_flow_style=False)
'''
