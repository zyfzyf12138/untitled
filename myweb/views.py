from django.shortcuts import render
from myweb import  models
# Create your views here.
def moviename(request):
    mov_list=models.Movie.objects.all()
    print(mov_list)
    context={
        'mov_list':mov_list
    }
    return render(request,'douban.html',context=context)

def find(request):
    return render(request,'choose.html')


# Create your views here.
