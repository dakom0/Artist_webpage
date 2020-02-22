import requests
import json

my_headers={"Authorization": "Bearer A80WlD_9nZOGpWKBx7ODnFuVK3RjU0W56uEFDvK_TQU6jhHNJKGrKICoet7Gcvj4"
    
}

response1= requests.get("https://api.genius.com/search?q=Coldplay",headers=
my_headers)

json_body= response1.json()
#print(json.dumps(json_body,indent=2))
print(json_body["response"]["hits"][0]["result"]["song_art_image_url"])
print(json_body["response"]["hits"][0]["result"]["title"])
