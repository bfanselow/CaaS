
"""

  File: router.py
  Class: Router()
  Description:
   Handle GET and POST requests for the "/calc" resource
    * GET request example:    /cac/{symbol} where "symbol" is one of the supported mathematical constants
    * POST request example:  -H "Content-Type: application/json" -d '{"problem": "(2/3)-(1/3)"}'

"""

import json
import falcon
from calculator import Calculator, constants 

##----------------------------------------------------------------------------
class InvalidRequestFormat(Exception):
  pass

##----------------------------------------------------------------------------
def max_body(max_bytes):
  """

  """
  def hook(req, resp, resource, params):
    length = req.content_length
    if length is not None and length > max_bytes:
      msg = "Request size (%s bytes) exceeds max-bytes: %s" % (str(length), str(max_bytes))
      raise falcon.HTTPPayloadTooLarge('Request error', msg)

  return( hook )

##----------------------------------------------------------------------------
class Router(object):

  ##--------------------------------------------------------------------------
  @falcon.before(max_body(64 * 1024))
  def on_post(self, req, resp):
    """
     Handle POST requests
    """
    try:
      json_data = self.parse_json(req)
      problem = json_data.get('problem', None)
      units = json_data.get('units', None)
      if problem is None:
        self.return_error( resp, falcon.HTTP_400, message='Missing required input parameter: [problem]')
        return

      d_resp = self.compute_answer(problem, units)
      resp.body = json.dumps(d_resp)
      resp.status = falcon.HTTP_200
    except Exception as e:
      message = "Request error: %s" % str(e)
      self.return_error( resp, falcon.HTTP_500, message=message) 

  ##--------------------------------------------------------------------------
  def on_get(self, req, resp, symbol=None):
    """
     Handle GET requests
    """
    math_const_list = ','.join(constants.keys())
    message = "GET a math constant (%s) as a resource, or POST a math problem in json format - example: {'problem': '(3*3)+2'}" % (math_const_list) 
    d_resp = {"type": "info", "message": message }
    if symbol is not None:
      if symbol not in math_const_list:
        message = "Invalid math constant: %s" % symbol 
        self.return_error( resp, falcon.HTTP_500, message=message) 
        return
      else:
        d_resp = {"constant": symbol, "value": constants[symbol] }

    resp.status = falcon.HTTP_200  
    resp.body = json.dumps(d_resp)

  ##--------------------------------------------------------------------------
  def return_error(self, resp, status_code, message=""):
    """
      Set resp.body and resp.status attributes on error condition 
    """
    resp.body = json.dumps({ 'type': 'error', 'message': message })
    resp.status = status_code

  ##--------------------------------------------------------------------------
  def parse_json(self, req):
    """
      Parse the request object to validate json format
      Req Arg: request object 
      Raises: InvalidRequestFormat() if invalid
      Return: None 
    """
    if req.content_length is None or req.content_length == 0:
      return None

    if req.content_type is not None and req.content_type.lower() == 'application/json':
      raw_body = req.stream.read(req.content_length or 0)
      if raw_body is None:
        return None

      try:
        json_body = json.loads(raw_body.decode('utf-8'))
        return(json_body)
      except json.JSONDecodeError as e:
        raise InvalidRequestFormat("%s: Invalid JSON in POST body: %s" % (req.path, e))
    else:
      raise InvalidRequestFormat("POST payload must be 'application/json' format")
  ##--------------------------------------------------------------------------
  def compute_answer(self, problem, units=None):
    """
      Use Calculator() to compute a math problem
      Return: dict resonse {'problem': problem, 'answer': answer }
    """

    d_init = {} ## not currently using this for anything 
    try:
      calc = Calculator(d_init)
    except Exception as e:
      raise

    try:
      answer = calc.compute(problem)
    except Exception as e:
      raise

    d_resp = {"problem": problem, "answer": answer}
    return(d_resp) 

