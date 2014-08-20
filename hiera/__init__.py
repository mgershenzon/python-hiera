

import os
import yaml
import hiera.plugins as plugins

#with open('/Users/mrochford/code/python-hiera/test/hiera.yaml', 'r') as f:
#    doc = yaml.load(f)

#print doc


class Hiera():
    def __init__(self, hiera_config_path=None):
        self.hiera_config_path = hiera_config_path
        self.hiera_config = None
        self.facts = {}
        if self.hiera_config_path is None:
            print "missing config"
        else:
            self._read_hiera_config()
            
    def _read_hiera_config(self,):
        with open(self.hiera_config_path, 'r') as f:
            self.hiera_config = yaml.load(f)

    def get_attribute(self, attribute_name) :
        print self.hiera_config[':backends']
        for backend in self.hiera_config[':backends']:
            try:
                return getattr(plugins.json, 'get_attribute')(self.hiera_config, self.facts, attribute_name)
            except AttributeError:
                next
        
        
