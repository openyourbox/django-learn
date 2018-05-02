from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/results/', views.result),
    path('<int:question_id>/vote/', views.vote, name = 'vote')

]