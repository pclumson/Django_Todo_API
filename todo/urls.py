from django.urls import include, path
from rest_framework.routers import DefaultRouter

from todo.views import *

router = DefaultRouter()
router.register(r'todos', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

]
