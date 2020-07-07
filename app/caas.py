#!/usr/bin/env python
"""

 Script: caas.py
 Description: Create the "api" WSGI object to be served by simple_server, or gunicorn

 For testing:
  $ python app/caas.py
   OR
  $ gunicorn caas:api -b <IP>:<PORT>

"""

import falcon
from wsgiref import simple_server
from router import Router 

##------------------------------------------------------------
class InputValidator(object):
    """Perform input validation before passing to router.
     TODO: make this actually do something    
    """
    def process_request(self, req, resp):
        #token = req.get_header('Api-Key')
        print("Validating input...")

##------------------------------------------------------------
## Configure WSGI server to load (our WSGI callable) "app.api"
api = application = falcon.API( middleware=[InputValidator()] )

api.req_options.strip_url_path_trailing_slash = True 

## POST
api.add_route('/calc', Router()) 

## GET 
api.add_route('/calc/{symbol}', Router()) 

##------------------------------------------------------------
if __name__ == '__main__':
    IP = '0.0.0.0'
    PORT = 8080
    httpd = simple_server.make_server(IP, PORT, api)
    httpd.serve_forever()
