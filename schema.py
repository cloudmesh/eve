#!/usr/bin/env python

import yaml
from cerberus import Validator

schema_text = '''
name:
  type: string
age:
  type: integer
  min: 10
'''
schema = yaml.load(schema_text)
document = {'name': 'Little Joe', 'age': 5}
v = Validator()
print v.validate(document, schema)
print v.errors
