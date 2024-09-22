from django.urls import path
from .views import course_list, view_profile , edit_profile

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]