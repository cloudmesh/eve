
profile = {
    'schema': {
        'username': {
            'type': 'string'
        },
        'context:': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'firstname': {
            'type': 'string'
        },
        'lastname': {
            'type': 'string'
        },
        'email': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        }
    }
}

virtual_machine = {
    'schema': {
        'status': {
            'type': 'string'
        },
        'authorized_keys': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'sshkey',
                    'field': '_id',
                    'embeddable': True
                }
            }
        },
        'name': {
            'type': 'string'
        },
        'nics': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'nic',
                    'field': '_id',
                    'embeddable': True
                }
            }
        },
        'RAM': {
            'type': 'string'
        },
        'ncpu': {
            'type': 'integer'
        },
        'loginuser': {
            'type': 'string'
        },
        'disk': {
            'type': 'string'
        },
        'OS': {
            'type': 'string'
        },
        'metadata': {
            'type': 'dict',
            'schema': {}
        }
    }
}

kubernetes = {
    'schema': {
        'items': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'status': {
                        'type': 'dict',
                        'schema': {
                            'capacity': {
                                'type': 'dict',
                                'schema': {
                                    'cpu': {
                                        'type': 'string'
                                    }
                                }
                            },
                            'addresses': {
                                'type': 'list',
                                'schema': {
                                    'type': 'dict',
                                    'schema': {
                                        'type': {
                                            'type': 'string'
                                        },
                                        'address': {
                                            'type': 'string'
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'kind': {
                        'type': 'string'
                    },
                    'metadata': {
                        'type': 'dict',
                        'schema': {
                            'name': {
                                'type': 'string'
                            }
                        }
                    }
                }
            }
        },
        'kind': {
            'type': 'string'
        },
        'users': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'name': {
                        'type': 'string'
                    },
                    'user': {
                        'type': 'dict',
                        'schema': {
                            'username': {
                                'type': 'string'
                            },
                            'password': {
                                'type': 'string'
                            }
                        }
                    }
                }
            }
        }
    }
}

nic = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'ip': {
            'type': 'string'
        },
        'mask': {
            'type': 'string'
        },
        'bandwidth': {
            'type': 'string'
        },
        'mtu': {
            'type': 'integer'
        },
        'broadcast': {
            'type': 'string'
        },
        'mac': {
            'type': 'string'
        },
        'type': {
            'type': 'string'
        },
        'gateway': {
            'type': 'string'
        }
    }
}

virtual_compute_node = {
    'schema': {
        'status': {
            'type': 'string'
        },
        'endpoint': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'ip': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'image': {
            'type': 'string'
        },
        'flavor': {
            'type': 'string'
        },
        'metadata': {
            'type': 'dict',
            'schema': {
                'experiment': {
                    'type': 'string'
                }
            }
        }
    }
}

openstack_flavor = {
    'schema': {
        'os_flv_disabled': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        },
        'os_flv_ext_data': {
            'type': 'string'
        },
        'ram': {
            'type': 'string'
        },
        'os_flavor_acces': {
            'type': 'string'
        },
        'vcpus': {
            'type': 'string'
        },
        'swap': {
            'type': 'string'
        },
        'rxtx_factor': {
            'type': 'string'
        },
        'disk': {
            'type': 'string'
        }
    }
}

azure_vm = {
    'schema': {
        'username': {
            'type': 'string'
        },
        'status': {
            'type': 'string'
        },
        'deployment_slot': {
            'type': 'string'
        },
        'group': {
            'type': 'string'
        },
        'private_ips': {
            'type': 'string'
        },
        'cloud_service': {
            'type': 'string'
        },
        'dns_name': {
            'type': 'string'
        },
        'image': {
            'type': 'string'
        },
        'floating_ip': {
            'type': 'string'
        },
        'image_name': {
            'type': 'string'
        },
        'instance_name': {
            'type': 'string'
        },
        'public_ips': {
            'type': 'string'
        },
        'media_link': {
            'type': 'string'
        },
        'key': {
            'type': 'string'
        },
        'flavor': {
            'type': 'string'
        },
        'resource_location': {
            'type': 'string'
        },
        'instance_size': {
            'type': 'string'
        },
        'disk_name': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        }
    }
}

