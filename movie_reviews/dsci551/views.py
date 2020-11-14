from django.shortcuts import render
from dsci551.models import Dsci551

# Create your views here.
def dsci551_index(request):
    dsci551 = Dsci551.objects.all()
    context = {
	'dsci551': dsci551
    }
    return render(request, 'dsci551_index.html', context)

def dsci551_detail(request, pk):
    dsci551 = Dsci551.objects.get(pk=pk)
    context = {
 	'dsci551': dsci551
    }
    return render(request, 'dsci551_detail.html', context)

def dsci551(request):
    return render(request, 'dsci551.html', {})
