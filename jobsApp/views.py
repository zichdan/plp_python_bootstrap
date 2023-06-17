from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Job
from .forms import JobForm, ApplyForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from django.core.paginator import Paginator                 


# Create your views here.

def job_list(request):
    jobs = Job.objects.all()
   
    # Filters
    myfilter = JobFilter(request.GET, queryset=jobs)
    job_list = myfilter.qs # qs == queryset
   
    # Pagination
    paginator = Paginator(job_list, 5) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    context = {
        'jobs': page_obj,
        'myfilter' : myfilter
    }                       # templates name
    return render(request, 'joblist.html', context)