#!/usr/bin/env python3

from .model import res_it
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import EXCLUDE, post_load

class res_itSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = res_it
		include_relationships = True
		load_instance = True
		unknown = EXCLUDE

#	@post_load
#	def make_instance(self, data, **kwargs):
#		return res_it.generate(data)
