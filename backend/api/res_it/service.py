#!/usr/bin/env python3

from .model import res_it as model
from .schema import res_itSchema
from ..db import Database
from ..db.crdb import CrDB
from flask import json

#TODO: adapt the crdb adapter to return values consistent with the methods in this service, adapt the methods in this service to send arguments consistent with the adapter methods?

class Service(object):
	def __init__(self, uri=None):
		if not uri:
			raise ValueError("Service: no uri specified")
		self.db = Database(adapter=CrDB, uri=uri)

	def find_all_its(self):
		res_its = self.db.find_all(selector=None)
		return [self.dump(it) for it in res_its]

	def find_it(self, res_id):
		it = self.db.find({'id': res_id})
		return self.dump(it)

	def create_it(self, it):
		self.db.create(it)
		return self.dump(it.data)

	def update_it(self, res_id, it):
		self.db.update(res_id, it)
		return self.dump(it.data)

	def delete_it(self, res_id):
		self.db.delete(res_id)
		return '', 204 #problematic in a HATEOAS environment

	def dump(self, data):
		return res_itSchema().dump(data)
