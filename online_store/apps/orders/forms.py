from django import forms
from .models import *

# class SubscriberForm(forms.ModelForm):

#     class Meta:
#         model = Subscriber
#         exclude = [""] # не писать fields = [... все поля] а перечислить что ничего не нужно исключать