class Database(object):
	def __init__(self, adapter=None, uri=None):
		if not adapter:
			raise ValueError("Invalid database implementation")
		if not uri:
			raise ValueError("Invalid uri")
		self.client = adapter(uri=uri)

	def find_all(self, selector):
		return self.client.find_all(selector)

	def find(self, selector):
		return self.client.find(selector)

	def create(self, item):
		return self.client.create(item)

	def update(self, selector, item):
		return self.client.update(selector, item)

	def delete(self, selector):
		return self.client.delete(selector)
