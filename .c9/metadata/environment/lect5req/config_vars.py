{"filter":false,"title":"config_vars.py","tooltip":"/lect5req/config_vars.py","undoManager":{"mark":36,"position":36,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":55},"action":"insert","lines":["def hello():","   return \"NUM_POTATOS is: \" + os.getenv(\"NUM_POTATOS\")"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":25},"action":"insert","lines":["import flask, random, os "],"id":3}],[{"start":{"row":0,"column":25},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":4,"column":16},"action":"insert","lines":["app = flask.Flask(__name__)","","@app.route('/') "],"id":5}],[{"start":{"row":6,"column":55},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":7,"column":0},"end":{"row":7,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":[" "],"id":7}],[{"start":{"row":7,"column":2},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":8,"column":2},"end":{"row":11,"column":1},"action":"insert","lines":["app.run(","    port=int(os.getenv('PORT', 8080)),","    host=os.getenv('IP', '0.0.0.0')",")"],"id":9}],[{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"remove","lines":[" "],"id":10},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":25},"action":"remove","lines":["NUM_POTATOS is"],"id":11},{"start":{"row":6,"column":11},"end":{"row":7,"column":0},"action":"insert","lines":["A80WlD_9nZOGpWKBx7ODnFuVK3RjU0W56uEFDvK_TQU6jhHNJKGrKICoet7Gcvj4\"",""]}],[{"start":{"row":6,"column":76},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":6,"column":78},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":7,"column":0},"end":{"row":7,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":["\""],"id":14}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["]"],"id":15}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["]"],"id":16},{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"remove","lines":["    "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":6,"column":75},"end":{"row":6,"column":76},"action":"insert","lines":[" "],"id":17},{"start":{"row":6,"column":76},"end":{"row":6,"column":77},"action":"insert","lines":["i"]},{"start":{"row":6,"column":77},"end":{"row":6,"column":78},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":24},"action":"remove","lines":["NUM_POTATOS"],"id":18},{"start":{"row":7,"column":13},"end":{"row":7,"column":77},"action":"insert","lines":["A80WlD_9nZOGpWKBx7ODnFuVK3RjU0W56uEFDvK_TQU6jhHNJKGrKICoet7Gcvj4"]}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":[" "],"id":19}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":[" "],"id":20}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "],"id":21}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["\""],"id":22}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["\""],"id":23}],[{"start":{"row":6,"column":79},"end":{"row":6,"column":80},"action":"remove","lines":[":"],"id":24}],[{"start":{"row":6,"column":78},"end":{"row":6,"column":79},"action":"insert","lines":[":"],"id":25}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":26}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":[" "],"id":27}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["+"],"id":28}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["+"],"id":29}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":[" "],"id":30}],[{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":[" "],"id":31},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["+"]},{"start":{"row":6,"column":81},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":80},"end":{"row":6,"column":81},"action":"remove","lines":[" "],"id":32}],[{"start":{"row":6,"column":80},"end":{"row":6,"column":81},"action":"insert","lines":["+"],"id":33}],[{"start":{"row":6,"column":81},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":7,"column":0},"end":{"row":7,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":[" "],"id":35},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":6,"column":80},"end":{"row":6,"column":81},"action":"insert","lines":[" "],"id":36}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":[" "],"id":37},{"start":{"row":6,"column":82},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":3},"end":{"row":6,"column":159},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567704952326,"hash":"3609ac3fb64d4156267b3b04372f8a647139a033"}