azure_size = {
    'schema': {
        'ram': {
            'type': 'integer'
        },
        'name': {
            'type': 'string'
        },
        'extra': {
            'type': 'dict',
            'schema': {
                'cores': {
                    'type': 'integer'
                },
                'max_data_disks': {
                    'type': 'integer'
                }
            }
        },
        'price': {
            'type': 'float'
        },
        '_uuid': {
            'type': 'string'
        },
        'driver': {
            'type': 'string'
        },
        'bandwidth': {
            'type': 'string'
        },
        'disk': {
            'type': 'integer'
        },
        'id': {
            'type': 'string'
        }
    }
}

openstack_vm = {
    'schema': {
        'vm_state': {
            'type': 'string'
        },
        'availability_zone': {
            'type': 'string'
        },
        'terminated_at': {
            'type': 'string'
        },
        'image': {
            'type': 'string'
        },
        'diskConfig': {
            'type': 'string'
        },
        'flavor': {
            'type': 'string'
        },
        'security_groups': {
            'type': 'string'
        },
        'volumes_attached': {
            'type': 'string'
        },
        'user_id': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        },
        'accessIPv4': {
            'type': 'string'
        },
        'accessIPv6': {
            'type': 'string'
        },
        'power_state': {
            'type': 'string'
        },
        'progress': {
            'type': 'string'
        },
        'image__id': {
            'type': 'string'
        },
        'launched_at': {
            'type': 'string'
        },
        'config_drive': {
            'type': 'string'
        },
        'username': {
            'type': 'string'
        },
        'updated': {
            'type': 'string'
        },
        'hostId': {
            'type': 'string'
        },
        'floating_ip': {
            'type': 'string'
        },
        'static_ip': {
            'type': 'string'
        },
        'key': {
            'type': 'string'
        },
        'flavor__id': {
            'type': 'string'
        },
        'group': {
            'type': 'string'
        },
        'task_state': {
            'type': 'string'
        },
        'created': {
            'type': 'string'
        },
        'tenant_id': {
            'type': 'string'
        },
        'status': {
            'type': 'string'
        }
    }
}

cluster = {
    'schema': {
        'provider': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'endpoint': {
            'type': 'dict',
            'schema': {
                'passwd': {
                    'type': 'string'
                },
                'url': {
                    'type': 'string'
                }
            }
        },
        'name': {
            'type': 'string'
        },
        'label': {
            'type': 'string'
        }
    }
}

computer = {
    'schema': {
        'ip': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'memoryGB': {
            'type': 'integer'
        },
        'label': {
            'type': 'string'
        }
    }
}

libcloud_image = {
    'schema': {
        'username': {
            'type': 'string'
        },
        'status': {
            'type': 'string'
        },
        'updated': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'owner_alias': {
            'type': 'string'
        },
        'kernel_id': {
            'type': 'string'
        },
        'hypervisor': {
            'type': 'string'
        },
        'ramdisk_id': {
            'type': 'string'
        },
        'state': {
            'type': 'string'
        },
        'created': {
            'type': 'string'
        },
        'image_id': {
            'type': 'string'
        },
        'image_location': {
            'type': 'string'
        },
        'platform': {
            'type': 'string'
        },
        'image_type': {
            'type': 'string'
        },
        'is_public': {
            'type': 'string'
        },
        'owner_id': {
            'type': 'string'
        },
        'architecture': {
            'type': 'string'
        },
        'virtualization_type': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        }
    }
}

user = {
    'schema': {
        'username': {
            'type': 'string'
        },
        'context:': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        },
        'firstname': {
            'type': 'string'
        },
        'lastname': {
            'type': 'string'
        },
        'roles': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'email': {
            'type': 'string'
        }
    }
}

file = {
    'schema': {
        'endpoint': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'created': {
            'type': 'string'
        },
        'checksum': {
            'type': 'dict',
            'schema': {
                'md5': {
                    'type': 'string'
                }
            }
        },
        'modified': {
            'type': 'string'
        },
        'accessed': {
            'type': 'string'
        },
        'size': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        }
    }
}

