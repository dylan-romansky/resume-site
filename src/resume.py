#!/usr/bin/env python3

import uuid

from flask import Flask, request, render_template, url_for, flash, redirect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction

from models import res_it

app = Flask(__name__.split('.')[0])
app.config.from_pyfile('resume.cfg')
engine = create_engine(app.config['SQL_ALCHEMY_DATABASE_URI'].replace('postgresql://', 'cockroachdb://'))

def get_all(session, type=None):
	if type == None:
		return session.query(res_it).all()
	return session.query(res_it).filter(res_it.type == type).all()

def get_by_id(session, id):
	return session.query(res_it).filter(res_it.id == id).one()

def add_item(session, item):
	session.add(item)

def del_item(session, id):
	session.query(res_it).filter(res_it.id == id).delete()

def update_item(session, id, fields):
	item = session.query(res_it).filter(res_it.id == id).one()
	item.name = fields['name']
	item.title = fields['title']
	item.startdate = fields['startdate']
	item.enddate = fields['enddate']
	item.content = fields['content']

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/resume')
def resume():
	jobs = []
	edus = []
	session = sessionmaker(bind=engine)()
	for item in get_all(session):
		if item.type == 'job':
			jobs.append(item)
		else:
			edus.append(item)
	session.close()
	return render_template('resume.html', edus=edus, jobs=jobs)

@app.route('/add_edu', methods=('GET', 'POST'))
def edu():
	if request.method == 'POST':
		name = request.form['name']
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		content = request.form['content']

		if not name or not content:
			flash('name, and content required')
		else:
			run_transaction(sessionmaker(bind=engine),
					lambda session: add_item(session,
						res_it(id=uuid.uuid4(), name=name,
						startdate=startdate, enddate=enddate, content=content,
						type='edu')))
			return redirect(url_for('resume'))
	return render_template('edu.html')

@app.route('/add_job', methods=('GET', 'POST'))
def job():
	if request.method == 'POST':
		name = request.form['name']
		title = request.form['title']
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		content = request.form['content']

		if not name or not title or not startdate:
			flash('name, title, and start date required')
		else:
			run_transaction(sessionmaker(bind=engine),
					lambda session: add_item(session,
						res_it(id=uuid.uuid4(), name=name,
						title=title, startdate=startdate, enddate=enddate,
						content=content, type='job')))
			return redirect(url_for('resume'))
	return render_template('job.html')

@app.route('/<id>/edit', methods=('GET', 'POST'))
def edit(id):
	session = sessionmaker(bind=engine)()
	item = get_by_id(session, id)
	session.close()
	if request.method == 'POST':
		if request.form['type'] == 'edu' and not request.form['name'] and not request.form['content']:
			flash('name and description required')
		elif request.form['type'] == 'job' and not request.form['name'] and not request.form['title'] and not request.form['startdate']:
			flash('name, title, and start date required')
		else:
			run_transaction(sessionmaker(bind=engine), lambda session: update_item(session, id, request.form))
			return redirect(url_for('resume'))
	return render_template('edit.html', item=item)

@app.route('/<id>/delete', methods=('POST',))
def delete(id):
	session = sessionmaker(bind=engine)()
	session.close()
	print("OK BUT WE MADE IT HERE ALRIGHT JACKASS")
	run_transaction(sessionmaker(bind=engine), lambda session: del_item(session, id))
	return redirect(url_for('resume'))
