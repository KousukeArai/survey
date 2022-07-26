from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('grade1/', views.Grade1View.as_view(), name='grade1'),
    path('grade2/', views.Grade2View.as_view(), name='grade2'),
    path('grade3/', views.Grade3View.as_view(), name='grade3'),
    path('小学1年生/', views.Question1View.as_view(), name='小学1年生'),
    path('小学2年生/', views.Question2View.as_view(), name='小学2年生'),
    path('小学3年生/', views.Question3View.as_view(), name='小学3年生'),
    # path('result/', views.ResultView.as_view(), name='result'),
]