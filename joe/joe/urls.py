from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poweroflamp/', views.power, name="power"),
    path('', views.power, name="powerofincandescentlamp"),
]
