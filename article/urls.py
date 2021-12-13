from django.contrib import admin
from django.urls import path
from article import views
app_name = "article"
urlpatterns = [
    path('dashbord', views.dashbordview, name='dashbord'),
    path('addarticle', views.addarticleview, name='addarticle'),
    path('<slug:slug>', views.detailview, name='detail'),
    path('category/<slug:slug>', views.category, name='category'),
    path('update/<int:id>', views.updateArticle, name='update'),
    path('delete/<int:id>', views.deleteArticle, name='delete'),
    path('comment/<int:id>', views.addComment, name='comment'),
    path('', views.articlesview, name='article'),



]
