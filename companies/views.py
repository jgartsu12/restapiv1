# from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.AllowAny,)

class CompanyDetailView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class =  CompanySerializer
    permission_classes = (permissions.AllowAny, )

class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class =  CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )

class CompanyUpdateView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class =  CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )

class CompanyDeleteView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )
