from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

#article_list, article_details, ArticleList, ArticleDetails


router = routers.DefaultRouter()
router.register('register', UserViewSet)
router.register('patients', views.PatientView)


urlpatterns = [
path('', include(router.urls)),
]

