from django.urls import path
from dsci551 import views

urlpatterns = [
    path('', views.dsci551_index, name='dsci551_index'),
    path("<int:pk>/", views.dsci551_detail, name="dsci551_detail"),
]
