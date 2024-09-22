from django.contrib import admin
from .models import Course

# Register the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at')
    search_fields = ('title', 'instructor__username')  # Allows searching by course title and instructor's username
    list_filter = ('instructor', 'created_at')
