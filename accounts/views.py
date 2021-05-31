from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User, auth 
#User allows us to use the user model already in the django framework
#auth is used for log in


def register(request): 
    #because the submit in the form of register.html will go back to this function,
    #the function must learn how to handle get and post requests...

    if request.method == 'POST': #handle a post request

        #first get the data from the user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        #then check if passwords match
        if password1 == password2:
            #then check if the username/email exists already in the database
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('accounts:register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('accounts:register')

            else:  #otherwise, create the new user
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'User Created')
                return redirect('accounts:login')

        else:
            messages.info(request,'Password Not Matching')
            return redirect('accounts:register')

    else:
        return render(request, 'accounts/register.html')  #send a get request

def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        to_go = request.POST['next_page'] #check if they were trying to get to another page
        user = auth.authenticate(username=username, password=password)
        
        if to_go == '':  #meaning there is no next query
            if user is not None: #if user is valid/authenticated
                auth.login(request,user) #log them in
                return redirect('travello:index') 
        else:
            if user is not None: 
                auth.login(request,user)
                return redirect(to_go)           
            else:
                messages.info(request,'Invalid Credentials')
                return redirect( reverse('accounts:login') + '?next=' + to_go )
            
    else:
        return render(request, 'accounts/login.html') #only want to retrieve the login page not submit on it

def logout(request):
    auth.logout(request)
    return redirect('travello:index')