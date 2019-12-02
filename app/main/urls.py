from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from todo import views as drf_views


router = routers.DefaultRouter()
router.register(r'users',drf_views.UserViewSet)
router.register(r'group',drf_views.GroupViewSet)
router.register(r'todos', drf_views.TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls) ),
    path('api/',include(router.urls) ),
    # path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework')),# . Check this in case it breaks
]

