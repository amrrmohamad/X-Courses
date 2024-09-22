from django.urls import path
from .views import (
    course_list,
    create_course,
    edit_course,
    course_detail,
    signup,
    login_view,
    logout_view,
)

urlpatterns = [
    path('', course_list, name='course_list'),  
    path('create-course/', create_course, name='create_course'),  
    path('edit-course/<int:course_id>/', edit_course, name='edit_course'),
    path('<int:course_id>/', course_detail, name='course_detail'),
    path('signup/',signup, name='signup'),  
    path('login/', login_view, name='login'),  
    path('logout/',logout_view, name='logout'),
]
