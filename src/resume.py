#!/usr/bin/env python3

import uuid

from flask import Flask, request, render_template, url_for, flash, redirect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction

from models import res_it

app = Flask(__name__.split('.')[0])
app.config.from_pyfile('resume.cfg')
engine = create_engine(app.config['SQL_ALCHEMY_DATABASE_URI'])

def get_all(session, type):
	return session.query(res_it).filter(res_it.type == type).all()

def get_by_id(session, id):
	return session.query(res_it).filter(res_it.id == id).one()

def add_item(session, item):
	session.add(item)

def del_item(session, id):
	session.delete(id)

def update_item(session, id, fields):
	item = session.query().filter(res_it.id == id).one()
	item.name = fields['name']
	item.title = fields['title']
	item.start = fields['start']
	item.end = fields['end']
	item.content = fields['content']

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/resume')
def resume():
	edus = run_transaction(sessionmaker(bind=engine),
				lambda session: get_all(session, 'edu'))
	jobs = run_transaction(sessionmaker(bind=engine),
				lambda session: get_all(session, 'job'))
	print("edus = " + str(edus))
	print("jobs = " + str(jobs))
	return render_template('resume.html', edus=edus, jobs=jobs)

@app.route('/add_edu', methods=('GET', 'POST'))
def edu():
	if request.method == 'POST':
		name = request.form['name']
		start = request.form['start']
		end = request.form['end']
		content = request.form['content']

		if not name or not content:
			flash('name, and content required')
		else:
			run_transaction(sessionmaker(bind=engine),
					lambda session: add_item(session,
						res_it(id=uuid.uuid4(), name=name,
						start=start, end=end, content=content,
						type='edu')))
			return redirect(url_for('resume'))
	return render_template('edu.html')

@app.route('/add_job', methods=('GET', 'POST'))
def job():
	if request.method == 'POST':
		name = request.form['name']
		title = request.form['title']
		start = request.form['start']
		end = request.form['end']
		content = request.form['content']

		if not name or not title or not start:
			flash('name, title, and start required')
		else:
			run_transaction(sessionmaker(bind=engine),
					lambda session: add_item(session,
						res_it(id=uuid.uuid4(), name=name,
						title=title, start=start, end=end,
						content=content, type='job')))
			return redirect(url_for('resume'))
	return render_template('job.html')

@app.route('/<id>/edit', methods=('GET', 'POST'))
def edit(id):
	item = res_it.query.filter(id=id)
	if request.method == 'POST':
		if request.form['type'] == 'edu' and not request.form['name'] and not request.form['content']:
			flash('name and description required')
		elif request.form['type'] == 'job' and not request.form['name'] and not request.form['title'] and not request.form['start']:
			flash('name, title, and start required')
		else:
			run_transaction(sessionmaker(bind=engine), lambda session: update_item(session, id, request.form))
			return redirect(url_for('resume'))
	return render_template('edit.html', item=item)

@app.route('/<id>/delete', methods=('POST',))
def delete(id):
	item = run_transaction(sessionmaker(bind=engine), lambda session: get_by_id(session, id))
	run_transaction(sessionmaker(bind=engine), lambda session: del_item(session, id))
	flash('"{}" was successfully deleted!'.format(item.name))
	return redirect(url_for('resume'))
