from django.urls import path
from .views import index, show_contacts, show_vacancy, get_order
from .decorators import check_recaptcha
urlpatterns = [
    path('', index, name='index'),
    path('order', get_order, name='get_order' ),
    path('vacancy', show_vacancy, name='vacancy'),
    path('contacts', show_contacts, name='contacts'),

]