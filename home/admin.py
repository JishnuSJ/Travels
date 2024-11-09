from django.contrib import admin
from .models import Places,Doctors,Booking
# Register your models here.

admin.site.register(Places)
admin.site.register(Doctors)
class Bookingadmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')     #t display admin booked on booked date
admin.site.register(Booking,Bookingadmin)