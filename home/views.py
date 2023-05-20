from django.shortcuts import render, redirect
from .models import Product, WebsiteSettings
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login,logout


# Create your views here.
def dashboard(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,"index.html", context)

def adminRep(request):
    if request.user.is_superuser:
        return render(request, "admin.html")  
    else:
        messages.info(request,'login as admin')
        return redirect("login") 

def adminProductDis(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            title = request.POST['title']
            discription = request.POST['discription']
            image  = request.FILES.get('img')
            product = Product(
                title=title,
                description=discription,
                image=image
                )
            product.save()
            messages.info(request,'added succesfully')
        print(request.user.is_superuser)    
        return render(request, "adminProductDis.html") 
    else:
        messages.info(request,'login as admin')
        return redirect("login")     

def websiteSettings(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            logo = request.FILES.get('logo')
            adderss = request.POST['address']
            phoneNO  = request.POST['PhoneNO']
            settings = WebsiteSettings(
                logo=logo,
                address=adderess,
                phone_number=phoneNO  
            )
            settings.save()
            messages.info(request,'added succesfully')
        return render(request, "setting.html") 
    else:
        messages.info(request,'login as admin')
        return redirect("login")            

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect("adminRep")
        else:
            messages.info(request, "username or password is incorrect") 
            return redirect("login")   
    else:    
        return render(request, "login.html")


def log_out(request):
    logout(request)
    messages.info(request,"you have succesfully logout")
    return redirect("login")        