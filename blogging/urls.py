from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'Blogging Admin Panel'
admin.site.site_title = 'Blogging'

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:id>/",views.post_detail,name="detail"),
    path("about/",views.about,name="about"),
    path("post/<int:id>/submit_comment/",views.submit_comment,name="submit_comment"),
]