#!/usr/bin/env python3

from flask import Flask, json, g, request
from api.res_it.service import Service as res_it

app = Flask(__name__.split('.')[0])
app.config.from_pyfile('dev.resume.cfg')
service = res_it(uri=app.config['SQL_ALCHEMY_DATABASE_URI'].replace('postgresql://', 'cockroachdb://'))
