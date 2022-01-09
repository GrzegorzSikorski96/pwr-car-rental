from django.shortcuts import render


def dashboard(request):
    template = 'dashboard.html'

    return render(request, template)
