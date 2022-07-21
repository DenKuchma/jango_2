from random import *
import string
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    random_int = randint(10000, 9999999999)
    random_str = get_random_string(length=10, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return render(request, 'main.html', {'random_int': random_int, 'random_str': random_str})


def main1(request):
    return render(request, 'main1.html')


def main2(request):
    return render(request, 'main2.html')


def main3(request):
    return render(request, 'main3.html')


def main4(request, article_number):
    return render(request, 'main4.html', {'article_number': article_number})


def main5(request, article_number):
    return render(request, 'main5.html', {'article_number': article_number})


def main6(request, article_number, slug_text):
    return render(request, 'main6.html', {'article_number': article_number, 'slug_text': slug_text})


def main7(request, user_number):
    return render(request, 'main7.html', {'user_number': user_number})


def main8(request, regular):
    return render(request, 'main8.html', {'regular': regular})


def main9(request, regular2):
    return render(request, 'main9.html', {'regular2': regular2})
