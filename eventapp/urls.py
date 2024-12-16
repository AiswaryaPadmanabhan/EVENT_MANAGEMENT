from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('contact/submit/', views.contact_submission, name='contact_submission'),
    path('signup/', views.signup_view, name='signup'),  # Signup page URL
    path('login/', views.login_view, name='login'),
    path('thankyou/', views.thankyou, name='thankyou'),  # URL for the Thank You page
    path("booking_thankyou/", views.booking_thank_you, name="booking_thankyou"),
    path('booking/', views.booking_form, name='booking_form'),
    path('booking/submit/', views.booking_form, name='booking_form'),  # Path for the form submission
    path('booking/thank-you/', views.booking_thank_you, name='thankyou_booking'),  # Thank you page
    ]
