#!/usr/bin/env python3

from flask import Flask, json, g, request
from api.res_it.service import Service as res_it
from flask_marshmallow import Marshmallow
from api.res_it.model import res_it as model
from api.res_it.schema import res_itSchema
from flask_cors import CORS

app = Flask(__name__.split('.')[0])
app.config.from_pyfile('dev.resume.cfg')
service = None
while not service:
	try:
		service = res_it(uri=app
				.config['SQL_ALCHEMY_DATABASE_URI']
				.replace('postgresql://', 'cockroachdb://'))
	except:
		#add a wait here to avoid excessive requests
		continue
ma = Marshmallow(app)
schema = res_itSchema()
CORS(app)

@app.route('/resume-item/', methods=['POST', 'GET'])
def items():
	match request.method:
		case 'POST':
			return service.create_it(request)
		case 'GET':
			return service.find_all_its()

@app.route('/resume-item/<int:res_id>/', methods=['PATCH', 'PUT', 'GET', 'DELETE'])
def item(res_id):
	match request.method:
		case 'PATCH':
			return service.update_it(res_id, model.from_json(request))
		case 'PUT':
			return service.update_it(res_id, model.from_json(request))
		case 'GET':
			return service.find_it(res_id)
		case 'DELETE':
			return service.delete_it(res_id)

if __name__ == '__main__':
	app.run(debug=True)
