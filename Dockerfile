FROM python:3.9.16-bullseye

WORKDIR /app

COPY ./src/requirements.txt /app
RUN pip install -r requirements.txt
COPY ./src/resume.py ./src/database.db ./src/schema.sql \
		./src/templates ./src/static ./src/init_db.py .
RUN ./init_db.py
EXPOSE 5000
ENV FLASK_APP=resume.py
CMD ["flask", "run", "--host", "0.0.0.0"]
