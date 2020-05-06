class SimpleMath(object):

	def on_get(self, req, resp):
		payload = {"problem": "1+1", "answer": 0}

		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
