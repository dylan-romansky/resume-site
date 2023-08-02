FROM python:latest

WORKDIR /app

COPY requirements.txt .
COPY setup_venv.sh .
COPY secrets/certs/ca.crt /certs/ca.crt
COPY secrets/certs/client.root.crt /certs/client.root.crt
COPY secrets/certs/client.root.key /certs/client.root.key
COPY resume.py .
COPY prod.resume.cfg ./prod.resume.cfg
#TODO: remove when ready for production
COPY dock.resume.cfg ./dev.resume.cfg
COPY api ./api
COPY __init__.py .
RUN apt-get update; apt-get upgrade -y; \
	./setup_venv.sh;

EXPOSE 5000

#CMD ["/bin/bash"]
#CMD ["./.env/bin/python", "./resume.py"]
CMD ["./.env/bin/gunicorn", "--bind=0.0.0.0:5000", "--worker-class=gevent", "--timeout=120", "resume:app"]
