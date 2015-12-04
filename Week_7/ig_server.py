import requests
from random import randint
import json

from flask import Flask # here we import the Flask class
app = Flask(__name__) # we create an instance of the Flask class -> '__name__'

from flask import request # lets us extract parameters from the query url

@app.route("/") # we use whats called a 'decorator' to tell Flask what URL should trigger our function
def hello():
    return "Hello World!" 


@app.route('/igtag/<tag>')
def igtag(tag):
    
    # we can call a function that has all the logic (hint: #hedgehog is an awesome IG tag!)
    return get_ig_media(tag)
    
@app.route('/igtagviz/<tag>')
def igtagviz(tag):
    
    url = get_ig_media(tag)
    
    # instead of returning the link, let's return html back
    return '<img src="%s"/>' % url
    
def get_ig_media(tag):
    
    client_id = '0db0c30814c14ac48a58c8e27a7b4a5a'
    client_secret = '8681192578424d78aea183f1bf05f465'

    from instagram.client import InstagramAPI

    api = InstagramAPI(client_id=client_id, client_secret=client_secret)
    
    media, _next = api.tag_recent_media(33, 0, tag)
    
    # let's make it a bit more interesting
    choice = randint(0,33)
    return media[choice].get_standard_resolution_url()
    


@app.route('/ig',methods=["GET"])
def ig_slack_command():
    webhook_url = "https://hooks.slack.com/services/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"

    tag = request.args.get('text',None)
    print tag
    
    if not tag:
        payload = {"text":'send me a tag!!', "username":'ig-bot'}
        r = requests.post(webhook_url, data={"payload":json.dumps(payload)})
    else:
        cur_url = get_ig_media(tag)
        payload = {"text":cur_url, "username":'ig-bot'}
        r = requests.post(webhook_url, data={"payload":json.dumps(payload)})
    
    return ''
    

# only runs if the script is executed directly from the Python interpreter (and not used as an imported module)
if __name__ == "__main__":  

    app.debug = True # we want to get error messages
    app.run(host='0.0.0.0', port=8886, threaded=True) # make your endpoint publicly available 

