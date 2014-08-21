
import json
import os


def _get_datadir(data_directory=None):
    found_files = list()
    for root, dirs, files in os.walk(data_directory, topdown=False):
        for name in files:
            found_files.append(os.path.join(root, name).replace("%s/" % data_directory,''))
    return found_files


def get_attribute(hiera_config, facts, attribute_name):
    
    files = _get_datadir(hiera_config[':json'][':datadir'])
    print files
    for h in hiera_config[':hierarchy']:
        if h != 'common':
            try:
                hiera_file = '%s.json' % h % facts
            except KeyError:
                continue
        else:
            hiera_file = 'common'
        
        if hiera_file in files:
            data = json.load(open("%s/%s" % (hiera_config[':json'][':datadir'], hiera_file)))
            if attribute_name in data:
                return data[attribute_name]
                
    return False