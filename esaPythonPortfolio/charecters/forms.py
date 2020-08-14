from django.forms import ModelForm
from .models import Charecter, Team


class CharecterForm(ModelForm):
    class Meta:
        model = Charecter
        fields = '__all__'


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
