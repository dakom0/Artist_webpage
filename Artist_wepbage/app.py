import flask, random, os 
import requests_oauthlib, requests
import json


app = flask.Flask(__name__)

@app.route('/')  
def index(): 
    r= random.randint(0,9)
    rand= random.randint(0,13)

    return flask.render_template(
        "index.html",
        quote=(json_body["statuses"][rand]["text"]),
        title=(json_body1["response"]["hits"][r]["result"]["title"]),
        thumb=(json_body1["response"]["hits"][r]["result"]["song_art_image_thumbnail_url"])
        )
        
my_headers={"Authorization": "Bearer A80WlD_9nZOGpWKBx7ODnFuVK3RjU0W56uEFDvK_TQU6jhHNJKGrKICoet7Gcvj4"
    }
response1= requests.get("https://api.genius.com/search?q=Coldplay",headers=
  my_headers)
json_body1= response1.json()

url = "https://api.twitter.com/1.1/search/tweets.json?q=Mourinho"

oauth = requests_oauthlib.OAuth1(
    "GlWPdDE6Ok0peQFSzjOjFCElf", 
    "Pm4UYOJC0eUfSd8HiUkDA9UPzZbXfneKfYlDBufDFPCRQJmUJi",
    "1167271344913952768-H0wcA9DtIZsLflMzIfjHzPmKn24RgZ",
    "WFZQukyQssHgqHrtghTSNVu9NWK7HfMIOamV90JFLCAId"
    )
response = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=coldplay",
auth=oauth)
json_body= response.json()

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
