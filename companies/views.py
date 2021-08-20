from rest_framework import viewsets
from rest_framework import permissions

from companies.serializers import CompanySerializer
from .models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    # api endpt allows companies to viewed || edited
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
