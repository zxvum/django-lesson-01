from django.urls import path
from .views import main, register

urlpatterns = [
    path('', main),
    # auth
    path('register/', register)
]
