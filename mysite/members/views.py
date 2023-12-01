# from django.shortcuts import render
# # from django.http import HttpResponse
# from django.template import request
#
# def members(request):
#   template = loader.get_template('lab3.html')
#   return render(template_name="lab3.htm")

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def members(request):
    template = loader.get_template('members/lab3.htm')
    return HttpResponse(template.render())
