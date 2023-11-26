
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Hotel
from .models import Register


def index_view(request):
  template = loader.get_template('template.html')
  hotels = Hotel.objects.all().values()
  context = {
    'hotel_ratings':hotels,
  }
  if request.POST:
    name = request.POST['name']
    rating = request.POST['rating']
    hotel = Hotel(name=name, rating=rating)
    try:
      hotel.save()
    except Exception as e:
      print (e)
  return HttpResponse(template.render(context, request))

def delete_view(request, id):
  hotel = Hotel.objects.get(id=id)
  hotel.delete()
  # The reverse function looks up the available urls.
  return HttpResponseRedirect(reverse('index'))


def update_view(request, id):
  # need to createa new view to obtain the data
  hotel = Hotel.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'hotel': hotel,
  }
  return HttpResponse(template.render(context, request))
  
def update(request, id):
  name = request.POST['name']
  rating = request.POST['rating']
  hotel = Hotel.objects.get(id=id)
  hotel.name = name
  hotel.rating = rating
  hotel.save()
  return HttpResponseRedirect(reverse('index'))

def reg_view(request):
  template = loader.get_template('register.html')
  registry = Register.objects.all().values()
  context = {
    'registry':registry,
  }
  if request.POST:
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    uid = request.POST['uid']
    register = Register(firstname=firstname, lastname=lastname, uid=uid)
    try:
      register.save()
    except Exception as e:
      print (e)
  return HttpResponse(template.render(context, request))