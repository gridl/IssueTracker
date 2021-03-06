# Django settings for IssueTracker project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
HOME = os.path.dirname(__file__)

ADMINS = (
     ('Nicholas Tollervey', 'ntoll@ntoll.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'issue_tracker_db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = HOME + '/static'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'cdy-$^-rk^n@md2b+&5in885zjcy*ng7c3)%(ve#i+rtesr4h^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'IssueTracker.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    HOME + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.comments',
    'workflow',
    'project',
    'tracker',
)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_SUBJECT_PREFIX = '[IssueTracker]'

# Path to graphviz's dot command
GRAPHVIZ_DOT_COMMAND = 'dot'

DEFAULT_CHARSET = 'utf-8'

# The default path (in URL) for the login page
LOGIN_URL = '/login'
# Where a successful login should redirect should a "next" argument not be
# supplied in the URI
LOGIN_REDIRECT_URL = '/'

# Registration defaults:
REGISTRATION_USE_HTTPS = False
REGISTRATION_EMAIL_TEMPLATE = 'register_email.html'
NEW_TICKET_EMAIL_TEMPLATE = 'new_ticket_email.html'

# Role defaults
ROLE_SUBMITTER = 1
ROLE_ASSIGNEE = 3 
ROLE_MANAGER = 2

# Specify your custom test runner to use
TEST_RUNNER='workflow.test_runner.test_runner_with_coverage'

# List of modules to enable for code coverage
COVERAGE_MODULES = ['workflow.models', 'workflow.views', 'project.models',
        'tracker.models', 'tracker.forms', 'tracker.views']

# Including a settings_local allows you to override these settings with
# something more appropriate for your machine
try:
        from settings_local import *
except:
        pass
