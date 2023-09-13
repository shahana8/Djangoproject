from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import project, Tag
from .forms import projectForm
from .utils import searchProjects, paginateProject


def projects(request):

    projects, search = searchProjects(request)
    custom_range, projects = paginateProject(request, projects, 6)


    context = {'list': projects, 'search':search, 'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)

def projct(request, pk):
    prjobj = project.objects.get(id=pk)
    # tags = prjobj.tags.all()
    # print('prjobj:', prjobj)
    return render(request, 'projects/single-projects.html', {'obj': prjobj})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = projectForm()


    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

        # print(request.POST)
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    projects = profile.project_set.get(id=pk)
    form = projectForm(instance=projects)

    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    projects = profile.project_set.get(id=pk)

    if request.method == 'POST':
        projects.delete()
        return redirect('account')
    context = {'object':projects}
    return render(request, 'deleteTemplate.html', context)



# Create your views here.
