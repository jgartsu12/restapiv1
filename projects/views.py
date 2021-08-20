from rest_framework import viewsets
from rest_framework import permissions

from Project.serializers import ProjectSerializer
from .models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    # api endpt allows companies to viewed || edited
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]