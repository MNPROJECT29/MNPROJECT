
from django import forms

from .models import unislot


class slotform(forms.ModelForm):
    class Meta:
          model= unislot
          fields=['name','desc','image','location']

