#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class res_it(Base):
	__tablename__='res_it'
	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	#id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
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

	@staticmethod
	def generate(data):
		id = data['id'] if 'id' in data else None
		name = data['name'] if 'name' in data else None
		title = data['title'] if 'title' in data else None
		startdate = data['startdate'] if 'startdate' in data else None
		enddate = data['enddate'] if 'enddate' in data else None
		content = data['content'] if 'content' in data else None
		type = data['type'] if 'type' in data else None
		return res_it(id=id, name=name, title=title, startdate=startdate, enddate=enddate, content=content, type=type)
