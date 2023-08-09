from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='dashboard'),
    path('about/',about, name='about'),
    path('projects/',portfolio, name='portfolio'),
    path('projects/<int:pk>',portfolio_detail, name='portfolio-detail'),
    path('blog/',blog, name='blog'),
    path('blog/<int:pk>',blog_detail, name='blog-detail'),
    path('contact',contact, name='contact'),
]