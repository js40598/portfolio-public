from django.shortcuts import render, get_object_or_404, redirect

from contact.models import Message
from .models import Page, Skill
from projects.models import Project, Subpage
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def home(request):
    current_page = get_object_or_404(Page, title='Portfolio')
    pages = Page.objects.filter(navbar_display=True).order_by('id')

    counter = 0
    counter += len(current_page.description.split('<p'))
    counter += len(current_page.description.split('<li'))
    counter += len(current_page.description.split('<br'))
    if current_page.title == 'Contact':
        counter += 22
    rows = [i for i in range(1, counter)]
    
    context = {
        'pages': pages,
        'rows': rows,
        'current_page': current_page
    }
    return render(request, 'pages/home.html', context)


def page(request, slug):
    current_page = get_object_or_404(Page, slug=slug)
    pages = Page.objects.filter(navbar_display=True).order_by('id')

    if current_page.title == 'Skills':
        SKILL_LEVEL_CHOICES = [('OWNED', 'Owned'), ('FAMILIAR', 'Familiar'), ('FUTURE', 'Future')]
        skills = Skill.objects.all()
        current_page.description = current_page.description.split("LIST_BREAK_POINTER")
        new_current_page = ''
        for lvl in SKILL_LEVEL_CHOICES:
            new_current_page += current_page.description.pop(0)
            for skill in skills:
                if skill.level == lvl[0]:
                    new_current_page += skill.in_html
            new_current_page += '<br>'
        current_page.description = new_current_page


    projects = ''
    if slug == 'projects':
        projects = Project.objects.all()

    subpages = Subpage.objects.all().order_by('id')

    counter = 0
    counter += len(current_page.description.split('<p'))
    counter += len(current_page.description.split('<li'))
    counter += len(current_page.description.split('<br'))
    if current_page.title == 'Contact':
        counter += 22
    rows = [i for i in range(1, counter)]

    context = {
        'rows': rows,
        'pages': pages,
        'current_page': current_page,
        'projects': projects,
        'subpages': subpages,
        'values': request.POST
    }

    # if Contact form submitted
    if request.method == "POST":
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        text = request.POST['text']
        context['values'] = request.POST

        has_contacted = Message.objects.all().filter(text=text)
        if has_contacted:
            messages.error(request, 'This email already has been sent!')
            return render(request, 'pages/page.html', context)

        # including = 'Name: ' + name + '\nCompany: ' + company + '\nEmail: ' + email + '\n\n' + text

        # send_mail('Portfolio message',
        #           including,
        #           'emailaddress@sending.com',
        #           ['emailaddress@to.com'])

        message = Message(name=name,
                          company=company,
                          email=email,
                          text=text)
        message.save()

        messages.success(request, 'E-mail has been sent!')
        return render(request, 'pages/page.html', context)

    return render(request, 'pages/page.html', context)
