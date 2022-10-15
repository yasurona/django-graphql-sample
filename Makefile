.PHONY: build up exec _python_script _django_admin _django_manage project app makemigrations showmigrations squashmigrations migrate _admin admin _dumpdata dumpdata _loaddata loaddata loadalldata dbshell

define dc
	docker-compose $1
endef

build:
	$(call dc,build)

up:
	$(call dc,up -d --build)

exec:
	$(call dc,exec $(service) $(cmd))

_python_script:
	$(MAKE) exec service='web' cmd='python $(path) $(arg)'

_django_admin:
	$(MAKE) exec service='web' cmd='django-admin $(cmd)'

_django_manage:
	$(MAKE) _python_script path='manage.py' arg='$(cmd)'

project:
	$(MAKE) _django_admin cmd='startproject $(PROJECT) .'

app:
	$(MAKE) exec service='web' cmd='mkdir -p apps/$(APP)'
	$(MAKE) _django_admin cmd='startapp $(APP) apps/$(APP)'

makemigrations:
	$(MAKE) _django_manage cmd='makemigrations $(APP)'

showmigrations:
	$(MAKE) _django_manage cmd='showmigrations $(APP)'

squashmigrations:
	$(MAKE) _django_manage cmd='squashmigrations $(APP) $(FROM) $(UNTIL)'

migrate:
	$(MAKE) _django_manage cmd='migrate'

_admin:
	$(MAKE) _django_manage cmd='createsuperuser $(option)'

admin:
	$(MAKE) _admin option='--noinput'

_dumpdata:
	$(MAKE) _django_manage cmd='dumpdata $(option) -o $(output)'

dumpdata:
	$(MAKE) _dumpdata output='data.json.gz'

_loaddata:
	$(MAKE) _django_manage cmd='loaddata $(option) $(fixture)'

loaddata:
	$(MAKE) _loaddata option='--exclude user --exclude admin --exclude auth.permission --exclude contenttypes' fixture='data.json'

loadalldata:
	$(MAKE) _loaddata option='--exclude auth.permission --exclude contenttypes' fixture='data.json'

dbshell:
	$(MAKE) _django_manage cmd='dbshell'
