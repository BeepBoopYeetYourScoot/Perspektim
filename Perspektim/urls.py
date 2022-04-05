from django.urls import path
from upload.views import upload_file

urlpatterns = [
    path('protect/', upload_file),
]
