from django import forms


from .models import Names_app

class Names_appForm(forms.ModelForm):
    class Meta:
        model = Names_app
        fields = ['name']