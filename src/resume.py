#!/usr/bin/env python3

from flask import Flask, request, render_template, url_for, flash, redirect
from werkzeug.exceptions import abort
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = "golly gee this key sure is secret"
app.config['MYSQL_DATABASE_HOST'] = 'mysql-db'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'res_it'
mysql = MySQL(app)

class _item:
	id: int
	name: str
	title: str
	start: str
	end: str
	content: str
	type: str
	def __init__(self, args):
		self.id = args[0]
		self.name = args[1]
		self.title = args[2]
		self.start = args[3]
		self.end = args[4]
		self.content = args[5]
		self.type = args[6]

def get_db_connection():
	conn = mysql.connect()
	return conn

def get_item(id: int):
	conn = get_db_connection()
	cur = conn.cursor()
	cur.execute('SELECT * FROM res_it WHERE id = %s', (id,))
	it = cur.fetchall()
	cur.close()
	conn.close()
	if it is None:
		abort(404)
	return _item(it[0])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/resume')
def resume():
	conn = get_db_connection()
	cur = conn.cursor()
	cur.execute("SELECT * FROM res_it WHERE type='edu'")
	edus = []
	for edu in cur.fetchall():
		edus.append(_item(edu))
	cur.execute("SELECT * FROM res_it WHERE type='job'")
	jobs = []
	for job in cur.fetchall():
		jobs.append(_item(job))
	cur.close()
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
			conn = get_db_connection()
			cur = conn.cursor()
			cur.execute('INSERT INTO res_it (name, start, end, content, type) VALUES (%s, %s, %s, %s, %s)',
				(name, start, end, content, 'edu'))
			conn.commit()
			cur.close()
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
			cur = conn.cursor()
			cur.execute('INSERT INTO res_it (name, title, start, end, content, type)'
							'VALUES (%s, %s, %s, %s, %s, %s)',
							(name, title, start, end, content, 'job'))
			conn.commit()
			cur.close()
			conn.close()
			return redirect(url_for('resume'))
	return render_template('job.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id: int):
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
			cur = conn.cursor()
			cur.execute('UPDATE res_it SET name = %s , title = %s, start = %s, end = %s,'
			   'content = %s WHERE id = %s', (name, title, start, end, content, id))
			conn.commit()
			cur.close()
			conn.close
			return redirect(url_for('resume'))
	return render_template('edit.html', item=item)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id: int):
	item = get_item(id)
	conn = get_db_connection()
	cur = conn.cursor()
	cur.execute('DELETE FROM res_it WHERE id = %s', (id))
	cur.close()
	conn.commit()
	conn.close()
	flash('"{}" was successfully deleted!'.format(item.name))
	return redirect(url_for('resume'))
