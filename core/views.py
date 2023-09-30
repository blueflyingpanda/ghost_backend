import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import permissions, viewsets, generics

from core.models import Student
from core.serializers import UserSerializer, StudentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def ping(request):
    with open('assistant_bot/data/data.json') as fr:
        data = json.load(fr)
        data.pop('teacher')
    return HttpResponse(json.dumps(data))


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def upd(request):
    with open('assistant_bot/data/data.json') as fr:
        data = json.load(fr)
        data.pop('teacher')

    updated = []

    for student_id, info in data['students'].items():
        student, is_new = Student.objects.get_or_create(
            tg_id=student_id,
            name=info['name'],
            points=info['points'],
            attendance=info['attendance']
        )

        if not is_new:
            updated.append(student)

    Student.objects.bulk_update(updated, ('name', 'points', 'attendance'))

    return HttpResponse('Bot data synced with database.')
