"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
from mymodels.models import USER



def home(request):
    aa=USER.objects.all()
    return HttpResponse(aa)
def pizzaHut(request):
    return render(request,'Pizzahut.html')

def sirTable(request):
    aa=USER.objects.all()
    user={
        'user':aa
    }

    if request.method=="POST":

        data=request.POST
        username=data.get('username')
        user_Emailid=data.get('user_Emailid')
        password=data.get('password')

        print(username,user_Emailid,password,'-=-=-')

        ul=USER(username=username,
                user_Emailid=user_Emailid,
                password=password)
        ul.save()

    return render(request,'sirTable.html',user)


def UserDelete(request,id):
    a=USER.objects.get(id=id).delete()
    pass
    print(a,'--a--')
    return redirect('/s')

def UserUpdate(request,id):
    onedata=USER.objects.get(id=id)
    print(onedata,'onedata')
    if request.method=="POST":
        username=request.POST['username']
        user_Emailid=request.POST['user_Emailid']
        password=request.POST['password']
        print('test post area')
        print(username,user_Emailid,password,'-=-=-')
        pass
        CollectionData=USER(id=id,username=username,password=password,user_Emailid=user_Emailid)
        CollectionData.save()
        print(CollectionData,'CollectionData')
        return redirect('/s')

    return render(request,'UserUpdate.html',{'onedata':onedata})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p',home),
    path('',pizzaHut),
    path('s',sirTable),
    path('UserDelete/<int:id>',UserDelete ,name='UserDelete'),
    path('UserUpdate/<int:id>',UserUpdate ,name='UserUpdate'),
]

