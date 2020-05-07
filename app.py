#!/usr/bin/env python
"""



"""


import falcon

from wsgiref import simple_server

from router import Router 


##------------------------------------------------------------
class InputValidator(object):
    """

    """
    def process_request(self, req, resp):
        #token = req.get_header('Api-Key')
        print("Validating input...")

##------------------------------------------------------------
## Configure WSGI server to load (our WSGI callable) "app.api"
api = application = falcon.API( middleware=[InputValidator()] )

api.req_options.strip_url_path_trailing_slash = True 

api.add_route('/calc', Router()) ## POST

api.add_route('/calc/{symbol}', Router()) ## GET 

##------------------------------------------------------------
## For testing (or run: "gunicorn app.api -b <IP>:<PORT>")
if __name__ == '__main__':
    IP = '0.0.0.0'
    PORT = 8080
    httpd = simple_server.make_server(IP, PORT, api)
    httpd.serve_forever()
