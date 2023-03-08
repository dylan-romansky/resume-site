#!/usr/bin/env python3

import sqlite3
from flask import Flask, request, render_template, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

def get_item(id):
	conn = get_db_connection()
	item = conn.execute('SELECT * FROM res_it WHERE id = ?', (id,)).fetchone()
	conn.close()
	if item is None:
		abort(404)
	return item

app = Flask(__name__)
app.config['SECRET KEY'] = 'yeah put some secret method here at some point'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/resume')
def resume():
	conn = get_db_connection()
	edus = conn.execute("SELECT * FROM res_it WHERE type='edu'").fetchall()
	jobs = conn.execute("SELECT * FROM res_it WHERE type='job'").fetchall()
	conn.close()
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
			conn = get_db_connection()
			conn.execute('INSERT INTO res_it (name, start, end, content, type) VALUES (?, ?, ?, ?, ?)',
				(name, start, end, content, 'edu'))
			conn.commit()
			conn.close()
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

		if not name or not start or not end:
			flash('name, start, and end required')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO res_it (name, title, start, end, content, type) VALUES (?, ?, ?, ?, ?, ?)',
				(name, title, start, end, content, 'job'))
			conn.commit()
			conn.close()
			return redirect(url_for('resume'))
	return render_template('job.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
	item = get_item(id)

	if request.method == 'POST':
		name = request.form['name']
		title = request.form['title'] if request.form.get('title') else None
		start = request.form['start']
		end = request.form['end']
		content = request.form['content']
		if request.form['type'] == 'edu' and not name and not content:
			flash('name and description required')
		elif request.form['type'] == 'job' and not name and not start and not end:
			flash('name, start, and end required')
		else:
			conn = get_db_connection()
			conn.execute('UPDATE res_it SET name = ? , title = ?, start = ?, end = ?, content = ?'
							'WHERE id = ?', (name, title, start, end, content, id))
			conn.commit()
			conn.close()
			return redirect(url_for('resume'))
	return render_template('edit.html', item=item)
