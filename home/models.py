from django.db import models         
                                                                             #ctrl c to stop server make migration(python manage.py makemigrations) ,(python manage.py migrate)this is important step to add create table  

# Create your models here.
class Places(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()  
    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Places,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doc_name + '-'+'('+self.doc_spec+ ')'                       #vie doct obj to booking table show as string


class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)       #use forgin key to call that table on delect use to delect any contion from that table same time delect this table
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)                        #show booked date not insert thorugh booking page automattic set
                                                                    #then goto admin.py