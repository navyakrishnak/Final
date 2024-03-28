from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
import time

# Create your views here.
def register(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exists")
                    return redirect('register:register')
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                    user.save()
                    messages.success(request, 'Successfully registered')
                    time.sleep(2)
                    return redirect('register:success', username=username)
            else:
                messages.info(request, "Passwords do not match")
    except:
        messages.error(request, "An error occurred")
    return render(request, 'register.html')
def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
        
            user = auth.authenticate(username = username, password = password)
            request.session['username'] = user.username


            if user is not None:
                auth.login(request, user)
                
                messages.success(request,"login sucess")
                time.sleep(3)
                
                return redirect('/')
            else:
                messages.error(request, "login sucess")
                time.sleep(3)
                return redirect('register:login')
    except:
        messages.error(request, "Error occured")
    
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def editprofile(request):
    if request.method == 'POST':
        # Check if user is logged in
        if 'username' in request.session:
            username = request.session['username']  
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return HttpResponse("User does not exist")
   
            # Update first name
            if 'firstname' in request.POST:
                first_name = request.POST['firstname']
                user.first_name = first_name
                print("First Name:", first_name)
                
            # Update last name
            if 'lastname' in request.POST:
                last_name = request.POST['lastname']
                user.last_name = last_name
                print("Last Name:", last_name)
                
            # Update email
            if 'email' in request.POST:
                email = request.POST['email']
                user.email = email
                print("Email:", email)
        
            # Update username
            if 'username' in request.POST:
                new_username = request.POST['username']
                if User.objects.filter(username=new_username).exists():
                    messages.error(request, "Username already exists")
                else:
                    user.username = new_username
                    print("Username:", new_username)
            request.session['username'] = user.username

                
            user.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "You must be logged in to edit profile")
    
    return render(request, 'editprofile.html')


def success(request,username):
    user = username
    return render(request, 'sucessUserRegistration.html',{"username" : user})