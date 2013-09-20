from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model
from members.models import *
from content.models import *
from django.template import RequestContext
@login_required
def chapter(request,chapter):
  c = Content.objects.get(chapter=int(chapter))
  return render_response(request,'chapter.html',{'c':c})
  #return render_to_response('chapter.html',{'c':c},context_instance=RequestContext(request))

def page(request,number):
  c = Page.objects.get(id=int(number))
  return render_response(request,'page.html',{'c':c})
