from django.shortcuts import get_object_or_404, render
from .models import Project
def home(request):
    projects = Project.objects.order_by('id')[:3]
    return render(request, 'portfolio/home.html', {'projects':projects})

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/all_projects.html', {'projects':projects})

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/detail.html', {'project':project})
