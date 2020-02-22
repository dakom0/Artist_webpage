# app.py
import flask
import os

app = flask.Flask(__name__)

@app.route('/')  
def index(): 
    x=['/static/ccc4ed75531c7d3ad9085317e9554a3a.300x300x1.jpg',
       '/static/c308ccf4f94eb2b71a2c63a4dfb678ca.300x300x1.png',
       '/static/669e1d96f7b1947e96f19270765a08fb.300x300x1.jpg',
       '/static/600d18d7f6b1ab588669a34411392d6d.300x300x1.jpg',
       '/static/8f0ee7d13b6067c205f6d0ce957d897e.300x300x1.png',
       '/static/aa981739449b02bbdd17cacddf5831be.300x300x1.png',
       '/static/1c96cd9f3ad24ecb1752d09613e78c7c.300x300x1.jpg',
       '/static/f93829ec937b934e29a18d20aa60f3c0.300x300x1.jpg',
       '/static/5881c376782cabdb1de2b38d38415fb8.300x300x1.jpg',
       '/static/fe6e2ae81c03cdac99a611052d5a2d7a.300x300x1.jpg',
        ]
    pic=x[9]
    return flask.render_template("array.html",thumb=pic) # what do I put in here?

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
