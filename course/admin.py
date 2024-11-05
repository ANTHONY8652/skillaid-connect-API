from django.contrib import admin
from .models import Course
from lesson.models import Lesson

class lessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ['title', 'content', 'order']
    ordering = ['order',]


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'category', 'difficulty_level', 'created_at', 'updated_at']
    read_only_fields = ['created_at', 'updated_at']
    search_fields = ['title', 'description', 'author', 'difficulty_level', 'category']
    list_filter = ['created_at', 'updated_at']
    ordering = ['created_at']
    inlines = [lessonInline]
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

admin.site.register(Course, CourseAdmin)


# Register your models here.
