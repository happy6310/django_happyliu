
# 基于Django OAuth Toolkit 实例
自己学习使用django oauth tookit 

## 创建项目目录

```
 mkdir  django_happyliu
 cd django_happyliu
 mkdir -p templates/registration
```
##创建虚拟环境

```
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
```
##安装依赖

```
pip install django 
pip install django-oauth-toolkit 
pip install django-cors-middleware 
```
##创建工程Django_oauth_project 及应用 Django_oauth_app

```
django-admin startproject Django_oauth_project
cd Django_oauth_project
django-admin startapp Django_oauth_app
```
## 配置 settings.py

```
...
INSTALLED_APPS = [
    ...
    'oauth2_provider',
    'corsheaders',
    'Resource_app',
]
....
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]

....
CORS_ORIGIN_ALLOW_ALL = True

```

## 配置urls

```
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url  # 注意这里


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Resource_app.urls')),
]

```
##配置数据库

```
python manage.py migrate
```
##配置django管理员账号 
```
python manage.py createsuperuser --email admin@example.com --username admin
```
8.复制templates/base.html
> 复制django_happyliu/venv/lib/python3.7/site-packages/django/contrib/admin/templates/admin/base.html

```
{% load i18n static %}<!DOCTYPE html>
{% get_current_language as LANGUAGE_CODE %}{% get_current_language_bidi as LANGUAGE_BIDI %}
<html lang="{{ LANGUAGE_CODE|default:"en-us" }}" {% if LANGUAGE_BIDI %}dir="rtl"{% endif %}>
<head>
<title>{% block title %}{% endblock %}</title>
<link rel="stylesheet" type="text/css" href="{% block stylesheet %}{% static "admin/css/base.css" %}{% endblock %}">
{% block extrastyle %}{% endblock %}
{% if LANGUAGE_BIDI %}<link rel="stylesheet" type="text/css" href="{% block stylesheet_rtl %}{% static "admin/css/rtl.css" %}{% endblock %}">{% endif %}
{% block extrahead %}{% endblock %}
{% block responsive %}
    <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{% static "admin/css/responsive.css" %}">
    {% if LANGUAGE_BIDI %}<link rel="stylesheet" type="text/css" href="{% static "admin/css/responsive_rtl.css" %}">{% endif %}
{% endblock %}
{% block blockbots %}<meta name="robots" content="NONE,NOARCHIVE">{% endblock %}
</head>
{% load i18n %}

<body class="{% if is_popup %}popup {% endif %}{% block bodyclass %}{% endblock %}"
  data-admin-utc-offset="{% now "Z" %}">

<!-- Container -->
<div id="container">

    {% if not is_popup %}
    <!-- Header -->
    <div id="header">
        <div id="branding">
        {% block branding %}{% endblock %}
        </div>
        {% block usertools %}
        {% if has_permission %}
        <div id="user-tools">
            {% block welcome-msg %}
                {% trans 'Welcome,' %}
                <strong>{% firstof user.get_short_name user.get_username %}</strong>.
            {% endblock %}
            {% block userlinks %}
                {% if site_url %}
                    <a href="{{ site_url }}">{% trans 'View site' %}</a> /
                {% endif %}
                {% if user.is_active and user.is_staff %}
                    {% url 'django-admindocs-docroot' as docsroot %}
                    {% if docsroot %}
                        <a href="{{ docsroot }}">{% trans 'Documentation' %}</a> /
                    {% endif %}
                {% endif %}
                {% if user.has_usable_password %}
                <a href="{% url 'admin:password_change' %}">{% trans 'Change password' %}</a> /
                {% endif %}
                <a href="{% url 'admin:logout' %}">{% trans 'Log out' %}</a>
            {% endblock %}
        </div>
        {% endif %}
        {% endblock %}
        {% block nav-global %}{% endblock %}
    </div>
    <!-- END Header -->
    {% block breadcrumbs %}
    <div class="breadcrumbs">
    <a href="{% url 'admin:index' %}">{% trans 'Home' %}</a>
    {% if title %} &rsaquo; {{ title }}{% endif %}
    </div>
    {% endblock %}
    {% endif %}

    {% block messages %}
        {% if messages %}
        <ul class="messagelist">{% for message in messages %}
          <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message|capfirst }}</li>
        {% endfor %}</ul>
        {% endif %}
    {% endblock messages %}

    <!-- Content -->
    <div id="content" class="{% block coltype %}colM{% endblock %}">
        {% block pretitle %}{% endblock %}
        {% block content_title %}{% if title %}<h1>{{ title }}</h1>{% endif %}{% endblock %}
        {% block content %}
        {% block object-tools %}{% endblock %}
        {{ content }}
        {% endblock %}
        {% block sidebar %}{% endblock %}
        <br class="clear">
    </div>
    <!-- END Content -->

    {% block footer %}<div id="footer"></div>{% endblock %}
</div>
<!-- END Container -->

</body>
</html>

```
## 新建 templates/registration/login.html
```
{% extends "base.html" %}

{% block content %}

{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

{% if next %}
    {% if user.is_authenticated %}
    <p>Your account doesn't have access to this page. To proceed,
    please login with an account that has access.</p>
    {% else %}
    <p>Please login to see this page.</p>
    {% endif %}
{% endif %}

```
## 运行django
```
python manage.py runserver 
```
## 相关域名
- 登陆域名：http://localhost:8000/o/applications/
- 认证URL：http://localhost:8000/o/authorize
- 获取TOKEN URL：http://127.0.0.1:8000/o/token/


### 参考文章
- [Oauth2.0基于Django的搭建使用（1）](https://www.jianshu.com/p/ba7eb3163794)
- [Oauth2.0基于Django的搭建使用（2）](https://www.jianshu.com/p/b7ec28b05c72)
- [Test your OAuth2 provider, I'll be your consumer](http://django-oauth-toolkit.herokuapp.com/consumer/)
- (http://django-oauth-toolkit.herokuapp.com/consumer/client/)


## Install Django and  django-oauth-toolkit django-cors-middleware  Django REST framework into the virtual environment
pip install django django-oauth-toolkit django-cors-middleware djangorestframework


#Set up a new project with a single application
django-admin startproject Django_oauth_project
cd Django_oauth_project
django-admin startapp Django_oauth_app


python manage.py migrate

#create superuser for django
python manage.py createsuperuser --email admin@example.com --username admin


# run django 
python manage.py runserver 
