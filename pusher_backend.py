import pusher

class Pusher(object):
	@staticmethod
	def init(app_id, key, secret):
		Pusher.p = pusher.Pusher(
		  app_id=app_id,
		  key=key,
		  secret=secret,
		  ssl=True,
		  port=443
		)

	@staticmethod
	def message(channel, event, message):
		Pusher.p.trigger(channel, event, {'message': message})
