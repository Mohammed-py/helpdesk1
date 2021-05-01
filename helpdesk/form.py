from django import forms
from .models import Sub_dis, City,  Ma_dis




class MajorForm(forms.ModelForm):
    class Meta:
        model = Ma_dis
        fields = ('first_name', 'last_name', 'region',)

    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)




     ############################################################################
class sub_disForm(forms.ModelForm):
    class Meta:
        model = Sub_dis
        fields = ('first_name', 'last_name', 'Ma_dis', 'city')
'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        '''
     ############################################################################

        