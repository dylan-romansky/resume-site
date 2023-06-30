#!/usr/bin/env python3

from .model import res_it
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class res_itSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = res_it
		include_relationships = True
		load_instance = True
