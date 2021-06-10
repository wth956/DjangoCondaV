"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings           # add static files
from django.conf.urls.static import static # addstatic files
from engine.views import (base, high_rate, top_rate, movie_also_like,
    movie_also_dislike, movie_rcmd_exist_user, movie_rcmd_to_user, movie_detail, add_rating)
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base),
    url(r'^high_rate$', high_rate, name = 'high_rate'), #平均最高分
    url(r'^top_rate$', top_rate, name = 'top_rate'), #最多人評分
    url(r'^movie_also_like$', movie_also_like), #同時也喜歡
    url(r'^movie_also_dislike$', movie_also_dislike), #同時也不喜歡
    url(r'^movie_rcmd_exist_user$', movie_rcmd_exist_user, name ='movie_rcmd_exist_user'), #推薦給現有使用者
    url(r'^movie_rcmd_to_user$', movie_rcmd_to_user, name = 'movie_rcmd_to_user'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', movie_detail, name='movie_detail'),
    url(r'^movie/(?P<movie_id>[0-9]+)/add_rating/$', add_rating, name='add_rating'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

