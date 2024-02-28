from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import caesar_cipher
# Create your views here.
def greetings(request):
    result={"message":"Welcome to the Ciphers API"}
    return JsonResponse(result)

def caesar_cipher_encode(request,plaintext,shift):
    parameters=dict(request.GET)
    cipher=caesar_cipher(plaintext,shift)
    return JsonResponse({"cipher":cipher})