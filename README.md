This website was built in Flask. The data for the resume
items is stored in a CockroachDB cluster.

Then it was containerized and made deployable using Docker
and Kubernetes

Then a barebones frontend was made in Angular


Currently backend is being converted from a purely flask
application to purely an api that the Angular frontend
is capable of interacting with

Then once that's in place, the frontend can be made much
more functional and much more visually appealing

Then I will reimplement the Docker/Kubernetes deployments

After that a Terraform configuration will be made

The entire thing will be deployed to a cloud provider

Then finally a CI/CD pipeline will be put into place so
that any time I push an update from here, it gets deployed
simultaneously to the cloud provider I end up choosing

I will then be using tools such as Prometheus and
Graphana to learn how to monitor the health of my
website
