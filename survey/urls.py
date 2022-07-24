from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('',views.IndexListView.as_view(), name='index'),
    path('questions/',views.QuestionsView.as_view(), name='questions')
]