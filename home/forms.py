#to create forms enter details to db
from django import forms

from .models import Booking

class DateInput(forms.DateInput):              #date picker in view page
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'                    #then goto viwes.py

        widgets={
            'booking_date':DateInput(),          #widget use to call the class to date
        }
        labels={
            'p_name':"Name",
            'p_phone':"Phone",
            'p_email':"Email",
            'doc_name':"Select place",
            'booking_date':"Booking Date"
        }