from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import project
from .forms import projectForm


def projects(request):
    projects = project.objects.all()
    context = {'list': projects}
    return render(request, 'projects/projects.html', context)

def projct(request, pk):
    prjobj = project.objects.get(id=pk)
    # tags = prjobj.tags.all()
    # print('prjobj:', prjobj)
    return render(request, 'projects/single-projects.html', {'obj': prjobj})


def createProject(request):
    form = projectForm()

    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        # print(request.POST)
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    projects = project.objects.get(id=pk)
    form = projectForm(instance=projects)

    if request.method == 'POST':
        form = projectForm(request.POST,instance=projects)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    projects = project.objects.get(id=pk)

    if request.method == 'POST':
        projects.delete()
        return redirect('projects')
    context = {'object':projects}
    return render(request, 'projects/deleteTemplate.html', context)

# Create your views here.
