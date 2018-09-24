# Parsing json with Python example #2
# import json​
# data = '''{​
#   "name" : "Chuck",​
#   "phone" : {​
#     "type" : "intl",​
#     "number" : "+1 734 303 4456"​
#    },​
#    "email" : {​
#      "hide" : "yes"​
#    }​
# }'''​
# ​info = json.loads(data)​
# print('Name:',info["name"])​
# print('Hide:',info["email"]["hide"])​


# Parsing json with Python example #2
# import json
# input = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Chuck"
#   } 
# ]'''
# info = json.loads(input)
# print('User count:', len(info))
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])


# Self made program to parse json
# import json
# input = '''
# {
#     "Account": "021465731353",
#     "UserId": "AIDAJHN2N2SQQBSTSULYI",
#     "Arn": "arn:aws:iam::021465731353:user/zora-trainer"
# }'''
# info = json.loads(input)
# print('Length',len(info))
# y = info['Arn']
# z = y.split('/')
# print('Name =', z[1])

# Service Oriented Approach​
# Most non-trivial web applications use services​
# They use services from other applications​
# -  Credit Card Charge​
# -  Hotel Reservation systems​
# Services publish the “rules” applications must follow to make use of the service (API)​
# YouTube Video - http://www.youtube.com/watch?v=mj-kCFzF0ME

# Application Programming Interface
# The API itself is largely abstract in that it specifies an interface and controls the behavior of the objects specified in that interface. The software that provides the functionality described by an API is said to be an “implementation” of the API.  An API is typically defined in terms of the programming language used to build an application. ​- http://en.wikipedia.org/wiki/API

# Type this URL in the google to get the json output:
# http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI%E2%80%8B

# Geocoding using Python - geojson.py 
# import urllib
# import json

# # serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# serviceurl = 'http://python-data.dr-chuck.net/geojson?'

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1 : break

#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print('Retrieving', url)
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print('Retrieved',len(data),'characters')

#     try: js = json.loads(str(data))
#     except: js = None
#     if 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue

#     print(json.dumps(js, indent=4))

#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('lat',lat,'lng',lng)
#     location = js['results'][0]['formatted_address']
#     print(location)


# Working with Twitter API
# import urllib
# import twurl
# import json

# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# while True:
#     print('')
#     acct = raw_input('Enter Twitter Account:')
#     if ( len(acct) < 1 ) : break
#     url = twurl.augment(TWITTER_URL,
#         {'screen_name': acct, 'count': '5'} )
#     print('Retrieving', url)
#     connection = urllib.urlopen(url)
#     data = connection.read()
#     headers = connection.info().dict
#     print('Remaining', headers['x-rate-limit-remaining'])
#     js = json.loads(data)
#     print(json.dumps(js, indent=4))

#     for u in js['users'] :
#         print(u['screen_name'])
#         s = u['status']['text']
#         print('  ',s[:50])

# Hidden.py
# Keep this file separate
# https://apps.twitter.com/

# def oauth() :
#     return { "consumer_key" : "h7Lu...Ng",
#         "consumer_secret" : "dNKenAC3New...mmn7Q",
#         "token_key" : "10185562-eibxCp9n2...P4GEQQOSGI",
#         "token_secret" : "H0ycCFemmC4wyf1...qoIpBo" }
