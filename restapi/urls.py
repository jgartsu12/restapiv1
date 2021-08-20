from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from blogs.views import (BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView)
from companies.views import (CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView)
from projects.views import (ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # companies urls
    path('company/', CompanyListView.as_view()),
    path('company/create/', CompanyCreateView.as_view()),
    path('company/<pk>', CompanyDetailView.as_view()),
    path('company/<pk>/update/', CompanyUpdateView.as_view()),
    path('company/<pk>/delete/', CompanyDeleteView.as_view()),
    # blogs urls
    path('blog/', BlogListView.as_view()),
    path('blog/create/', BlogCreateView.as_view()),
    path('blog/<pk>', BlogDetailView.as_view()),
    path('blog/<pk>/update/', BlogUpdateView.as_view()),
    path('blog/<pk>/delete/', BlogDeleteView.as_view()),
    # projects urls
    path('project/', ProjectListView.as_view()),
    path('project/create/', ProjectCreateView.as_view()),
    path('project/<pk>', ProjectDetailView.as_view()),
    path('project/<pk>/update/', ProjectUpdateView.as_view()),
    path('project/<pk>/delete/', ProjectDeleteView.as_view()),
]
