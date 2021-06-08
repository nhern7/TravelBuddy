This Django project was done to learn the framework and, afterwards, experiment with different functionalities/advanced techniques. 


resources:
Telusko on youtube
https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django

glossary:
"app" a web application that does something. can be used within multiple projects
"project" is a collection of settings for an instance of Django, including: 
database configuration, Django-specific options, and application-specific settings. can contain mulitple apps
"travello" is the name of our fake website that we are learning with. is an app
"FirstApp" is the name of our django project that we are learning with
"view" is a 'type' of Web page in an app that generally serves a specific function and has a specific template
"asset" css or js or image that we want an app to serve

directory_layout:
FirstApp/
    accounts/
        migrations/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
    assets/
	admin/
	images/
	js/
	plugins/
	styles/
    calc/
	migrations/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
    FirstApp/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    media/
	pics/
    static/
	images/
	js/
	plugins/
	styles/
    templates/
	base.html
	home.html
	index.html
	register.html
	result.html
    travello/
	migrations/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
    manage.py
    README.txt

errors:

scheduler idea:
https://alexpnt.github.io/2017/07/15/django-calendar/
