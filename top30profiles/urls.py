from django.urls import path, re_path

from . import views 

urlpatterns = [
    path("", views.initial_insights, name="initial insights"),
    path("industries/", views.industries, name="all industries"),
    re_path(r"^industries/...", views.specific_industry, name="selected industries")
]
