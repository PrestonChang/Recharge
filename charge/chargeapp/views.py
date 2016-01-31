from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import ChargingStation, Upload, UserProfile

import datetime 

from .forms import CreateUserForm, ChangeUserProfileForm, LoginForm, UploadForm, NewChargingStationForm, StationForm, UseChargingStationForm
from charge.settings import SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET

from twitter import *
import os


def index(request):
    return render(request, "index.html")

def maps(request):
    charging_stations = ChargingStation.objects.all()
    if (request.user.is_authenticated() and request.user.userprofile.admin_data_only):
        charging_stations = ChargingStation.objects.all().filter(admin=True)
    context = {'charging_stations': charging_stations}
    return render(request, "chargeapp/maps.html", {'charging_stations' : charging_stations})

def list(request):
    charging_stations = ChargingStation.objects.all()
    if (request.user.is_authenticated() and request.user.userprofile.admin_data_only):
        charging_stations = ChargingStation.objects.all().filter(admin=True)
    context = {'charging_stations': charging_stations}
    return render(request, 'chargeapp/list.html', context)

def filterCOVList(request):
    charging_stations = ChargingStation.objects.filter(operator="City of Vancouver")
    if (request.user.is_authenticated() and request.user.userprofile.admin_data_only):
        charging_stations = ChargingStation.objects.all().filter(admin=True)
    context = {'charging_stations': charging_stations}
    return render(request, 'chargeapp/list.html', context)

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                newdoc = Upload(docfile = request.FILES['docfile'])
                newdoc.full_clean()
                newdoc.save()
                parsed_data = newdoc.parse()
                newdoc.import_parsed(parsed_data)

            except Exception as e:
                messages.error(request, 'Error: %s, when uploading.' % e)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('chargeapp.views.upload'))
    else:
        form = UploadForm() # A empty, unbound form

    # Upload documents for the list page
    documents = Upload.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        "chargeapp/upload.html",
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def create_user(request):
    if (request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            try:
                user = User.objects.create_user(username = form['username'], first_name = form['first_name'], 
                    last_name = form['last_name'], email = form['email'], password = form['password'])
                messages.success(request, 'Account Created! (placeholder)')
            except Exception as e:
                messages.error(request, 'Error: %s, when creating user.' % e)
            return HttpResponseRedirect(reverse('create_user'))
    else:
        form = CreateUserForm()
    return render(request, 'chargeapp/create-user.html', {'form': form})



def profile(request):
    if (request.user.is_authenticated()):
        if (request.method == 'POST'):
            form = ChangeUserProfileForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                try:
                    user_profile = User.objects.get(id = request.user.id).userprofile
                    user_profile.sidebar_colour =  form['sidebar_colour']
                    user_profile.admin_data_only = form['admin_data_only']
                    user_profile.save()
                    messages.success(request, 'Values Updated!')
                except Exception as e:
                    messages.error(request, 'Error: %s, when updating user preferences.' % e)  
                return HttpResponseRedirect(reverse('profile'))
        else:
            form = ChangeUserProfileForm()
        return render(request, 'chargeapp/user-profile.html', {'form': form, 'username': request.user.username, 
                'sidebar_colour': request.user.userprofile.get_sidebar_colour_display(), 'admin_data_only': request.user.userprofile.admin_data_only})
    else:
        form = LoginForm()
        return render(request, 'chargeapp/login.html', {'form': form})



def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, 'Login Success! (placeholder)')
                return HttpResponseRedirect('/chargeapp/profile/')
            else:
                messages.success(request, 'Valid login, however, account is not active! (placeholder)')
        else:
            messages.warning(request, 'Invalid login credentials')
    form = LoginForm()
    return render(request, 'chargeapp/login.html', {'form': form})


def new_charging_station(request):
    if (request.method=='POST'):
        form = NewChargingStationForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            try:
                new = ChargingStation(lat=form['lat'], lon=form['lon'], operator=form['operator'], address=form['address'])
                new.save()
                messages.success(request, 'New Charging Station Added!')
            except Exception as e:
                messages.error(request, 'Error: %s, when adding a new charging station.' % e)
            return HttpResponseRedirect(reverse('new_charging_station'))
    else:
        form = NewChargingStationForm()
    return render(request, 'chargeapp/new-charging-station.html', {'form': form})

