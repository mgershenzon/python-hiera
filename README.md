# python-hiera #

## Synopsis ##
python-hiera is a key/value look up tool for configuration data. It is based of
the puppet version of heira. This module is written in pure python and does not
use subprocess to execute hiera.

### Data Sources available ###
 - YAML
 - JSON

## Example ##
This module contains a example that only has one key/value pair stored in the data
store. The key is 'http_proxy' and doesn't live completely in a single data source. 