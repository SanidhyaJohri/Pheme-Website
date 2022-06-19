from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('',views.index, name='home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('Acads', views.Acads, name='Acads'),
    path('Extra', views.Extra, name='Extra'),
    path('project_details', views.project, name='project_details'),
    path('eventsBlog', views.eventsBlog, name='eventsBlog'),
    path('blogDetail',views.blogDetail, name='blogDetail'),
    path('blog',views.BlogList.as_view(),name='blog'),
    path('event',views.EventList.as_view(),name='events'),
    path('<slug:slug>',views.EventDetail.as_view(),name='event_detail'),
    path('<slug:slugBlog>',views.BlogDetail.as_view(),name='blog_detail'),
]