deployment = {
    'schema': {
        'cluster': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'id': {
                        'type': 'string'
                    }
                }
            }
        },
        'stack': {
            'type': 'dict',
            'schema': {
                'layers': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                },
                'parameters': {
                    'type': 'dict',
                    'schema': {
                        'hadoop': {
                            'type': 'dict',
                            'schema': {
                                'zookeeper.quorum': {
                                    'type': 'list',
                                    'schema': {
                                        'type': 'string'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

mapreduce = {
    'schema': {
        'layers': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'hdfs_datanode': {
            'type': 'string'
        },
        'java': {
            'type': 'dict',
            'schema': {
                'platform': {
                    'type': 'string'
                },
                'version': {
                    'type': 'string'
                }
            }
        },
        'supervisord': {
            'type': 'string'
        },
        'yarn_historyserver': {
            'type': 'string'
        },
        'zookeeper': {
            'type': 'string'
        },
        'hdfs_namenode': {
            'type': 'string'
        },
        'hdfs_journalnode': {
            'type': 'string'
        },
        'yarn_resourcemanager': {
            'type': 'string'
        }
    }
}

group = {
    'schema': {
        'users': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'user',
                    'field': '_id',
                    'embeddable': True
                }
            }
        },
        'name': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        }
    }
}

role = {
    'schema': {
        'users': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'user',
                    'field': '_id',
                    'embeddable': True
                }
            }
        },
        'name': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        }
    }
}

virtual_directory = {
    'schema': {
        'endpoint': {
            'type': 'string'
        },
        'protocol': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'collection': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        }
    }
}

file_alias = {
    'schema': {
        'alias': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        }
    }
}

virtual_cluster = {
    'schema': {
        'nodes': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'virtual_machine',
                    'field': '_id',
                    'embeddable': True
                }
            }
        },
        'frontend': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'virtual_machine',
                'field': '_id',
                'embeddable': True
            }
        },
        'name': {
            'type': 'string'
        }
    }
}

libcloud_flavor = {
    'schema': {
        'uuid': {
            'type': 'string'
        },
        'price': {
            'type': 'string'
        },
        'ram': {
            'type': 'string'
        },
        'bandwidth': {
            'type': 'string'
        },
        'flavor_id': {
            'type': 'string'
        },
        'disk': {
            'type': 'string'
        },
        'cpu': {
            'type': 'string'
        }
    }
}

batchjob = {
    'schema': {
        'output_file': {
            'type': 'string'
        },
        'group': {
            'type': 'string'
        },
        'job_id': {
            'type': 'string'
        },
        'script': {
            'type': 'string'
        },
        'cmd': {
            'type': 'string'
        },
        'queue': {
            'type': 'string'
        },
        'cluster': {
            'type': 'string'
        },
        'time': {
            'type': 'string'
        },
        'path': {
            'type': 'string'
        },
        'nodes': {
            'type': 'string'
        },
        'dir': {
            'type': 'string'
        }
    }
}

organization = {
    'schema': {
        'users': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'user',
                    'field': '_id',
                    'embeddable': True
                }
            }
        }
    }
}

container = {
    'schema': {
        'ip': {
            'type': 'string'
        },
        'endpoint': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'memoryGB': {
            'type': 'integer'
        },
        'label': {
            'type': 'string'
        }
    }
}

sshkey = {
    'schema': {
        'comment': {
            'type': 'string'
        },
        'source': {
            'type': 'string'
        },
        'uri': {
            'type': 'string'
        },
        'value': {
            'type': 'string'
        },
        'fingerprint': {
            'type': 'string'
        }
    }
}

stream = {
    'schema': {
        'attributes': {
            'type': 'dict',
            'schema': {
                'rate': {
                    'type': 'integer'
                },
                'limit': {
                    'type': 'integer'
                }
            }
        },
        'name': {
            'type': 'string'
        },
        'format': {
            'type': 'string'
        }
    }
}

database = {
    'schema': {
        'endpoint': {
            'type': 'string'
        },
        'protocol': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        }
    }
}

default = {
    'schema': {
        'context': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'value': {
            'type': 'string'
        }
    }
}

