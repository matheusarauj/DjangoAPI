from django.contrib import admin

from .models import Course, Evaluation

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publication', 'update', 'active')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'evaluation', 'publication', 'update', 'active')

