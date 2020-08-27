from django.shortcuts import render, get_object_or_404

from pages.models import Page
from .models import Project, Subpage
from tasks.models import Task

# Create your views here.


def project(request):
    return render(request, 'projects/project_subpage.html')


def project_subpage(request, project_slug, subpage_slug):
    current_project = get_object_or_404(Project, slug=project_slug)
    current_subpage = get_object_or_404(Subpage, project=current_project, slug=subpage_slug)
    pages = Page.objects.filter(navbar_display=True).order_by('id')
    subpages = Subpage.objects.all().order_by('id')
    projects = Project.objects.all()

    if current_subpage.title == 'Tasks':
        IS_DONE_CHOICES = [('DONE', 'Done'), ('ONGOING', 'Ongoing'), ('FUTURE', 'Future')]
        tasks = Task.objects.filter(project=current_project).order_by('priority', 'id')
        current_subpage.description = current_subpage.description.split("LIST_BREAK_POINTER")
        new_current_subpage = ''
        for choice in IS_DONE_CHOICES:
            new_current_subpage += current_subpage.description.pop(0)
            for task in tasks:
                if task.is_done == choice[0]:
                    new_current_subpage += task.in_html
            new_current_subpage += '<br>'
        current_subpage.description = new_current_subpage
    elif current_subpage.title == 'Github':
        current_subpage.description = current_subpage.description.split("GITHUB_URL_HERE")
        current_subpage.description = current_project.github_url.join(current_subpage.description)

    counter = 1
    counter += len(current_subpage.description.split('<p'))
    counter += len(current_subpage.description.split('<li'))
    counter += len(current_subpage.description.split('<br'))
    rows = [i for i in range(1, counter)]

    context = {
        'rows': rows,
        'pages': pages,
        'current_project': current_project,
        'current_page': current_subpage,
        'current_subpage': current_subpage,
        'projects': projects,
        'subpages': subpages
    }
    return render(request, 'projects/project_subpage.html', context)

