from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def Name(request):
    mymember = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember1 = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember1':mymember1,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    
    return HttpResponse(template.render())

def table(request):
    mymember2 = Member.objects.all()
    template = loader.get_template('table.html')
    context = {
        'mymember2':mymember2,
    }
    return HttpResponse(template.render(context, request))
