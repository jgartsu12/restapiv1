from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from projects.serializers import ProjectSerializer
from projects.models import Project

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny,)

class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class =  ProjectSerializer
    permission_classes = (permissions.AllowAny, )

class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class =  ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, )

class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class =  ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, )

class ProjectDeleteView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, )
