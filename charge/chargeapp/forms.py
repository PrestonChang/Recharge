from django import forms
from .models import UserProfile, ChargingStation

class CreateUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(),label='Password', max_length=30)

AVAILABLE_COLOURS = (
    ('BLK', 'black'),
    ('BLU', 'blue'),
    ('GRY', 'grey'),
    ('RED', 'red'),
    ('GRN', 'green'),
)

class ChangeUserProfileForm(forms.Form):
    sidebar_colour = forms.CharField(label = 'Sidebar Colour', max_length = 3, widget = forms.RadioSelect(choices=AVAILABLE_COLOURS))
    admin_data_only = forms.BooleanField(label = 'Show Admin Data Only?', required=False, initial=False)
 
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(),label='Password', max_length=30)

class UploadForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='please select a csv file for upload'
    )

class StationForm(forms.Form):
    station_identification = forms.ModelChoiceField(queryset=ChargingStation.objects.all())

class NewChargingStationForm(forms.Form):
    lat = forms.DecimalField(min_value=49.201301, max_value=49.361247, label='Latitude', max_digits=20, decimal_places=15)
    lon = forms.DecimalField(min_value=-123.274155, max_value=-123.023314, label='Longitude', max_digits=20, decimal_places=15)
    operator = forms.CharField(label='Lot Operator', max_length=50)
    address = forms.CharField(label='Address', max_length=50)

class UseChargingStationForm(forms.Form):
    station_id = forms.CharField(label='ID', max_length=3)
    time_used = forms.IntegerField(label='Hours', min_value=0)
