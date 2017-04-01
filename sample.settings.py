
profile = {
    'schema': {
        'firstname': {
            'type': 'string'
        },
        'Lastname': {
            'type': 'string'
        },
        'e-mail': {
            'type': 'string'
        },
        'username': {
            'type': 'string'
        }
    }
}

nock = {
    'schema': {
        'profile': {
            'type': 'string'
        }
    }
}

cluster = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'label': {
            'type': 'string'
        },
        'provider': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'endpoint': {
            'type': 'dict',
            'schema': {
                'url': {
                    'type': 'string'
                },
                'passwd': {
                    'type': 'string'
                }
            }
        }
    }
}

computer = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'label': {
            'type': 'string'
        },
        'network': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'ip': {
                        'type': 'string'
                    },
                    'name': {
                        'type': 'string'
                    }
                }
            }
        },
        'memoryGB': {
            'type': 'integer'
        }
    }
}



eve_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_DBNAME': 'testing',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'BANDWIDTH_SAVER': False,
    'DOMAIN': {
        'profile': profile,
        'nock': nock,
        'cluster': cluster,
        'computer': computer,
    },
}
