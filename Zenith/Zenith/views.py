from django.shortcuts import render, redirect
from contact.models import Contact


def home_view(request):
    return render(request, 'home.html')

def thank_you_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        org = request.POST.get('org')
        number = request.POST.get('number')

        Contact.objects.create(name=name, email=email, org=org, number=number)

        return redirect('thank_you_page')

    return render(request, 'thanks.html')