openstack_image = {
    'schema': {
        'status': {
            'type': 'string'
        },
        'username': {
            'type': 'string'
        },
        'updated': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        },
        'created': {
            'type': 'string'
        },
        'minDisk': {
            'type': 'string'
        },
        'progress': {
            'type': 'string'
        },
        'minRam': {
            'type': 'string'
        },
        'os_image_size': {
            'type': 'string'
        },
        'metadata': {
            'type': 'dict',
            'schema': {
                'instance_uuid': {
                    'type': 'string'
                },
                'image_location': {
                    'type': 'string'
                },
                'image_state': {
                    'type': 'string'
                },
                'instance_type_memory_mb': {
                    'type': 'string'
                },
                'user_id': {
                    'type': 'string'
                },
                'description': {
                    'type': 'string'
                },
                'kernel_id': {
                    'type': 'string'
                },
                'instance_type_name': {
                    'type': 'string'
                },
                'ramdisk_id': {
                    'type': 'string'
                },
                'instance_type_id': {
                    'type': 'string'
                },
                'instance_type_ephemeral_gb': {
                    'type': 'string'
                },
                'instance_type_rxtx_factor': {
                    'type': 'string'
                },
                'image_type': {
                    'type': 'string'
                },
                'network_allocated': {
                    'type': 'string'
                },
                'instance_type_flavorid': {
                    'type': 'string'
                },
                'instance_type_vcpus': {
                    'type': 'string'
                },
                'instance_type_root_gb': {
                    'type': 'string'
                },
                'base_image_ref': {
                    'type': 'string'
                },
                'instance_type_swap': {
                    'type': 'string'
                },
                'owner_id': {
                    'type': 'string'
                }
            }
        }
    }
}

azure_image = {
    'schema': {
        '_uuid': {
            'type': 'string'
        },
        'driver': {
            'type': 'string'
        },
        'id': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'extra': {
            'type': 'dict',
            'schema': {
                'category': {
                    'type': 'string'
                },
                'description': {
                    'type': 'string'
                },
                'vm_image': {
                    'type': 'string'
                },
                'location': {
                    'type': 'string'
                },
                'affinity_group': {
                    'type': 'string'
                },
                'os': {
                    'type': 'string'
                },
                'media_link': {
                    'type': 'string'
                }
            }
        }
    }
}

hadoop = {
    'schema': {
        'deployers': {
            'type': 'dict',
            'schema': {
                'ansible': {
                    'type': 'string'
                }
            }
        },
        'requires': {
            'type': 'dict',
            'schema': {
                'java': {
                    'type': 'dict',
                    'schema': {
                        'implementation': {
                            'type': 'string'
                        },
                        'version': {
                            'type': 'string'
                        },
                        'zookeeper': {
                            'type': 'string'
                        },
                        'supervisord': {
                            'type': 'string'
                        }
                    }
                }
            }
        },
        'parameters': {
            'type': 'dict',
            'schema': {
                'num_resourcemanagers': {
                    'type': 'integer'
                },
                'num_namenodes': {
                    'type': 'integer'
                },
                'use_yarn': {
                    'type': 'boolean'
                },
                'num_datanodes': {
                    'type': 'integer'
                },
                'use_hdfs': {
                    'type': 'boolean'
                },
                'num_historyservers': {
                    'type': 'integer'
                },
                'num_journalnodes': {
                    'type': 'integer'
                }
            }
        }
    }
}

compute_resource = {
    'schema': {
        'kind': {
            'type': 'string'
        },
        'endpoint': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        }
    }
}

node_new = {
    'schema': {
        'authorized_keys': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'name': {
            'type': 'string'
        },
        'external_ip': {
            'type': 'string'
        },
        'memory': {
            'type': 'integer'
        },
        'create_external_ip': {
            'type': 'boolean'
        },
        'internal_ip': {
            'type': 'string'
        },
        'loginuser': {
            'type': 'string'
        },
        'owner': {
            'type': 'string'
        },
        'cores': {
            'type': 'integer'
        },
        'disk': {
            'type': 'integer'
        },
        'ssh_keys': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'from': {
                        'type': 'string'
                    },
                    'decrypt': {
                        'type': 'string'
                    },
                    'ssh_keygen': {
                        'type': 'boolean'
                    },
                    'to': {
                        'type': 'string'
                    }
                }
            }
        },
        'security_groups': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'ingress': {
                        'type': 'string'
                    },
                    'egress': {
                        'type': 'string'
                    },
                    'ports': {
                        'type': 'list',
                        'schema': {
                            'type': 'integer'
                        }
                    },
                    'protocols': {
                        'type': 'list',
                        'schema': {
                            'type': 'string'
                        }
                    }
                }
            }
        },
        'users': {
            'type': 'dict',
            'schema': {
                'name': {
                    'type': 'string'
                },
                'groups': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                }
            }
        }
    }
}

