
import hiera

hiera = hiera.Hiera('./test/hiera.yaml')


print
print "dev"
print "-" * 80
hiera.facts ={'environment': 'dev'}
print hiera.get_attribute('http_proxy')
print
print "prod"
print "-" * 80
hiera.facts ={'environment': 'prod'}
print hiera.get_attribute('http_proxy')
print
print "qa"
print "-" * 80
hiera.facts ={'environment': 'qa'}
print hiera.get_attribute('http_proxy')
