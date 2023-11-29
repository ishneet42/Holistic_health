from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('thank_you')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'contact/thank_you.html')
# Create your views here.
