from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include( router.urls) ),
    path('api/auth',include( 'rest_framework.urls', namespace='rest_framework'))
]
