
from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    data=slider.objects.all().order_by('-id')[0:3]
    d=ncategory.objects.all().order_by('-id')[0:6]
    cd=mynews.objects.all().order_by('-id')[0:6]
    cc = mynews.objects.all().order_by('-id')[0:3]
    vdo=videonews.objects.all().order_by('-id')[0:2]
    ct=city.objects.all().order_by('-id')[0:6]

    mydict={"res":data,"data":d,"dm":cd,"vdata":vdo,"city":ct,"ndata":cc}

    return render(request,'user/index.html',mydict)
##################################################
def about(request):

    return render(request,'user/about.html')
################################################

def contact(request):
    status=False
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mob')
        message=request.POST.get('msg')
        contactus(Name=name,Email=email,Mobile=mobile,Message=message).save()
        status=True
    return render(request,'user/contact.html',context={"msg":status})
####################################################
def video(request):
    from django.db.models import Q
    vdata=videonews.objects.all().order_by('-id')
    if request.method=="GET":
        s=request.GET.get('search')
        if s is not None:

            vdata=videonews.objects.all().filter(Q(vhead__icontains=s) |Q(vcategory__icontains=s) |Q(vcity__icontains=s))


    mydict={"data":vdata}
    return render(request,'user/video.html',context=mydict)
#################################################
def gallery(request):
    d=igallery.objects.all().order_by('-id')
    mydict={"data":d}


    return render(request,'user/gallery.html',context=mydict)
#################################################
def news(request):
    x=ncategory.objects.all().order_by('-id')
    y=city.objects.all().order_by('-id')
    z=mynews.objects.all().order_by('-id')

    mydict={"cat":x,"ct":y,"ndata":z}
    ctid=request.GET.get('ctid')
    catid=request.GET.get('catid')
    if ctid is not None:
        z=mynews.objects.all().filter(ncity=ctid)
    elif catid is not None:
        z = mynews.objects.all().filter(category=catid)

    return render(request,'user/news.html',context=mydict)
##############################################
def ndetails(request):
    nid=request.GET.get('n')
    x=mynews.objects.all().filter(id=nid)
    myd={"ndata":x}

    return render(request,'user/ndetails.html',context=myd)
#################################################
def login(request):
    return render(request,'user/login.html')
###############################################

def viewnews(request):
    a=request.GET.get('msg')
    c=request.GET.get('cid')
    if a is not None:
        x=mynews.objects.all().filter(category=a).order_by('-id')
    elif c is not None:
        x = mynews.objects.all().filter(ncity=c).order_by('-id')
    mydict={"ndata":x}

    return render(request,'user/viewnews.html',context=mydict)

def vdetail(request):
    a=request.GET.get('vid')
    x=videonews.objects.all().filter(id=a)
    mydict={"vdata":x}
    return render(request,'user/vdetail.html',context=mydict)
def mydetails(request):
    return render(request,'user/mydetails.html')
