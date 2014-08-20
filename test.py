
import hiera

hiera = hiera.Hiera('/Users/mrochford/code/python-hiera/test/hiera.yaml')
hiera.facts ={'environment': 'dev'}
print hiera.get_attribute('http_proxy')