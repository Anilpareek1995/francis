from django.shortcuts import render,redirect
from django.contrib import messages
from .models import wanted,Missing
# Create your views here.

def pmissing(request):
    if request.method == 'POST':
        name = request.POST["t1"]
        mobile = request.POST["t2"]
        address = request.POST["t3"]
        city = request.POST["t4"]
        image = request.FILES["imgfile"]
        details = request.POST["t6"]
        mst = Missing(name=name, mobile=mobile, address=address, city=city, image=image,details=details)
        mst.save()

    return render(request,'Police/missing.html')

def mostwanted(request):
    if request.method =='POST':
        uname = request.POST.get('name')
        height = request.POST.get('height')
        color = request.POST.get("color")
        crime_type = request.POST.get("crime_type")
        crime_area = request.POST.get("crime_area")
        crime_spot = request.POST.get("crime_spot")
        image = request.FILES.get("img")
        mst = wanted(uname=uname, height=height, color=color, crime_type=crime_type, crime_area=crime_area,crime_spot=crime_spot, photo=image)
        mst.save()
    return render(request,'Police/mostwanted.html')


def policehome(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Police/phome.html', context)
    
    