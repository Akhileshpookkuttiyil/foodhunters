from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import ModelForm
# Create your views here.

def home(request):
    obj=Vlog.objects.all()
    return render(request,'home.html',{'vlogs':obj})

def add(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        title = request.POST.get('title')
        location = request.POST.get('location')
        descriptions = request.POST.get('description')
        image = request.FILES['image']
        author = request.POST.get('author')
        s = Vlog(title=title,date=date,location=location,image=image,description=descriptions,author=author)
        s.save()
        print('blog added')
        return redirect('/')
    return render(request, 'add_blogs.html')

def update(request,vlog_id):
    obj = get_object_or_404(Vlog,id=vlog_id)
    form = ModelForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit_blg.html', {'form': form, 'obj': obj})

def detail(request,vlog_id):
    vlog=Vlog.objects.get(id=vlog_id)
    return render(request,'details.html',{'vlog':vlog})

def delete(request,vlog_id):
    vlog=Vlog.objects.get(id=vlog_id)
    vlog.delete()
    return redirect('/')
