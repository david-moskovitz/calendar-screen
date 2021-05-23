from django import forms
from luach.models import *

class MyDateForm(forms.ModelForm):
    class Meta:
        model = MyDate
        fields = '__all__'

        widgets = {
            'english_date':forms.DateInput({'type':'date'}),
            'sof_zman_1':forms.TimeInput({'type':'time'}),
            'sof_zman_2':forms.TimeInput({'type':'time'}),
            'sof_zman_tefila':forms.TimeInput({'type':'time'}),
        }




class DayImageForm(forms.ModelForm):

    keep_every_year = forms.BooleanField(required=False)
    keep_till = forms.IntegerField()

    class Meta:
        model = DayImage
        fields = ('images',)



class MazelTovForm(forms.ModelForm):

    keep_till = forms.IntegerField()

    class Meta:
        model = MazelTov
        fields = ('mazel_tov',)
        widgets = {'mazel_tov':forms.Textarea(attrs={'class':'form-control'})}

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {'message':forms.Textarea(attrs={'class':'form-control'})}

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = '__all__'
