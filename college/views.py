from college.serializers import SubjectSerializer, TeacherSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from college.models import Subject, Teacher, Comment
from rest_framework import viewsets
from rest_framework.response import Response

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

    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        all_teachers = Teacher.objects.all()
        all_subjects = Subject.objects.all()
        all_comments = []
        index = 0
        for comment in queryset.values():
            teacher_id = serializer.data[index]['teacher']
            subject_id = serializer.data[index]['subject']
            teacher = all_teachers.filter(id=teacher_id)
            subject = all_subjects.filter(id=subject_id)
            all_comments.append({'comment':comment['comment'], 'teacher':{'id':teacher_id, 'name':teacher.values()[0]['name']},
             'subject':{'id':subject_id, 'name':subject.values()[0]['name']}, 'user':comment['user_id'] })
            index+= 1 

        return Response(all_comments)