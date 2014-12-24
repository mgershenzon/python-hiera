
import hiera

hiera = hiera.Hiera('/Users/mrochford/personal/python-hiera/test/hiera.yaml')

print "Dev"
print "-" * 80
hiera.facts ={'environment': 'dev'}
print hiera.get_attribute('http_proxy')
print hiera.get_attribute('smtp_server')
print

print "Prod"
print "-" * 80
hiera.facts ={'environment': 'prod'}
print hiera.get_attribute('http_proxy')
print 

print "QA"
print "-" * 80
hiera.facts ={'environment': 'qa'}
print hiera.get_attribute('http_proxy')
print
