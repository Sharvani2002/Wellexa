"""
Django settings for Wellexa project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hji*6=**f#7%6@wu15qir+)nwoo=md$fkh5ajt80ou=gm+o@1u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # 'honeybadger.contrib.DjangoHoneybadgerMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Wellexa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['templates'],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Wellexa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

HONEYBADGER = {
  'API_KEY': '8858316b'
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
# import keras
# import numpy as np
# # from keras import backend as K
# # import tensorflow.keras.backend as K
# import tensorflow.compat.v1 as tf
# import tensorflow.compat.v1.keras.backend as K
# # import tensorflow as tf
# from tensorflow.python.keras.backend import set_session
# # from keras.applications import vgg16
# from keras.models import load_model
# from tensorflow.python.keras.backend import get_session



# # def get_session():
# #     config = tf.ConfigProto()
# #     config.gpu_options.allow_growth = True
# #     return tf.compat.v1.Session(config=config)

# # # tf.keras.backend.clear_session()
# # # with tf.Session():

# # # K.tensorflow_backend.set_session(get_session())
# # K.set_session(get_session())
# # # tf.compat.v1.keras.backend.set_session(get_session())
# # config = tf.compat.v1.ConfigProto()
# # config.gpu_options.allow_growth = True
# # SESS = tf.compat.v1.Session(config=config)
# # print("model loading")
# # GRAPH1 = tf.get_default_graph()

# # K.set_session(SESS)
# # # Load the VGG model
# # VGG_MODEL = vgg16.VGG16(weights="imagenet")
# # Load the personally trained model

# # MY_MODEL = load_model('best_model.h5')
# tf.keras.backend.clear_session()
# def get_session():
#     config = tf.ConfigProto()
#     config.gpu_options.allow_growth = True
#     return tf.Session(config=config)

# K.set_session(get_session())

# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True
# SESS = tf.Session(config=config)
# print("model loading")
# GRAPH1 = tf.get_default_graph()

# set_session(SESS)
# # Load the VGG model
# # VGG_MODEL = vgg16.VGG16(weights="imagenet")
# MY_MODEL = load_model('best_model.h5')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'