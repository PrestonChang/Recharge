from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import ChargingStation, Upload, UserProfile
from .forms import CreateUserForm, ChangeUserProfileForm, LoginForm, UploadForm, NewChargingStationForm, UseChargingStationForm

import datetime 

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

def logout_view(request):
    logout(request)
    form = LoginForm()
    return render(request, 'chargeapp/login.html', {'form': form})

def use_charging_station(request):
    if (request.method=='POST'):
        form = UseChargingStationForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            station = ChargingStation.objects.get(pk=form['station_id'])
            if station.inUse() != True:
                station.next_available = station.next_available + datetime.timedelta(hours=form['time_used'])
                station.save()
            else:
                messages.warning(request, 'Charging station already in use')  
    else:
        form = UseChargingStationForm()

    return render(request, 'chargeapp/use-charging-station.html', {'form': form})
