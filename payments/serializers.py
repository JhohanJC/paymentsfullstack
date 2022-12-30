from rest_framework import serializers
from .models import Payments, Services, Payment_users, Expired_payments
from users.models import User
class PaymentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Payments 
        fields = '__all__'
        read_only_fields = '__all__',
        # read_only_fields = ('date_payment',)
# add's
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Services
        fields= '__all__'
        # exclude=['url']
        # read_only_fields = '__all__',
class PaymentUserSerializer(serializers.ModelSerializer):
    # url=serializers.URLField()
    class Meta:
        model = Payment_users   
        fields= '__all__'
        # '__all__'
        # read_only_fields = '__all__',
class ExpiredSerializer(serializers.ModelSerializer):
    class Meta:
        model= Expired_payments
        fields= '__all__'
        # read_only_fields = '__all__',
# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields= ["email", "username"]
        # read_only_fields = 'email','username',
        # fields = ["email", "username"]