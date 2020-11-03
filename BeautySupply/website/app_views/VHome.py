from django.shortcuts import render
from django.core import serializers


def home(request):
    # all_employees = serializers.serialize("json",Customer.objects.all())
    return render(request, 'home.html', {})
