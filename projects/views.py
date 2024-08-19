from django.shortcuts import render, get_object_or_404
from .models import Project, Measurement
# Create your views here.

def index(request):
    projects_list = Project.objects.all()
    context = {"projects_list":projects_list}
    return render(request, "projects/index.html", context)

def details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    m = project.measurement_set.all()
    return render(request, "projects/details.html", {"measurement_list":m})

