from django.shortcuts import render
from .forms import ImageFrom
from .models import Image

# Create your views heregrf
def home(request):
    if request.method=='POST':
        form=ImageFrom(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    form=ImageFrom()
    img=Image.objects.all()
    
    return render(request,'testapp/base.html',{'img':img ,'form':form})

