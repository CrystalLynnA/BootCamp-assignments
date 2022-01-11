from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process_checkout),
    path('checkout/<int:order_id>', views.display_checkout),
]
