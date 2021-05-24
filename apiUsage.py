import urllib.request, urllib.parse, urllib.error 
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


serviceURL = "http://py4e-data.dr-chuck.net/json?"
param = dict()
address = input("Enter your address")
api_key = 42
param["address"] = address
param["key"] = api_key

url = serviceURL + urllib.parse.urlencode(param)
data = urllib.request.urlopen(url, context=ctx).read().decode()
print("Retrieving", len(data), "characters")
data = json.loads(data)
# print(json.dumps(data, indent=4))
print("Place_id is", data["results"][0]["place_id"])