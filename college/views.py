from django.db.models import query
from college.serializers import SubjectSerializer, TeacherSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from college.models import Subject, Teacher, Comment
from rest_framework import viewsets

class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer