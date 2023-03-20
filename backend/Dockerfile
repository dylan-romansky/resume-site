FROM python:latest

WORKDIR /app

COPY requirements.txt .
COPY secrets/certs/ca.crt /certs/ca.crt
COPY secrets/certs/client.root.crt /certs/client.root.crt
COPY secrets/certs/client.root.key /certs/client.root.key
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
COPY resume.cfg .
COPY models.py .
COPY static ./static
COPY templates/ ./templates
COPY __init__.py .
CMD supervisord

EXPOSE 80
