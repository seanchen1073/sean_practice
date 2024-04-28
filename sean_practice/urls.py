from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path("",views.home),
    path('about/',views.about_us),
    path('admin/', admin.site.urls),
]
