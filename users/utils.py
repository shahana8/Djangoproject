from django.db.models import Q
from .models import Skill, Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfiles(request, profile, results):

    page = request.GET.get('page')
    paginator = Paginator(profile, results)

    try:
        profile = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profile = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profile = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex + 1)

    return custom_range, profile

def searchProfiles(request):
    search = ""

    if request.GET.get('text'):
        search = request.GET.get('text')

    print("search:", search)
    skills = Skill.objects.filter(name__iexact=search)
    profile = Profile.objects.distinct().filter(Q(name__icontains=search) |
                                                Q(short_intro__icontains=search) |
                                                Q(skill__in=skills))

    return profile, search