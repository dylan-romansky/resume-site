FROM python:latest

WORKDIR /app

COPY requirements.txt .
COPY setup_venv.sh .
COPY secrets/certs/ca.crt /certs/ca.crt
COPY secrets/certs/client.root.crt /certs/client.root.crt
COPY secrets/certs/client.root.key /certs/client.root.key
RUN apt-get update; apt-get upgrade -y; \
	./setup_venv.sh;
COPY resume.py .
COPY prod.resume.cfg ./resume.cfg
COPY api .
COPY __init__.py .

EXPOSE 5000

CMD ["./.env/bin/gunicorn", "--bind", "0.0.0.0:5000", "resume:app"]
