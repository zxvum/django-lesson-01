from django.shortcuts import render


def main(request):
    return render(request, 'index.html')


# auth
def register(request):
    return render(request, 'register.html')
