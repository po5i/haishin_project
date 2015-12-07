# Shippify python client
# carlos.po5i@gmail.com
# @po5i

"""
STATUS
0	Cancelled
1	Getting ready
2	Pending to assign
3	Pending for shipper response
4	Shipper confirmed
5	Being picked up
6	Being delivered
7	Delivered successfully
"""

"""
PAYMENT TYPES:
1	Credit - pay with credit card
2	Cash - pay in cash
3	Bank transfer - Pay in a bank transfer
4	Debit - Pay with debit card
5	Boleto - Pay with boleto (brasil)
"""

"""
PAYMENT STATUS:
1	Not paid
2	Paid
"""

"""
SIZES
1	Extra Small (XS) - Keys, papers, documents.
2	Small (S) - Tedy Bears, Shoe's box, keyboard, Ipad.
3	Medium (M)- Laptop, PC, monitor.
4	Large (L)- Chair, a small desk, bicycle.
5	Extra large (XL) - Desk, furniture, boat.
"""

import requests

# Authorization: "Basic <apiKeyId>:<apiSecretId>"
# Testing API KEYS:

class Configuration(object):
	@staticmethod
	def set_credentials(api_key, api_secret, debug=True):
		Configuration.SHIPPIFY_API_KEY = api_key
		Configuration.SHIPPIFY_API_SECRET = api_secret
		Configuration.SHIPPIFY_DEBUG = debug

	@staticmethod
	def headers():
		return {
			'Authorization': 'Basic %s:%s' % (Configuration.SHIPPIFY_API_KEY, Configuration.SHIPPIFY_API_SECRET)
		}

class Task(object):
	@staticmethod
	def create_task(api_data):
		# POST https://services.shippify.co/task/new
		if Configuration.SHIPPIFY_DEBUG:
			endpoint = 'https://staging.shippify.co/task/new'
		else:
			endpoint = 'https://services.shippify.co/task/new'

		response = requests.post(endpoint, json=api_data, auth=(Configuration.SHIPPIFY_API_KEY, Configuration.SHIPPIFY_API_SECRET))
		#print response.request.body
		#print response.json()

		if response.status_code > 201:
			raise Exception('Error %d: %s' % (response.status_code,response.text))
		elif response.json()['errFlag'] != 0:
			raise Exception('Error Flag %d: %s' % (response.json()['errFlag'],response.json()['errMsg']))
		else:
			return response.json()

	@staticmethod
	def get_task(task_id):
		# GET https://services.shippify.co/task/info/:taskId
		if Configuration.SHIPPIFY_DEBUG:
			endpoint = 'https://staging.shippify.co/task/info/%s' % task_id
		else:
			endpoint = 'https://services.shippify.co/task/info/%s' % task_id

		response = requests.get(endpoint, auth=(Configuration.SHIPPIFY_API_KEY, Configuration.SHIPPIFY_API_SECRET))

		if response.status_code > 201:
			raise Exception('Error %d: %s' % (response.status_code,response.text))
		elif response.json()['errFlag'] != 0:
			raise Exception('Error Flag %d: %s' % (response.json()['errFlag'],response.json()['errMsg']))
		else:
			return response.json()

