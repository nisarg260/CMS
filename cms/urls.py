from django.urls import path
from cms import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/<int:id>', views.data, name="data"),
    path('pay/<int:b_id>', views.pay, name='pay'),
    path("paid", views.paid, name='paid'),
    path("remaining", views.remaining, name='remaining'),
    path('add', views.add, name="add"),
    path('reset/<int:r_id>', views.reset, name="reset")
]