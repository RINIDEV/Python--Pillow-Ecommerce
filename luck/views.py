from django.shortcuts import render, redirect
from .models import User, Product
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def page(request):
    return render(request, 'page.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if the user already exists
        if not User.objects.filter(email=email).exists():
            
            # Create new user with hashed password
            hashed_password = make_password(password)
            User.objects.create(email=email, password=hashed_password)
            return redirect('login')  # Redirect to login page
        else:
            return render(request, 'signup.html', {'error': 'User already exists'})
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                products = Product.objects.all()
                return render(request, 'dash.html', {"products": products})
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist'})
    
    return render(request, 'login.html')


def dash(request):
    return render(request,'dash.html')