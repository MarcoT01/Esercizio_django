from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
from contact_me.forms import ContactForm


class ContactFormView(generic.FormView):
    template_name = "contact_me/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        return super().form_valid(form)
