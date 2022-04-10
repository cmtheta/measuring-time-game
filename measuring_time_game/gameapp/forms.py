from django import forms

from gameapp.models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('record', 'target_time')