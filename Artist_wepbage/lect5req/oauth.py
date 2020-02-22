# oauth_test.py
import requests_oauthlib, requests
import json


url = "https://api.twitter.com/1.1/search/tweets.json?q=chongy"

oauth = requests_oauthlib.OAuth1(
    "GlWPdDE6Ok0peQFSzjOjFCElf", 
    "Pm4UYOJC0eUfSd8HiUkDA9UPzZbXfneKfYlDBufDFPCRQJmUJi",
    "1167271344913952768-H0wcA9DtIZsLflMzIfjHzPmKn24RgZ",
    "WFZQukyQssHgqHrtghTSNVu9NWK7HfMIOamV90JFLCAId"
)

response = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=chongy", auth=oauth)
json_body= response.json()
#print(json.dumps(json_body,indent=2))
#print(json_body["statuses"][0]["text"])

print('-'+json_body["statuses"][0]["user"]["screen_name"])
