# forms.py

from django import forms
from .models import Artist

class ArtistRegistrationForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"
        # Add more fields from the Artist model as needed

# forms.py

from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"
        # Add more fields from the Artist model as needed
