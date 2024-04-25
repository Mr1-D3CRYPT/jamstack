from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from api.models import Complaint

def profile(request):
    user = request.user
    if user.is_authenticated:
        complaints = Complaint.objects.filter(reg=user)
        uname = user.username
        return render(request, "profile.html", {"complaints": complaints,"username":uname})
    else:
        return redirect("/login")

def delete_complaint(request):
    if request.method == 'POST':
        complaint_id = request.POST.get('complaint_id')
        if complaint_id:
            complaint = Complaint.objects.get(uid=complaint_id)
            complaint.delete()
    return redirect('/profile')

def submit_complaint(request):
    if request.method == "POST":
        user = request.user
        complaint_text = request.POST.get("complaint")
        Complaint.objects.create(reg=user, compt=complaint_text)
        return redirect("/profile")
    else:
        return redirect("/profile")
     
def register(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/profile")
    if request.method=='POST':
        username = request.POST.get("username")
        passw = request.POST.get("pass")
        try:
            User.objects.get(username=username) 
            message = "user exists!! try another username"
            return render(request,"register.html",{"message":message})
        except User.DoesNotExist:
            User.objects.create_user(username=username, password=passw)
            user = authenticate(request, username=username, password=passw)

            if user is not None:
                login(request, user)
                return redirect('/profile')
    return render(request,"register.html")
    
def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/profile")
    if request.method=='POST':
        username = request.POST.get("username")
        passw = request.POST.get("pass")

        user = authenticate(request, username=username, password=passw)    
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            message = "Invalid username or password. Please try again."
            return render(request, "login.html", {"message": message})
    return render(request,"login.html")
    
def logout_view(request):
    logout(request)
    return redirect('/login')
    