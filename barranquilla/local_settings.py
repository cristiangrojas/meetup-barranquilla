# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'barranquilla',
        'USER': 'cristianrojas',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}