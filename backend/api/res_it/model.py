#!/usr/bin/env python3

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class res_it(Base):
	__tablename__='res_it'
	id = Column(UUID(as_uuid=True), primary_key=True)
	name = Column(String)
	title = Column(String)
	startdate = Column(String)
	enddate = Column(String)
	content = Column(String)
	type = Column(String)

	def update_fields(self, item):
		self.id = item.id
		self.name = item.name
		self.title = item.title
		self.startdate = item.startdate
		self.enddate = item.enddate
		self.content = item.content
		self.type = item.type
