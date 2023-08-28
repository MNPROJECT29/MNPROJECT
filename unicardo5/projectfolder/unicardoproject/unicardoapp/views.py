from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import slotform
from .models import unislot


# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def unicardo(request):
    card_item=unislot.objects.all()

    return render(request,'unicardo.html',{'card':card_item})

def detail(request,id):
    item_var=unislot.objects.get(id=id)
    return render(request,'detail.html',{'item':item_var})

def base(request):
    return render(request,'base.html')

def slot_add(request):
    if request.method == 'POST':
        s_name=request.POST.get('slot_name')
        s_desc=request.POST.get('slot_desc')
        s_location=request.POST.get('slot_location')
        s_image=request.FILES.get('slot_image')
        if unislot.objects.filter(name=s_name).exists():
            return render(request,'add.html')
        else:
          new_slot=unislot(name=s_name,desc=s_desc,location=s_location,image=s_image)
          new_slot.save()
          return redirect('/')

    return render(request,'add.html')

def slot_update(request,name):

    slot=unislot.objects.get(name=name)

    form_b=slotform(request.POST or None,request.FILES,instance=slot)

    if form_b.is_valid():
        form_b.save();
        return redirect('/')
    return render(request,'edit.html',{'form_key':form_b,'slot':slot})


def slot_delete(request,name):
    if request.method == "POST":
         slot_d=unislot.objects.get(name=name)
         slot_d.delete()
         return redirect('/')
    return render(request,'delete.html')
