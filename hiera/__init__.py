

import os
import yaml
import hiera.plugins as plugins


class Hiera():
    def __init__(self, hiera_config_path=None, hiera_config=None, facts={}):
        self.hiera_config_path = hiera_config_path
        self.hiera_config = hiera_config
        self.facts = facts
        if self.hiera_config_path is not None:
            self._read_hiera_config()

    def _read_hiera_config(self,):
        with open(self.hiera_config_path, 'r') as f:
            self.hiera_config = yaml.load(f)

    def get_attribute(self, attribute_name):
        attribute = None
        for backend in self.hiera_config[':backends']:
            try:
                attribute = getattr(getattr(plugins, 'hiera_{0}'.format(backend)),
                                    'get_attribute')(self.hiera_config,
                                                     self.facts, attribute_name)
            except AttributeError:
                continue
            if attribute is not None:
                return attribute
        return attribute
