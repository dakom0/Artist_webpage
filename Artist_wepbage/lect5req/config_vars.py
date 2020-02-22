import flask, random, os 

app = flask.Flask(__name__)

@app.route('/') 
def hello():
   return "A80WlD_9nZOGpWKBx7ODnFuVK3RjU0W56uEFDvK_TQU6jhHNJKGrKICoet7Gcvj4 is:" +os.getenv("A80WlD_9nZOGpWKBx7ODnFuVK3RjU0W56uEFDvK_TQU6jhHNJKGrKICoet7Gcvj4")
  
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)