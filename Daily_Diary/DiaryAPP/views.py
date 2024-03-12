from django.shortcuts import render
from django.views.generic import View
from DiaryAPP.models import dairy_db,contentdb
from django.db import IntegrityError



class base(View):
    def get(self,request):
        return render(request,'base.html')

class Register(View):
    def get(self, request):
        return render(request, 'Register.html')

    def post(self, request):
        user = request.POST['username']
        pwd = request.POST['password']
        try:
            # Attempt to create a new entry
            dairy_db.objects.create(user=user, password=pwd)
            return render(request, 'Login.html', {'msg': 'You are registered successfully. Please login'})
        except IntegrityError:
            # Handle the case where the username already exists
            return render(request, 'Register.html', {'msg': 'Username already taken. Please choose a different username'})


class Login(View):
    def get(self,request):
        return render(request,'Login.html')

    def post(self, request):
        user = request.POST['username']
        pwd = request.POST['password']
        rec = dairy_db.objects.filter(password=pwd, user=user)
        if rec.exists():
            request.session['user'] = user  # Set the user in the session
            return render(request, 'Writing.html', {'msg': 'LogIn successful...', 'username': user})
        else:
            return render(request, 'Login.html', {'msg': 'Invalid Credentials. Please log in again...'})



class Writing(View):
    def get(self, request):
        return render(request, 'writing.html')

    def post(self, request):
        user = request.session.get('user')
        if user:
            try:
                user_instance = dairy_db.objects.get(user=user)
                date = request.POST['date']
                content = request.POST['content']
                content_entry = contentdb.objects.create(user=user_instance, date=date, content=content)
                return render(request, 'showrecs.html',{'msg':'record inserted successfully...'})
            except dairy_db.DoesNotExist:
                return render(request, 'login.html', {'msg': 'User not found. Please log in again.'})
        else:
            return render(request, 'login.html', {'msg': 'User information not found. Please log in again.'})



class ShowRecords(View):
    def get(self, request):
        # Retrieve the username from the session
        username = request.session.get('user')

        # Retrieve records based on the username
        records = contentdb.objects.filter(user__user=username)

        return render(request, 'showrecs.html', {'records': records})

class view_page(View):
    def get(self,request):
        # Retrieve the username from the session
        username = request.session.get('user')
        # Retrieve records based on the username
        records = contentdb.objects.filter(user__user=username)
        return render(request,'view.html', {'records': records})

def Logout(request):
    if 'username' in request.session:
        del request.session['username']
    else:
        # If 'username' key is not in the session, the user is not logged in
        return render(request, 'Login.html', {'msg': 'Please Login first '})
    return render(request, 'Login.html', {'msg': 'Logged Out Successfully'})

class home(View):
    def get(self,request):
        return render(request,'home.html')

class contact(View):
    def get(self,request):
        return render(request,'contact.html')