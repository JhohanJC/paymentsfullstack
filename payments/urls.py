from .api import PaymentSet, ServiceView, PaymentUserView, ExpiredPaymentView
from rest_framework import routers 
from .views import home, base, delete, post, put
from django.urls import path
router = routers.DefaultRouter()
router.register(r'payments',PaymentSet, 'payments')
router.register(r'services',ServiceView, 'services')
router.register(r'payment_user',PaymentUserView, 'payment_user')
router.register(r'expired_payments',ExpiredPaymentView, 'expired_payments')
urlpatterns = [
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('delete/', delete, name='delete'),
    path('post/', post, name='post'),
    path('put/', put, name='put'),
]
urlpatterns += router.urls


