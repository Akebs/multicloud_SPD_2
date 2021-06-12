[![Python application test with Github Actions](https://github.com/Akebs/multi-cloud/actions/workflows/main.yml/badge.svg)](https://github.com/Akebs/multi-cloud/actions/workflows/main.yml)

# Cloud Services Testing (AWS,GCP,MSA)


This a Amazon Web Services, Google Cloud Platform and Microsoft Azure implementation of Pragmatic AI Labs tutorial: "1:1 multi cloud onboarding with cloud computing"

<a href="https://youtu.be/zznvjk0zsVg">  <img src="https://i.ytimg.com/vi/zznvjk0zsVg/maxresdefault.jpg" width="480" > </a>


It creates a python app, in these cloud platforms, that adds two given values.

It also includes a Github Actions workflow to install list, test and format the code. Upon conclusion, it refreshes the execution success badge on top.

A Django frame is used to generate a simple form view to input integer values and display the add result.

## Notes:

Required local modifications in settings.py are in included folders for each cloud provider.

    AWS & Azure: ALLOWED_HOSTS is set to include the value of the CNAME/WEBSITE_HOSTNAME environment variable, if present. Cloud providers automatically sets this environment variable upon deployment to the app's URL.

    AWS & Azure: The DATABASES object is commented out (using """) so that the app doesn't attempt to use a database at all. To use a database, remove the comments and modify the values as appropriate for your database.
    
    Gcloud: App Engine by default looks for a main.py file at the root of the app directory with a WSGI-compatible object called app. To acomodate this, the file main.py, in the root of the gcloud django project, references the aplication as app.

## More info:

Pragmatic AI Labs <a href="https://paiml.com/docs/home/books/cloud-computing-for-data/"> Cloud Computing for Data Analysis </a>

AWS deployment <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-deploy"> Deploying a Django application to Elastic Beanstalk </a>

MSA deployment <a href="https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-django"> Quickstart: Create a Python app using Azure App Service on Linux </a>

GCP deployment <a href="https://cloud.google.com/python/django"> Getting started with Django </a>
