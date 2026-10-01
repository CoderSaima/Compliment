from App import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.compliment, name="compliment"),
    path('form/', views.Form_view, name="compliment"),
]
