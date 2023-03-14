FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN apt-get update; apt-get upgrade -y; \
	apt-get install -y nginx supervisor; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	useradd --no-create-home nginx; \
	rm /etc/nginx/sites-enabled/default; \
	rm -r /root/.cache
COPY serv_config/nginx.conf /etc/nginx/
COPY serv_config/flask-nginx.conf /etc/nginx/conf.d/
COPY serv_config/uwsgi.ini /etc/uwsgi/
COPY serv_config/supervisord.conf /etc/
COPY resume.py .
COPY models.py .
COPY static .
COPY templates .
COPY __init__.py .
CMD supervisord
