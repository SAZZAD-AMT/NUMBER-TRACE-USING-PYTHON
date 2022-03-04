import requests

## single ip request
# response = requests.get("http://ip-api.com/json/24.48.0.1").json()
#
# print(response['lat'])
# print(response['lon'])

# batch ip request

response = requests.post("http://ip-api.com/batch", json=[
  {"query": "103.120.203.180"},
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")
