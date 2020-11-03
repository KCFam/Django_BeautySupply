from django.shortcuts import render


def login(request):
    # all_employees = serializers.serialize("json",Customer.objects.all())
    return render(request, 'login.html', {})
