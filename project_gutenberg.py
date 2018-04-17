import urllib2
response = urllib2.urlopen('http://gutenberg.org/')
html = response.read ()

print (html)
# Have to install pip , I guess or something of the sort 
