from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet

router = routers.DefaultRouter() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('see/', UserViewSet.as_view())
]
