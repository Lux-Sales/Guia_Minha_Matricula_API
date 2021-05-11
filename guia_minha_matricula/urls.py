from django.conf.urls import include
from django.contrib import admin
from django.urls import base, path
from rest_framework import routers
from users.views import RegisterUserViewSet, LoginViewSet
from college.views import CommentViewSet, SubjectViewSet, TeacherViewSet

router = routers.DefaultRouter() 

router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createuser/', RegisterUserViewSet.as_view()),
    path('login/', LoginViewSet.as_view()),
    path('', include(router.urls)),
]
