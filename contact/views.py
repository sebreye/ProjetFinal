from django.shortcuts import render, redirect
from .models import ContactUs, AboutUs

# Create your views here.
def Contact_page(request):
    infos = AboutUs.objects.all()
    return render(request, 'projetfinal/contact/contact.html', {'infos': infos})
    
def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('contact')
    else:
        form = ContactUsForm()

    return render(request, 'projetfinal/contact/contact.html', {'form': form})