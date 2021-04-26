from django.shortcuts import render
from datetime import datetime
from .models import myblog
# Create your views here.

def blog(request):
    name=''
    image = ''
    desc= ''
    data = myblog.objects.all()
    return render(request,'blog.html',{'data':data})


def blogentry(request):
    if(request.method == 'POST'):
        ima = request.FILES['image']
        name1 = request.POST['name']
        desc = request.POST['desc']
        myblog(img=ima,name=name1,about=desc,datetime=datetime.today()).save()
        
    return render(request, 'blogentry.html')