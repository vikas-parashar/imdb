import urllib
import json
import re
import urllib

def imdb():
  t = raw_input("Enter movie: ")
  url = 'http://deanclatworthy.com/imdb/?'
  return url+urllib.urlencode({"q":t})
fetch = urllib.urlopen(imdb())
data = json.load(fetch)
print data["rating"]
#it's just a comment...
