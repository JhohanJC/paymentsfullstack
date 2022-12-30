from rest_framework import viewsets, permissions, status, generics, filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView, status
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payments, Services, Payment_users, Expired_payments
from users.models import User
from .serializers import (PaymentSerializer, ServiceSerializer,
 PaymentUserSerializer, ExpiredSerializer)
from .pagination import StandardResultsSetPagination
class PaymentSet(viewsets.ModelViewSet):
    queryset = Payments.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]
    # permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ('Payment_date','Expiration_date')
    # filterset_fields = ('usuario__id', 'fecha_pago', 'servicio')
    # search_fields = ['user_id', 'date_payment', 'service']
    # throttle_classes = 'payments'
#service#
class ServiceView(viewsets.ModelViewSet):
    queryset=Services.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
#payment#
class PaymentUserView(viewsets.ModelViewSet):
    queryset=Payment_users.objects.all()  
    serializer_class = PaymentUserSerializer  
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    # permission_classes = [UserPaymentPermission]
    # # filter_backends = [filters.OrderingFilter]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ('Payment_date','Expiration_date')
#------------------- expired--------------------------------#
class ExpiredPaymentView(viewsets.ModelViewSet):
    queryset=Expired_payments.objects.all()
    serializer_class = ExpiredSerializer
    pagination_class=StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]
    # permission_classes=[UserExpiredPermission]
    # http_method_names = ['get','post']
#_________________________ users ______________________________#
# class UsersView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class = UsersSerializer
#     pagination_class=StandardResultsSetPagination
#     permission_classes = [permissions.AllowAny]