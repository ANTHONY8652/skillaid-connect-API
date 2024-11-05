from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'created_at', 'updated_at']
    read_only_fields = ['created_at', 'updated_at']
    search_fields = ['title', 'course__title']
    list_filter = ['course', 'created_at']
    ordering = ['course', 'order']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

admin.site.register(Lesson, LessonAdmin)

# Register your models here.
