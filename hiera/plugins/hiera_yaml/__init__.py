import yaml
import os
import hiera

def _get_datadir(datadir=None):
    found_files = list()
    if isinstance(datadir, str):
        datadir = [datadir]

    for directory in datadir:
        directory = directory.replace("~", os.path.expanduser("~"))
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory, topdown=False):
                for name in files:
                    found_files.append((directory, os.path.join(root, name).replace("{0}/".format(directory),'')))
    return found_files

def _recursive_get_attribute(attribute, hiera_config, facts):
    replace = {}
    while 1:
        try:
            attribute = attribute.format(**replace)
        except KeyError as e:
            key = e.args[0]
            if key == 'datadir':
                replace[key] = hiera_config[':yaml'][':datadir']
            else:
                internal_hiera = hiera.Hiera(hiera_config=hiera_config, facts=facts)
                replace[key] = internal_hiera.get_attribute(key)
        else:
            return attribute

def get_attribute(hiera_config, facts, attribute_name):
    files = _get_datadir(hiera_config[':yaml'][':datadir'])
    for h in hiera_config[':hierarchy']:
        if h != 'common':
            try:
                hiera_file = '{0}.yaml'.format(h).format(**facts)
            except KeyError:
                continue
        else:
            hiera_file = 'common'

        if files:
            if hiera_file in zip(*files)[1]:
                (datadir, hiera_file) = [seq for seq in files if seq[1] == hiera_file][0]
                data = yaml.load(open("{0}/{1}".format(datadir, hiera_file)))

                if data is not None:
                    if attribute_name in data:
                        if isinstance(data[attribute_name], list):
                            for i,attr in enumerate(data[attribute_name]):
                                data[attribute_name][i] =  _recursive_get_attribute(attr, hiera_config, facts)
                            return data[attribute_name]
                        else:
                            return _recursive_get_attribute(data[attribute_name], hiera_config, facts)
                else:
                    continue
        else:
            continue
