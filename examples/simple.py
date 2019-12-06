"""A sample file that will print the API response code and your IP"""
import json
from reqrest import REST

# Set REST URL
RESTAPI = REST('api.ipify.org')

# Create the querystring so we get json data back
QUERYSTRING = {}
QUERYSTRING['format'] = "json"

# Do the API call
RESPONSE = RESTAPI.get("/", QUERYSTRING)

# Get the response body and convert it to a dict
IP = json.loads(RESPONSE.text)

# Print what we got
print("HTTP status code: %i" % RESPONSE.status_code)
print("IP Address: %s " % IP['ip'])
