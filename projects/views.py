from django.shortcuts import render
from django.http import HttpResponse
from .models import project

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    projects = project.objects.all()
    context = {'list': projects}
    return render(request, 'projects/projects.html', context)

def projct(request, pk):
    prjobj = project.objects.get(id=pk)
    # tags = prjobj.tags.all()
    # print('prjobj:', prjobj)
    return render(request, 'projects/single-projects.html', {'obj': prjobj})

# Create your views here.
