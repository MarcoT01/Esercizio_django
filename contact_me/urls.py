from django.urls import path

from contact_me import views

app_name = "contact_me"
urlpatterns = [
    path("", views.ContactFormView.as_view(), name="contact")
]
