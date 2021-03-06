
from django.contrib import admin
from django.urls import path, include
from article import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexview, name = "index"),
    path('about', views.aboutview, name = "about"),
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

