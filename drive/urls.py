from django.urls import path
from .views import *

urlpatterns = [
    path('home/', FileUploadView.as_view(), name='home'),
    path('delete/', DeleteFilesView.as_view(), name='delete'),
    path('search-files/', search_files, name='search_files'),
    path('file/<int:file>/', SingleFileView.as_view(), name='file')
]
