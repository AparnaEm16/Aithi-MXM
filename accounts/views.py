from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method=='POST':
        pass
    else:
        form=AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})
