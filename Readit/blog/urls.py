from django.conf.urls import url
from .import views
from django.urls import path

urlpatterns = [
    path('',views.Home),
    path('<slug:slug>/<int:id>',views.article_details,name="article_details")
]
