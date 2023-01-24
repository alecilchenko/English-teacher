from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('add-eng-word/', views.AddEngWordView.as_view(), name='add_eng_word'),
    path('add-rus-word/', views.AddRusWordView.as_view(), name='add_rus_word'),
    path('add-picture/', views.AddPictureView.as_view(), name='add_picture'),
]