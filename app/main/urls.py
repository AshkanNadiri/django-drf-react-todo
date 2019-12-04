from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views as todo_views

router = routers.DefaultRouter()
router.register(r'todos', todo_views.TodoViewSet, 'todos')
router.register(r'users', todo_views.UserViewSet)
router.register(r'groups', todo_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



















# from rest_framework import routers
# from django.contrib import admin
# from django.urls import path, include
# from todo import views as todo_views


# router = routers.DefaultRouter()
# router.register(r'users',todo_views.UserViewSet)
# router.register(r'group',todo_views.GroupViewSet)
# router.register(r'todos', todo_views.TodoViewSet, 'todo')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include(router.urls) ),
#     # path('api/',include(router.urls) ),
#     path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework'))# . Check this in case it breaks
# ]

