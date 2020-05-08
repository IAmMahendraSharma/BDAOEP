from django.shortcuts import render, redirect
from .models import Student, Faculty

# Create your views here.
def index(req):
    return render(req, 'index.html')

def logout(req):
    return redirect('/', index)

def dashboard(req):
    participants = Student.objects.all().order_by('PEN')
    params = {'participants' : participants}
    return render(req, 'dashboard.html', params)

def register(req):
    return render(req, 'register.html')

def login1(req):
    email = req.POST.get('email', 'email')
    password = req.POST.get('password', 'password')
    if Faculty.objects.filter(Email = email, Password = hash(password)):
        return redirect('../dashboard', dashboard)
    else:
        return render(req, 'index.html')

def register1(req):
    admin = Faculty()
    admin.Name = req.POST.get('name', 'name')
    admin.Email = req.POST.get('email', 'email')
    admin.Gender = req.POST.get('gender', 'gender')
    admin.Mobile = req.POST.get('mobile', 'mobile')
    admin.Department = req.POST.get('department', 'department')
    admin.Password = hash(req.POST.get('password', 'password'))
    admin.save()
    return redirect('/', index)

def add(req):
    add_participant = Student()
    add_participant.PEN = req.POST.get('pen', 'pen')
    add_participant.Name = req.POST.get('name', 'name')
    add_participant.Email = req.POST.get('email', 'email')
    add_participant.Gender = req.POST.get('gender', 'gender')
    add_participant.Mobile = req.POST.get('mobile', 'mobile')
    add_participant.Semester = req.POST.get('semester', 'semester')
    add_participant.Department = req.POST.get('department', 'department')
    add_participant.save()
    return redirect('../dashboard', dashboard)

def update(req):
    add_participant = Student()
    add_participant.Name = req.POST.get('name', 'name')
    add_participant.Email = req.POST.get('email', 'email')
    add_participant.Gender = req.POST.get('gender', 'gender')
    add_participant.Mobile = req.POST.get('mobile', 'mobile')
    add_participant.Semester = req.POST.get('semester', 'semester')
    add_participant.Department = req.POST.get('department', 'department')
    if Student.objects.filter(Email = add_participant.Email).exists:
        add_participant.save()
        return redirect('../dashboard', dashboard)

def delete(req):
    pid = req.GET.get('pid', 'email')
    part = Student.objects.get(Email = pid)
    if part.delete():
        return redirect('../dashboard')
