from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *


def sample(request):
    return render(request,'sample.html')

# def insert_topic(request):
#     if request.method=='POST':
#         tn=request.POST['tn']
#         TO=Topic.objects.get_or_create(topic_name=tn)[0]
#         TO.save()
#         return HttpResponse('Topic  is Created Successfully')

#     return render(request,'insert_topic.html')


# def insert_Webpage(request):
#     QLTO=Topic.objects.all()
#     d={'QLTO':QLTO}

#     if request.method=='POST':
#         tn=request.POST['tn']
#         n=request.POST['n']
#         url=request.POST['url']
#         email=request.POST['email']

#         RTO=Topic.objects.get(topic_name=tn)
#         WPO=Webpage.objects.get_or_create(topic_name=RTO,name=n,url=url,email=email)[0]
#         WPO.save()
#         return HttpResponse('Web-page  is Created Successfully')
    
#     return render(request,'insert_Webpage.html',d)  


def insert_AccessRecord(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    
    if request.method=='POST':
        na=request.POST['na']
        d=request.POST['d']
        aut=request.POST['aut']
        email=request.POST['email']

        RWPO=Webpage.objects.get(id=na)
        IAO=AccessRecord.objects.get_or_create(name=RWPO,date=d,author=aut,email=email)[0]
        IAO.save()
        return HttpResponse('AccessRecord  is Created Successfully')
    return render(request,'insert_AccessRecord.html',d)


def display_Webpage(request):
    QLTO = Webpage.objects.all()[::5]
    QLTO = Webpage.objects.filter(name__startswith='a')
    QLTO = Webpage.objects.filter(name__contains='t')
    QLTO = Webpage.objects.filter(name__endswith='r')

    QLTO = Webpage.objects.filter(topic_name='Cricket')
    QLTO = Webpage.objects.filter(topic_name='Football')
    QLTO = Webpage.objects.exclude(topic_name='Chess')
    QLTO = Webpage.objects.filter(name__in=['Vamsi','Virat'])   

    d={'QLTO':QLTO}
    return render(request,'display_Webpage.html',d)


def display_AccessRecord(request):
    QLAR=AccessRecord.objects.all()[1:]
    QLAR=AccessRecord.objects.filter(date__gt='2016-02-13')
    QLAR=AccessRecord.objects.filter(date__lt='2024-05-08')
    
    d={'QLAR':QLAR}
    return render(request,'display_AccessRecord.html',d)

def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        STL=request.POST.getlist('tn')
        WOS=Webpage.objects.none()
        for t in STL:
            WOS=WOS|Webpage.objects.filter(topic_name=t)
        d1={'WOS':WOS}
        
        # print(WOS)
        return render(request,'display_Webpage.html',d1)
    
    return render(request,'select_multiple.html',d)


def checkbox(request):
    QTO=Topic.objects.all()
    d={'QTO':QTO}
    
    return render(request,'checkbox.html',d)

# ----------------------------------------------

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFO=TopicForm(request.POST)
        if TFO.is_valid():
            tn=TFO.cleaned_data['tn']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            # return HttpResponse('Data is created')
            return HttpResponse(str(TFO.cleaned_data))
        else:
            return HttpResponse('Data is not created')
    return render(request,'insert_topic.html',d)


def insert_Webpage(request):
    WFO=WebpPageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFDO=WebpPageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['tn']
            name=WFDO.cleaned_data['name']
            email=WFDO.cleaned_data['email']
            url=WFDO.cleaned_data['url']

            RTO=Topic.objects.get(topic_name=tn)
            WPO=Webpage.objects.get_or_create(topic_name=RTO,name=name,url=url,email=email)[0]
            WPO.save()
            return HttpResponse('Webpage  is Created Successfully')
        else:
            return HttpResponse('Data is not created')
    
    return render(request,'insert_Webpage.html',d)