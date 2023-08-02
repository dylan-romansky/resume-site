#!/usr/bin/env python3

from flask import Flask, json, g, request
from flask.wrappers import Response
from api.res_it.service import Service as res_it
from flask_marshmallow import Marshmallow
from api.res_it.model import res_it as model
from api.res_it.schema import res_itSchema
from flask_cors import CORS
from flask_uuid import FlaskUUID
from time import sleep as sleep

app = Flask(__name__.split('.')[0])
if __name__ == "__main__":
	app.config.from_pyfile('dev.resume.cfg')
else:
	app.config.from_pyfile('prod.resume.cfg')
FlaskUUID(app)
service = None
while not service:
	print("heeheehee hoohoohoo")
	try:
		service = res_it(uri=app
				.config['SQL_ALCHEMY_DATABASE_URI']
				.replace('postgresql://', 'cockroachdb://'))
	except:
		sleep(1)
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

@app.route('/resume-item/<uuid:res_id>/', methods=['PATCH', 'PUT', 'GET', 'DELETE'])
def item(res_id):
	match request.method:
		case 'PATCH':
			return service.update_it(res_id, request)
		case 'PUT':
			return service.update_it(res_id, request)
		case 'GET':
			return service.find_it(res_id)
		case 'DELETE':
			return service.delete_it(res_id)

@app.before_request
def handle_preflight():
	if request.method == "OPTIONS":
		res = Response()
		res.headers['X-Content-Type-Options'] = '*'
		return res

def resume_api():
	app.run()

if __name__ == '__main__':
	app.run(debug=True)
