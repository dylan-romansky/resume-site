FROM python:3.9.16-bullseye

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
RUN ./init_db.py
EXPOSE 5000
ENV FLASK_APP=resume.py
CMD ["flask", "run", "--host", "0.0.0.0"]
