import requests
import json

my_headers={"Authorization": "Bearer A80WlD_9nZOGpWKBx7ODnFuVK3RjU0W56uEFDvK_TQU6jhHNJKGrKICoet7Gcvj4"
    
}

response1= requests.get("https://api.genius.com/search?q=Coldplay",headers=
my_headers)

json_body1= response1.json()
print(json.dumps(json_body1,indent=2))
print(json_body1["response"]["hits"][0]["result"]["song_art_image_url"])
print(json_body1["response"]["hits"][1]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][2]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][3]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][4]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][5]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][6]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][7]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][8]["result"]["song_art_image_thumbnail_url"])
print(json_body1["response"]["hits"][9]["result"]["song_art_image_thumbnail_url"])
#print(json_body1["response"]["hits"][9]["result"]["title"])
