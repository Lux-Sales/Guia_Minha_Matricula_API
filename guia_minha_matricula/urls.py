from django.contrib import admin
from django.urls import path
from rest_framework import routers
from users.views import RegisterUserViewSet, LoginViewSet

router = routers.DefaultRouter() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createuser/', RegisterUserViewSet.as_view()),
    path('login/', LoginViewSet.as_view()),
]
