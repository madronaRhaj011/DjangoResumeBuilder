from django.urls import path
from . import views

urlpatterns = [
    path('', views.collect_resume_info, name='collect_resume_info'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]
