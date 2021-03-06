"""tinyintennesseeback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from tinyintennesseeapi.views import BuilderView, LocationView
from tinyintennesseeapi.views.auth import register_user, login_user
from tinyintennesseeapi.views.county_view import CountyView
from tinyintennesseeapi.views.law_view import LawView
from tinyintennesseeapi.views.location_category_view import LocationCategoryView
from tinyintennesseeapi.views.post_view import PostView
from tinyintennesseeapi.views.tag_view import TagView
from tinyintennesseeapi.views.user_view import UserView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'builders', BuilderView, 'builder')
router.register(r'locations', LocationView, 'location')
router.register(r'laws', LawView, 'law')
router.register(r'posts', PostView, 'post')
router.register(r'counties', CountyView, 'county')
router.register(r'locationCategories', LocationCategoryView, 'locationCategory')
router.register(r'users', UserView, 'user')
router.register(r'tags', TagView, 'tag')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    
]
