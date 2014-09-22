
import hiera

hiera = hiera.Hiera('./test/hiera.yaml')


hiera.facts ={'environments': 'dev'}
print hiera.get_attribute('http_proxy')

#hiera.facts ={'environment': 'prod'}
#print hiera.get_attribute('http_proxy')

#hiera.facts ={'environment': 'qa'}
#print hiera.get_attribute('http_proxy')