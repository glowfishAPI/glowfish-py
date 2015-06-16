import requests, json
import urllib3
urllib3.disable_warnings()

import config as config

class Glower(object):
	sid 					= None
	token 					= None
	
	params					= {}
	config					= config

	def __init__(self, _sid, _token, **kwargs):	
		setattr(self, 'sid', _sid)
		setattr(self, 'token', _token)
				
		for key, val in kwargs.iteritems():
			self.params[key] = val
		
	def use(self, set_name="default"):
		self.set_name = set_name
		
	def train(self, data_set, response):
		data = {
			"data_set": data_set,
			"response": response
		}
		return self._request('train', data)
		
	def train_csv(self, data_set, response):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set,
			"response": open(response, 'rb') if isinstance(response, (str, unicode)) else response
		}
		return self._request('train/csv', {}, files)
		
	def predict(self, data_set, response=None):
		data = {
			"data_set": data_set,
			"response": response
		}
		return self._request('predict', data)
		
	def predict_csv(self, data_set, response=None):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set
		}
		
		if response:
			files['response'] = open(response, 'rb') if isinstance(response, (str, unicode)) else response
		
		return self._request('predict/csv', {}, files)
		
	def cluster(self, data_set):
		data = {
			"data_set": data_set
		}
		return self._request('cluster', data)
		
	def cluster_csv(self, data_set):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set
		}
		return self._request('cluster/csv', {}, files)
		
	def feature_select(self, data_set, response):
		data = {
			"data_set": data_set,
			"response": response
		}
		return self._request('feature_select', data)
		
	def feature_select_csv(self, data_set, response):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set,
			"response": open(response, 'rb') if isinstance(response, (str, unicode)) else response
		}
		return self._request('feature_select/csv', {}, files)
		
	def filter_train(self, userids, productids, ratings):
		data = {
			"userid": userids,
			"productid": productids,
			"rating": ratings
		}
		
		return self._request('filter_train', {'data_set': data})
		
	def filter_train_csv(self, data_set):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set
		}
		
		return self._request('filter_train/csv', {}, files)
		
	def filter_predict(self, userids, productids, ratings):
		data = {
			"userid": userids,
			"productid": productids,
			"rating": ratings
		}
		
		return self._request('filter_predict', {'data_set': data})
		
	def filter_predict_csv(self, data_set):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set
		}
		
		return self._request('filter_predict', {}, files)
		
	def _request(self, endpoint, data, files=None):
		data.update(self.params)
		
		for key, val in data.iteritems():
			if isinstance(val, bool):
				data[key] = "true" if val is True else "false"
								
		url = "%s%s/%s/" % (self.config.API_ENDPOINT, self.config.API_VERSION, endpoint)
		if files:
			r = requests.post(url, data=data, files=files, auth=(self.sid, self.token))
		else:
			r = requests.post(url, json.dumps(data), auth=(self.sid, self.token))
		
		try:
			return r.json()
		except:
			r.raise_for_status()
			
	def __getattr__(self, name):
		if name in self.params:
			return self.params[name]
		return None
			
	def __setattr__(self, name, value):
		if name == "sid" or name == "token" or name == "params":
			super(Glower, self).__setattr__(name, value)
			return
		
		self.params[name] = value