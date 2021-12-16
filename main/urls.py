from django.contrib import admin
from django.urls import path, include #add include

urlpatterns = [
  path('', include('main.urls')),  #add path
  path('admin/', admin.site.urls),
]