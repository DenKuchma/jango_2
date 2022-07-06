from django.http import HttpResponse

def main(request):
    return HttpResponse("Main!")


def main1(request):
    return HttpResponse("Main1!")


def main2(request):
    return HttpResponse("Main2!")


def main3(request):
    return HttpResponse("Main3!")


def main4(request, article_number):
    return HttpResponse(f"Main 4:  #{article_number}.")


def main5(request, article_number):
    return HttpResponse(f"Main 5:  #{article_number}.")


def main6(request, article_number, slug_text):
    return HttpResponse(f"Main 6:  #{article_number} and #{slug_text}.")


def main7(request, user_number):
    return HttpResponse(f"Main 7:  #{user_number}.")


def main8(request, regular):
    return HttpResponse(f"Main 8(regular): {regular}")


def main9(request, regular2):
    return HttpResponse(f"Main 9 number(regular): {regular2}")
