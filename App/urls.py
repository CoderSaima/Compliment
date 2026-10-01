from App import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('com/', views.compliment, name="compliment"),
    path('', views.Form_view, name="compliment"),
]
