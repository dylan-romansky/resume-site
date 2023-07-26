#Use this as reference for setting up
#an NginX container to connect the
#frontend and backend

FROM python:latest

WORKDIR /app

COPY requirements.txt .
COPY setup_venv.sh .
COPY secrets/certs/ca.crt /certs/ca.crt
COPY secrets/certs/client.root.crt /certs/client.root.crt
COPY secrets/certs/client.root.key /certs/client.root.key
RUN apt-get update; apt-get upgrade -y; \
	apt-get install -y nginx supervisor; \
	./setup_venv.sh; \
	useradd --no-create-home nginx; \
	rm /etc/nginx/sites-enabled/default; \
	rm -r /root/.cache
COPY serv_config/nginx.conf /etc/nginx/
COPY serv_config/flask-nginx.conf /etc/nginx/conf.d/
COPY serv_config/uwsgi.ini /etc/uwsgi/
COPY serv_config/supervisord.conf /etc/
COPY resume.py .
COPY prod.resume.cfg .
COPY api .
COPY __init__.py .
RUN chown root:nginx /certs/*; chmod 640 /certs/client.root.key
CMD supervisord

EXPOSE 80
