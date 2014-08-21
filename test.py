
import hiera

hiera = hiera.Hiera('./test/hiera.yaml')
hiera.facts ={'environment': 'dev'}
print hiera.get_attribute('http_proxy')