from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
# Payments
class Payments(models.Model):
    class Servicess(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Star +')
        PARAMOUNT = 'PM', _('Paramount +')
    service = models.CharField(
        max_length=2,
        choices=Servicess.choices,
        default=Servicess.NETFLIX,
    )
    date_payment = models.DateField(auto_now_add=True)
    amount = models.FloatField(default=0.0)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user')

class Services(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    description=models.TextField()
    logo=models.ImageField(upload_to='logo/')

class Payment_users(models.Model):
    id=models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name='users')
    service_id=models.ForeignKey(Services,on_delete=models.CASCADE,related_name='services')
    amount=models.FloatField(default=0.0)
    payment_date=models.DateField()
    expiration_date=models.DateField()

class Expired_payments(models.Model):
    id=models.AutoField(primary_key=True)
    payment_user_id=models.ForeignKey(Payment_users,on_delete=models.CASCADE,related_name='payment_users')
    penalty_fee_amount=models.FloatField()
