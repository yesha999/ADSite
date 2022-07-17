from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
]
users_router = SimpleRouter()

users_router.register("users", UserViewSet)

urlpatterns += users_router.urls
