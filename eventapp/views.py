
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User  # For creating a new user (signup)
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def booking(request):
    return render(request, 'booking.html')
def events(request):
    events_data = [
        {
            'name': 'Wedding',
            'image': 'images/event1.png',
            'description': 'A beautiful wedding ceremony to remember for a lifetime.',
        },
        {
            'name': 'Corporate Events',
            'image': 'images/event2.jpg',
            'description': 'An elegant corporate event with keynotes and networking.',
        },
        {
            'name': 'Birthday Party',
            'image': 'images/event3.jpg',
            'description': 'A fun-filled birthday party with games and entertainment.',
        },
    ]
    return render(request, 'events.html', {'events': events_data})
def contact(request):
    return render(request, 'contact.html')
def signup_view(request):
    if request.method == 'POST':
        # Fetch data from the POST request
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        try:
            # Create a new user
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login page or homepage after successful signup
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('signup')  # Stay on signup page if error occurs

    return render(request, 'signup.html')
def login_view(request):
    if request.method == 'POST':
        # Get the username (email) and password from the form
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # If the user is found, log them in
            login(request, user)
            return redirect('index')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')  # Render the login page
def contact_submission(request):
    if request.method == 'POST':
        # Here you can handle the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Process form data, e.g., save to database, send an email, etc.
        
        return HttpResponse("Thank you for your message.")
    else:
        return HttpResponse("Invalid request", status=400)
def contact_view(request):
    # If it's a POST request, process the form
    if request.method == 'POST':
        # Here, you can add logic to save the form data or send an email.
        # After processing the form, redirect to the index (home) page
        return redirect('thankyou')  # Assuming 'index' is your homepage URL name

    # If GET request, just render the contact page with the form
    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Process data: save to database, send email, etc. (Optional)

        # Redirect to the Thank You page
        return redirect('thankyou')  # Name of the URL pattern for thank you page

    # Default GET: render the contact page
    return render(request, 'contact.html')

def thankyou(request, context={}):
    # Context will include specific details based on the type of request (contact us or booking)
    return render(request, 'thankyou.html', context)

def booking_form(request):
    if request.method == "POST":
        # Get form data
        event = request.POST.get("event")
        event_date = request.POST.get("event_date")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        
        try:
            # Send confirmation email
            send_mail(
                subject=f"Booking Confirmation for {event}",
                message=f"Dear {name},\n\n"
                        f"Thank you for booking your {event} with Lumiere Event Management on {event_date}.\n"
                        f"We will contact you soon at {phone}.\n\n"
                        f"Best regards,\nLumiere Event Management",
                from_email="lumiereeventmanagement@gmail.com",  # Replace with your actual email
                recipient_list=[email],
                fail_silently=False,
            )
            print(f"Email sent to {email}")
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except Exception as e:
            print(f"Email sending error: {e}")
            return HttpResponse("An error occurred while sending the email.")
        
        # Redirect to the thank-you page
        return redirect("thankyou_booking")

    return render(request, "booking.html")

def booking_thank_you(request):
    return render(request, "thankyou_booking.html")