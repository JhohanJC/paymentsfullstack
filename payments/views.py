from django.shortcuts import render
from .models import Payments, Services, Payment_users, Expired_payments
from users.models import User
# Create your views here.
def home(request):
    return render(request, "login.html")
def base(request):
    paymentsx=Payments.objects.all()
    servicesx=Services.objects.all()
    payment_usersx=Payment_users.objects.all()
    expired_paymentsx=Expired_payments.objects.all()
    return render(request, "base.html",{'paymentsx':paymentsx,'servicesx':servicesx,
    'payment_usersx':payment_usersx,'expired_paymentsx':expired_paymentsx})
def delete(request):
    return render(request, "delete.html")
def post(request):
    userx=User.objects.all()
    paymentsx=Payments.objects.all()
    servicesx=Services.objects.all()
    return render(request, "post.html",{'paymentsx':paymentsx,'userx':userx,'servicesx':servicesx})
def put(request):
    return render(request, "put.html")
