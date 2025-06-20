from django.shortcuts import render
from project_app.models import Project
from contactus_app.models import Footer

def home(request):

    projects = Project.objects.all()
    footer = Footer.objects.all().last()

    return render(request, 'index.html', context={'projects': projects , 'footer': footer})