filter = {
    'schema': {
        'function': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        }
    }
}

reservation = {
    'schema': {
        'start_time': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'hosts': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'end_time': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        }
    }
}

replica = {
    'schema': {
        'endpoint': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'checksum': {
            'type': 'dict',
            'schema': {
                'md5': {
                    'type': 'string'
                }
            }
        },
        'replica': {
            'type': 'string'
        },
        'accessed': {
            'type': 'string'
        },
        'size': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        }
    }
}

microservice = {
    'schema': {
        'function': {
            'type': 'string'
        },
        'endpoint': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        }
    }
}

var = {
    'schema': {
        'type': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'value': {
            'type': 'string'
        }
    }
}

mesos_docker = {
    'schema': {
        'container': {
            'type': 'dict',
            'schema': {
                'docker': {
                    'type': 'dict',
                    'schema': {
                        'credential': {
                            'type': 'dict',
                            'schema': {
                                'secret': {
                                    'type': 'string'
                                },
                                'principal': {
                                    'type': 'string'
                                }
                            }
                        },
                        'image': {
                            'type': 'string'
                        }
                    }
                },
                'type': {
                    'type': 'string'
                }
            }
        },
        'mem': {
            'type': 'float'
        },
        'args': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'cpus': {
            'type': 'float'
        },
        'instances': {
            'type': 'integer'
        },
        'id': {
            'type': 'string'
        }
    }
}

libcloud_vm = {
    'schema': {
        'username': {
            'type': 'string'
        },
        'status': {
            'type': 'string'
        },
        'root_device_type': {
            'type': 'string'
        },
        'private_ips': {
            'type': 'string'
        },
        'instance_type': {
            'type': 'string'
        },
        'image': {
            'type': 'string'
        },
        'private_dns': {
            'type': 'string'
        },
        'image_name': {
            'type': 'string'
        },
        'instance_id': {
            'type': 'string'
        },
        'image_id': {
            'type': 'string'
        },
        'public_ips': {
            'type': 'string'
        },
        'state': {
            'type': 'string'
        },
        'root_device_name': {
            'type': 'string'
        },
        'key': {
            'type': 'string'
        },
        'group': {
            'type': 'string'
        },
        'flavor': {
            'type': 'string'
        },
        'availability': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
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
        'virtual_machine': virtual_machine,
        'kubernetes': kubernetes,
        'nic': nic,
        'virtual_compute_node': virtual_compute_node,
        'openstack_flavor': openstack_flavor,
        'azure-vm': azure_vm,
        'azure-size': azure_size,
        'openstack_vm': openstack_vm,
        'cluster': cluster,
        'computer': computer,
        'libcloud_image': libcloud_image,
        'user': user,
        'file': file,
        'deployment': deployment,
        'mapreduce': mapreduce,
        'group': group,
        'role': role,
        'virtual_directory': virtual_directory,
        'file_alias': file_alias,
        'virtual_cluster': virtual_cluster,
        'libcloud_flavor': libcloud_flavor,
        'batchjob': batchjob,
        'organization': organization,
        'container': container,
        'sshkey': sshkey,
        'stream': stream,
        'database': database,
        'default': default,
        'openstack_image': openstack_image,
        'azure_image': azure_image,
        'hadoop': hadoop,
        'compute_resource': compute_resource,
        'node_new': node_new,
        'filter': filter,
        'reservation': reservation,
        'replica': replica,
        'microservice': microservice,
        'var': var,
        'mesos-docker': mesos_docker,
        'libcloud_vm': libcloud_vm,
    },
}
