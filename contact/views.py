from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from home.views import index

# Create your views here.


def contact(request):
    """ Use the contact form """
    user = request.user
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thanks {user}, your message has been submitted and will be responded to as soon as possible')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
