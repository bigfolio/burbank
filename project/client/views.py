from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model
from members.models import *
from content.models import *
from django.template import RequestContext
import stripe

@csrf_exempt
def index(request):
  pages = Page.objects.all()
  if request.method == 'POST':

    paying = str(request.POST['email'])
    usercreated = MyCustomEmailUser.objects.create_user(paying, 'A7S80D8A92455712SD#a9vk2100kasd7282ahjakh&*&@$^v')
    user = authenticate(username=paying, password='A7S80D8A92455712SD#a9vk2100kasd7282ahjakh&*&@$^v')
    login(request,user)
    return render_response(request,'index1.html')
  return render_response(request,'index.html')



@csrf_exempt
def pay(request):
  if request.method == 'POST':
    token = request.POST['stripeToken']
    #user = User.objects.get(id=request.user.id)
    user = get_user_model().objects.get(id=request.user.id)
    charge(token,user)
    return render_response(request,'thanks.html')
  return render_response(request,'pay.html')
@login_required
def forbidden(request):
  try:
    c = Content.objects.get(front_page = True)
  except:
    c = {}
  return render_response(request,'forbidden.html',{'c':c})




def charge(token,user):
  # Set your secret key: remember to change this to your live secret key in production
  # See your keys here https://manage.stripe.com/account
  stripe.api_key = "sk_test_TMlOC9anA6ITtOKACGQHHTaJ"

  # Get the credit card details submitted by the form

  # Create the charge on Stripe's servers - this will charge the user's card
  try:
    charge = stripe.Charge.create(
      amount=2000, # amount in cents, again
      currency="usd",
      card=token,
      description="payinguser@example.com"
      )
    user.paid = True
    user.save()
    print 'success'
  except stripe.CardError, e:
      # The card has been declined
      print 'no charge'

def render_response(req, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(req)
  return render_to_response(*args, **kwargs)
