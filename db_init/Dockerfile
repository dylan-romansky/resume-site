FROM cockroachdb/cockroach:v22.2.6

COPY schema.sql /docker-entrypoint-initdb.d/schema.sql
#CMD cockroach init --insecure; cockroach start --insecure --join cockroachdb