def twitter(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response("chargeapp/twitter.html", context_instance=context)

def facebook(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response("chargeapp/facebook.html", context_instance=context)

def posttw(request):
    charging_stations = ChargingStation.objects.all()
    form = StationForm()
    if request.method == "POST":

        form = StationForm(request.POST)
        if form.is_valid:

            station = request.POST['station_identification']
            if station == "":
                HttpResponseRedirect(reverse('posttw'))
            else:
                try:
                    charstation = ChargingStation.objects.get(id=station)
                    address = charstation.address
                    MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
                    if not os.path.exists(MY_TWITTER_CREDS):
                        oauth_dance("My App Name", SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, MY_TWITTER_CREDS)
                    else:
                        oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

                    twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET))
                    status = "I just charged my car at station " + str(station) + " at " + address + "! Check out more at https://tranquil-beach-1921.herokuapp.com/chargeapp/"
                    twitter.statuses.update(status=status)
                    return render(request, 'chargeapp/sharetw.html', {'station': station, 'address': address})
                except Exception as e:
                    if "duplicate" in str(e):
                        messages.error(request, 'You\'ve already tweeted about station %s!' % station)
                    else:
                        messages.error(request, 'Unknown Error! Sorry, try again.')
                    HttpResponseRedirect(reverse('posttw'))
            #redirect to the url where you'll process the input
            #return HttpResponseRedirect('sharefb') # insert reverse or url
        else: print (form.errors)
    errors = form.errors or None # form not submitted or it has errors
    return render(request, 'chargeapp/posttw.html',{
      'form': form,
      'errors': errors,
      'charging_stations': charging_stations,
      })

def sharetw(request):
    return render(request, 'chargeapp/sharetw.html')

def postfb(request):
    charging_stations = ChargingStation.objects.all()
    form = StationForm()
    if request.method == "POST":

        form = StationForm(request.POST)
        if form.is_valid:
            station = request.POST['station_identification']
            return render(request, 'chargeapp/sharefb.html', {'station': station})
            #redirect to the url where you'll process the input
            #return HttpResponseRedirect('sharefb') # insert reverse or url
        else: print (form.errors)
    errors = form.errors or None # form not submitted or it has errors
    return render(request, 'chargeapp/postfb.html',{
      'form': form,
      'errors': errors,
      'charging_stations': charging_stations,
      })

def sharefb(request):
    return render(request, 'chargeapp/sharefb.html')

def delete(request):
    if (request.method == 'POST'):
        if request.POST.get('delete_cs'):
            ChargingStation.objects.all().delete()
            messages.success(request, 'Deleted All Charging Stations')
        elif request.POST.get('delete_upload'):
            Upload.objects.all().delete()
            messages.success(request, 'Deleted Uploads')
        elif request.POST.get('delete_admin'):
            ChargingStation.objects.filter(admin=True).delete()
            messages.success(request, 'Deleted Admin Stations')
        elif request.POST.get('delete_user'):
            ChargingStation.objects.filter(admin=False).delete()
            messages.success(request, 'Deleted User Stations')
    return render(request, 'chargeapp/delete.html')

def logoutuser(request):
    logout(request)
    form = LoginForm()
    messages.success(request, 'You have logged out successfully!')
    return render(request, 'chargeapp/login.html', {'form': form})

def use_charging_station(request):
    if (request.method=='POST'):
        form = UseChargingStationForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            try:
                station = ChargingStation.objects.get(pk=form['station_id'])
                if station.inUse() != True:
                    station.next_available = station.next_available + datetime.timedelta(hours=form['time_used'])
                    station.save()
                    messages.success(request, 'Charging station %s now in use for %s hours' % (form['station_id'], form['time_used']))
                else:
                    messages.warning(request, 'Charging station already in use')
            except Exception as e:
                if "query does not exist" in str(e):
                    messages.error(request, 'That charging station doesn\'t exist! Try again.')
                else:
                    messages.error(request, 'Unknown Error! Sorry, try again.')
    form = UseChargingStationForm()
    return render(request, 'chargeapp/use-charging-station.html', {'form': form})

def privacy(request):
    return render(request, "chargeapp/privacy.html")



