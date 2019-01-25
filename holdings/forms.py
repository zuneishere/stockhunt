from django.forms import ModelForm
from django import forms
from .models import Holdingmutual
from products.models import Product



class MutualForm(forms.ModelForm):    
    productid = forms.ModelChoiceField(queryset=Product.objects.all())
    notes=forms.CharField(
        required=False,
        widget=forms.Textarea(
                attrs={
                    "class":"my-text-class",
                    "rows":20,
                    "cols":120,
                    "id": "my-id-text"
                }
            )
        )
    class Meta:
         model=Holdingmutual
         #fields='__all__'
         exclude=['userid']
         widgets = {'start_date': forms.DateInput(attrs={'class': 'datepicker' }),
         'sip_date': forms.DateInput(attrs={'class': 'datepicker' })
         }
         
    def __init__(self, *args, **kwargs):
        super(MutualForm, self).__init__(*args, **kwargs)
        self.fields['no_shares'].label = "No of Shares"
        self.fields['productid'].label = "Mutual Fund"


         