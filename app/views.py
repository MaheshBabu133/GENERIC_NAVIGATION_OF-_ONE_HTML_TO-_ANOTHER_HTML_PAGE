from django.shortcuts import render

# Create your views here.
def navigate(request):
    '''d={'name':'Akshaya','age':23} '''
    return render(request,'hai.html')



def navigate1(request):
   #d={'name':'TejuPapa','age':23}
    return render(request,'bye.html')