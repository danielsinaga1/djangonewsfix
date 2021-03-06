"""
Django settings for djangonews project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&e%_5ch8_oqq@6q*pc9znu!qm7z4w6z3u0(fnjjew5b1+i@^rb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Configure the django-otp package.
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    # Enable two-factor auth.
    'allauth_2fa',
    'haystack',
    'ajax_select',
    'el_pagination',
    'captcha',
    'newsroom',
    'security',
    'payment',
    'socialmedia',
    'republisher',
    'clearcache',
    'blocks',
    'gallery',
    'pgsearch',
    'compressor',
    'letters',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # Configure the django-otp package. Note this must be after the
    # AuthenticationMiddleware.
    'django_otp.middleware.OTPMiddleware',

    # Reset login flow middleware. If this middleware is included, the login
    # flow is reset if another page is loaded between login and successfully
    # entering two-factor credentials.
    'allauth_2fa.middleware.AllauthTwoFactorMiddleware',

    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'djangonews.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'newsroom.context_processors.newsroom_template_variables',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'djangonews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'E:\ImplementationDjango\gu\storage.db',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'security.utils.StaffMinimumLengthValidator',
        'OPTIONS': {
            'staff_min_length': 10,
            'other_min_length': 8
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Greenwich'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SIDE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

FILEBROWSER_DIRECTORY = "uploads/"

FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
}

FILEBROWSER_SELECT_FORMATS = {
    'file': ['Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
}

FILEBROWSER_VERSIONS_BASEDIR = '_versions'

FILEBROWSER_MAX_UPLOAD_SIZE = 10485760

FILEBROWSER_NORMALIZE_FILENAME = True

FILEBROWSER_CONVERT_FILENAME = False

FILEBROWSER_OVERWRITE_EXISTING = False

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail',
                        'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail',
                  'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small',
              'width': 140, 'height': 100, 'opts': 'crop'},
    'medium': {'verbose_name': 'Medium',
               'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big',
            'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large',
              'width': 680, 'height': '', 'opts': ''},
    'extra_large': {'verbose_name': 'Extra large',
              'width': 750, 'height': '', 'opts': ''},
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'KEY_PREFIX': 'djangonews',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'KEY_PREFIX': 'djangonews',
    }
}

FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big',
                              'large', 'extra_large']

GRAPPELLI_INDEX_DASHBOARD = 'groundup.dashboard.CustomIndexDashboard'

GRAPPELLI_ADMIN_TITLE = "GroundUp Administration"

NEWSROOM_ARTICLE_COPYRIGHT = '&copy; ' + str(datetime.date.today().year) + \
                             ' GroundUp. <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="/static/newsroom/images/cc.png" /></a><br />This article is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.<p>You may republish this article, so long as you credit the authors and GroundUp, and do not change the text. Please include a link back to the original article.</p>'


NEWSROOM_SUPPORT_US_IMAGES = [
    'newsroom/images/SupportGroundUpAdvert-20180118.jpg',
]

NEWSROOM_LOGO = 'newsroom/images/GroundUpLogo-20170216.png'

# Spam prevention
NOCAPTCHA = True

# System now uses Postgres full text search. This is Only being kept live because of the

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename':'log.txt',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins', ],
            'propagate': True,
            'level': 'WARNING',
        },
    }
}

# DEPRECATED BUT CODE MUST BE REMOVED FROM VIEW FIRST
# advert_code_file_1 = open(os.path.join(BASE_DIR,
#                              "newsroom/templates/newsroom/advert_1.html"),
#                        "r")
# NEWSROOM_ADVERT_CODE_1 = advert_code_file_1.read()
# advert_code_file_2 = open(os.path.join(BASE_DIR,
#                                "newsroom/templates/newsroom/advert_2.html"),
#                        "r")
# NEWSROOM_ADVERT_CODE_2 = advert_code_file_2.read()

DONATE_PAGE = "/donate/"
#############

ACME_ADS = False
GOOGLE_ADS = False
AMAZON_ADS = False
AB_TEST_ADS = False

if AB_TEST_ADS:
    ADVERT_CODE_ACME = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_acme.html"),
                                "r").read()
    ADVERT_CODE_GOOGLE = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_google_responsive.html"),
                                "r").read()
    ADVERT_CODE_AMAZON = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/"
        "advert_amazon_gift_responsive.html"), "r").read()
elif ACME_ADS:
    NEWSROOM_ADVERT_CODE = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_acme_responsive.html"),
                                "r").read()
elif GOOGLE_ADS:
    NEWSROOM_ADVERT_CODE = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_google_responsive.html"),
                                "r").read()
else:
    NEWSROOM_ADVERT_CODE = ""

PIWIK_SITEID = 1
PIWIK_ENTRIES = 40

if DEBUG is True:
    INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar',]
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + \
        ['debug_toolbar.middleware.DebugToolbarMiddleware',]
