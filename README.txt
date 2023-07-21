File Structrue:
FirstApp/
    accounts/
        migrations/
	    __init__.py
	templates/
	    accounts/
	        login.html
		logout.html
		register.html
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
    assets/
	admin/
	    ...
	bootstrap/
	    ...
	images/
	    ...
	jquery/
	    ...
	jquery-ui/
	    ...
	js/
	    ...
	plugins/
	    ...
	styles/
	    ...
    destinations/
        migrations/
	    __init__.py
	templates/
	    destinations/
	         all_destinations.html
		 details.html
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
    Lib/
        site-packages/
	    ...
    media/
	pics/
	    ...
    static/
        FirstApp/
	    images/
	        ...
	    js/
	        ...
	    plugins/
	        ...
	    styles/
	        ...
    travello/
	migrations/
	    __init__.py
	    0001_initial.py
	    0002_auto_20200526_1451.py
	    0003_guide.py
	    0004_auto_20210530_0432.py
	    0005_auto_20210530_1532.py
	    0006_auto_20210530_1918.py
	    0007_remove_destination_end_time.py
	    0008_auto_20210530_1928.py
	    0009_auto_20210530_1937.py
	templates/
	    travello/
	        index.html
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
    manage.py
    README.txt

Resources:
   - "Telusko" on youtube
   - https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django

Glossary:
"project" - a collection of settings for an instance of Django, including: database configuration, Django-specific options, and application-specific settings. can contain mulitple apps
"view" - a 'type' of Web page in an app that generally serves a specific function and has a specific template
"asset" - css image to serve

Future Ideas:
   - https://alexpnt.github.io/2017/07/15/django-calendar/
