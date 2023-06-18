from django.urls import path
from . import views


app_name = "jobsApp"

urlpatterns = [
    path('', views.job_list, name='job_list'), # reverse("jobs:job_list")
    path('job-detail/<str:slug>', views.job_detail, name="job-detail"),
    
]
