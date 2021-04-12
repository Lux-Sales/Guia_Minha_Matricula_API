from django.contrib import admin
from django.urls import path
from rest_framework import routers
from users.views import LogOutViewSet, RegisterUserViewSet, LoginViewSet
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createuser/', RegisterUserViewSet.as_view()),
    path('login/', LoginViewSet.as_view()),
    path('logout/', LogOutViewSet.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
