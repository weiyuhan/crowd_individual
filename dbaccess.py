from pymongo import MongoClient
from config import Config
import datetime
import os
import json
import time
import sys

class MongoWrapper(object):
	def __init__(self):
		self.client =  MongoClient(Config.mongodb_ip, Config.mongodb_port)
		self.db = self.client.CrowdJigsaw
		self.shapeArray = None

	def round_document(self):
		return self.db['rounds'].find_one({'round_id': Config.round_id})

	def edges_documents(self):
		return self.db['rounds'].find_one({'round_id': Config.round_id})['edges_saved']

	def shapes_documents(self):
		if not self.shapeArray:
			self.shapeArray = json.loads(self.db['rounds'].find_one({'round_id': Config.round_id})['shapeArray'])
		return self.shapeArray

	def cogs_documents(self, timestamp):
		""" get actions documents in-between start_time and end_time """
		return self.db['cogs'].find({'round_id': Config.round_id, \
											'time':{'$gt':0, '$lte':timestamp}})
	
	def __del__(self):
		self.client.close()

mongo_wrapper = MongoWrapper()
