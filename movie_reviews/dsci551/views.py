from django.shortcuts import render
from dsci551.models import Dsci551
import pyrebase

config = {
    'apiKey': "AIzaSyD-cFEFVd5wfcXc4AD6hCRiuf1id39yJpg",
    'authDomain': "project-movie-reviews.firebaseapp.com",
    'databaseURL': "https://project-movie-reviews.firebaseio.com/",
    'storageBucket': "project-movie-reviews.appspot.com"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
first_reviews = db.child("movie_reviews").child("11").get().val()

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

def search(request):
    context = {
        "first_reviews": first_reviews
    }
    return render(request, 'dsci551_search.html', context)
