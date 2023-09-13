from django.db.models import Q
from .models import project, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProject(request, projects, results):

    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex + 1)

    return custom_range, projects


def searchProjects(request):
    search = ""

    if request.GET.get('text'):
        search = request.GET.get('text')

    tags = Tag.objects.filter(name__icontains=search)

    projects = project.objects.distinct().filter(
        Q(title__icontains=search) |
        Q(description__icontains=search) |
        Q(owner__name__icontains=search) |
        Q(tags__in=tags)
    )

    return projects, search