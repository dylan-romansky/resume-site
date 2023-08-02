from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from ..res_it.model import res_it, Base
from ..res_it.schema import res_itSchema
from flask import json

#once this works as intended, see if you can use
#self.session to derive the specific session for
#each transaction this will run

class CrDB(object):
	def __init__(self, uri=None):
		if not uri:
			raise ValueError("Invalid database uri")
		self.db = create_engine(uri)
		#I have no clue if the below will work
		if not self.db:
			raise ValueError("CrDB failed to create engine")
		#determine how to check if table exists
		Base.metadata.create_all(self.db)
		self.session = sessionmaker(bind=self.db)

	#in the future, use the selector that the
	#frontend sends us to inform us which group of
	#items to return based on how they are tagged.
	#perhaps using a list of tag strings
	def find_all(self, selector):
		session = sessionmaker(bind=self.db)()
		return session.query(res_it).all()

	def find(self, selector):
		session = sessionmaker(bind=self.db)()
		return session.query(res_it).filter(res_it.id == selector).one()

	def create(self, item):
		sess = sessionmaker(bind=self.db)()
		thing = json.loads(item.data)
		thing.pop('id')
		it = res_itSchema().load(thing, session=sess)
		sess.commit()
		run_transaction(sess,
				lambda session: session.add(it))
		return it
	#best rest practice is to return url of newly
	#created resource so do that in the future

	def update(self, selector, item):
		sess = sessionmaker(bind=self.db)()
		#it = res_itSchema(exclude=['id']).load(json.loads(item.data), session=sess)
		it = res_itSchema().load(json.loads(item.data), session=sess)
		sess.commit()
		run_transaction(sess,
				lambda session:
					session.query(res_it)
					.filter(res_it.id == selector)
					.one().update_fields(it))
		return item

	def delete(self, selector):
		run_transaction(sessionmaker(bind=self.db),
				lambda session:
					session.query(res_it)
					.filter(res_it.id == selector)
					.delete())
		return '' #find a way for a 204 response code. possibly defined at the endpoints
