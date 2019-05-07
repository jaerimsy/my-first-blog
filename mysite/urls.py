from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/login', include('django.contrib.auth.urls')), # new
    #path('accounts/login/', include('blog.urls')),
    #path('accounts/login/', include('blog.urls')),    
]