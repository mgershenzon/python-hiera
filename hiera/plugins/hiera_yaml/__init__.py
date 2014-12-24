import yaml
import os


def _get_datadir(data_directory=None):
    found_files = list()
    for root, dirs, files in os.walk(data_directory, topdown=False):
        for name in files:
            found_files.append(os.path.join(root, name).replace("%s/" % data_directory,''))
    return found_files


def get_attribute(hiera_config, facts, attribute_name):
    files = _get_datadir(hiera_config[':yaml'][':datadir'])
    for h in hiera_config[':hierarchy']:
        if h != 'common':
            try:
                hiera_file = '%s.yaml' % h % facts
            except KeyError:
                continue
        else:
            hiera_file = 'common'
        
        if hiera_file in files:
            data = yaml.load(open("%s/%s" % (hiera_config[':yaml'][':datadir'], hiera_file)))
            
            if data is not None:
                if attribute_name in data:
                    return data[attribute_name]
            else:
                continue