import urllib2, base64
data = '{}'
url = 'http://172.26.182.70:30100/api/v2/risks/vulnerabilities/csv'
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
base64string = base64.b64encode('%s:%s' % ('api', 'apiuser123'))
req.add_header("Authorization", "Basic %s" % base64string)
f = urllib2.urlopen(req)
for x in f:
    print(x)
f.close()

