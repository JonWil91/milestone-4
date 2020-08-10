from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact(request):
    """ Use the contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent succesfully!')
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    else:
        form = ContactForm()
        
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
