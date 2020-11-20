from django.shortcuts import render
from dsci551.models import Dsci551
import pyrebase
#from pyspark.sql import SparkSession
from .models import Movies

#spark = SparkSession \
    #.builder \
    #.appName("q1") \
    #.config("spark.some.config.option", "some-value") \
    #.getOrCreate()

#ids = spark.read.option("header","true").csv('movies_id.csv')


config = {
    'apiKey': "AIzaSyD-cFEFVd5wfcXc4AD6hCRiuf1id39yJpg",
    'authDomain': "project-movie-reviews.firebaseapp.com",
    'databaseURL': "https://project-movie-reviews.firebaseio.com/",
    'storageBucket': "project-movie-reviews.appspot.com"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
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
    query = request.GET.get('input')
    if(query == None):
        query = "Star+Wars"
    #newColumns = ["id", "title"]

    #ids.toDF(*newColumns)

    query = query.replace('+', ' ')
    moviesID = Movies.objects.filter(title=query)
    answer = moviesID[0].id
    #answer = answer.first()[0]
    first_reviews = db.child("movie_reviews").child(answer).get().val()
    context = {
        "first_reviews": first_reviews
    }
    return render(request, 'dsci551_search.html', context)

def home(request):
    if request.method == 'POST':
        # 'genre_selection'：the name in this <select name="genre_selection">
        genre_selected = int(request.POST.get('genre_selection'))
        movie_info = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT m.title, m.popularity "
                           "FROM genres_in_movies g, movies m "
                           "WHERE g.genres_id = %s AND g.movie_id=m.id "
                           "limit 10", [genre_selected])
            movie_info = cursor.fetchall()
        genre_list = Genres.objects.all()
        context = {
            'genre_list': genre_list,
            'genre_selected': genre_selected,
            'movie_info': movie_info
        }
        return render(request, 'home.html', context)

    genre_list = Genres.objects.all()
    context = {
        'genre_list': genre_list
    }
    return render(request, 'home.html', context)