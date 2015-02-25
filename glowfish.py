import requests, json

import config as config

class Glower(object):
	sid 					= None
	token 					= None
	
	set_name 				= "default"
	
	fail_if_mistakes		= False
	delete_previous_data	= False
	save_data				= False
	stats					= False
	hold					= False
	update					= False
	
	max_number				= -1
	accuracy				= False
	group_max_number		= -1
	

	def __init__(self, sid, token):
		self.sid 	= sid
		self.token 	= token
		
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
		
	def predict(self, data_set):
		data = {
			"data_set": data_set
		}
		return self._request('predict', data)
		
	def predict_csv(self, data_set):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set
		}
		return self._request('predict', {}, files)
		
	def cluster(self, data_set):
		data = {
			"data_set": data_set
		}
		return self._request('cluster', data)
		
	def cluster_csv(self, data_set):
		files = {
			"data_set": open(data_set, 'rb') if isinstance(data_set, (str, unicode)) else data_set
		}
		return self._request('cluster', {}, files)
		
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
		return self._request('feature_select', {}, files)
		
	def _request(self, endpoint, data, files=None):
		data['fail_if_mistakes'] = self.fail_if_mistakes
		data['delete_previous_data'] = self.delete_previous_data
		data['save_data'] = self.save_data
		data['stats'] = self.stats
		data['hold'] = self.hold
		data['update'] = self.update
		data['max_number'] = self.max_number
		data['accuracy'] = self.accuracy
		data['group_max_number'] = self.group_max_number
		
		url = "%s%s/%s/" % (config.API_ENDPOINT, config.API_VERSION, endpoint)
		if files:
			r = requests.post(url, data=data, files=files, auth=(self.sid, self.token))
		else:
			r = requests.post(url, json.dumps(data), auth=(self.sid, self.token))
		
		try:
			return r.json()
		except:
			r.raise_for_status()
		
		
#glower = Glower('Grpnx1KDiNVDi6UEkjHNfVZTPyWSsdyJ', 'sarvnQ48jcAiDM9hu8lnzcAHNJ33NBa0')
#print glower.train({'feature_1': [1,2,3,4,5,6,7]}, {'class': [0,9,8,7,6,5,4]})
#print glower.train_csv('./airfoil_train_regression_statsFalse_holdFalse_features.csv', './#airfoil_train_regression_statsFalse_holdFalse_responses.csv')