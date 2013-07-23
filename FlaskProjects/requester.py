import urllib2
import urllib
import json
pack = {'sdf':234, 'ads':'asdf'}

data = urllib2.urlopen("http://127.0.0.1:5000/gptest", json.dumps(pack)).read()
print data

#data = urllib2.urlopen('http://127.0.0.1:5000/gptest').read()
#print data
