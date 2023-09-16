import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import permissions, viewsets

from ghost_backend.core.serializers import UserSerializer


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
    return HttpResponse(data)
