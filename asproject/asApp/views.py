from django.shortcuts import render,redirect,HttpResponse
from asApp.models import Request,Update
from asApp.forms import CustomerCreationForm,CustomerLoginForm,RequestForm,UpdateForm
from django.contrib.auth import authenticate , login as loginUser, logout as logoutUser

# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = CustomerCreationForm()
        return render(request,template_name='signup.html',context={'form':form})
    else:
        if request.method == 'POST':
            form = CustomerCreationForm(request.POST or None)
            if form.is_valid():
                user = form.save()
                user.email = user.username
                user.save()
                return redirect('loginpage')
            context = {
                'form': form
            }
            return render(request, template_name='signup.html', context=context)



def login(request):
    if request.method == 'GET':
        form = CustomerLoginForm()
        return render(request,template_name='login.html',context={'form':form})
    else:
        if request.method == 'POST':
            form = CustomerLoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username,password = password)
                if user:
                    loginUser(request,user)
                    return redirect('requestpage')
            else:
                return render(request,template_name='login.html',context={'form':form})


def request_page(request):
    if request.method == 'GET':
        form = RequestForm()
        return render(request,template_name='request.html',context={'form':form})
    else:
        if request.method == 'POST':
            form = RequestForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('requestlistpage')
            else:
                return render(request,template_name='request.html',context=None)


def request_list(request):
    there = Request.objects.all()
    context = {
        'there':there
    }
    return render(request,'requestlist.html',context=context)

def updatepage(request):
    if request.method=='GET':
        form = UpdateForm()
        here = Request.objects.all()
        return render(request,'update.html',{'here':here,'form':form})

    else:
        if request.method == 'POST':
            form = UpdateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('statuspage')
            else:
                return render(request,'update.html',{'form':form})

def viewrequeststatuspage(request):
    there = Request.objects.all()
    return render(request,'status.html',{'there':there})








