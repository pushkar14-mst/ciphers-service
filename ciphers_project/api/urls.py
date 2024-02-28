from django.urls import path
from .views import *

urlpatterns = [
    path('', greetings),
    path('caesar/<str:plaintext>/<int:shift>', caesar_cipher_encode)
]