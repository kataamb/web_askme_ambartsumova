from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('login/', views.log_in, name='login'),

    path('signup/', views.register, name='register'),

    path('ask/', views.ask, name='ask'),

    path('settings/', views.settings, name='settings'),

    path('questions/<int:question_id>', views.question, name='question'),
    path('tag/<slug:tag_slug>', views.tag, name='tag'),

]