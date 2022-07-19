from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/create_vote/',views.create_vote,name='create_vote'),
    path('create_poll/',views.create_poll,name='create_poll'),
    path('post_poll/',views.post_poll,name='post_poll'),

]