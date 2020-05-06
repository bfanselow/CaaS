import falcon

from calculator import SimpleMath 

api = application = falcon.API()

simple = SimpleMath()

api.add_route('/simple', simple)
