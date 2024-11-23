from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'review_content']
    list_filter = ['course_title', 'course']
    search_fields = ['course_title', 'review_content']
    date_hierarchy = 'created_at'

admin.site.register(Review, ReviewAdmin)

# Register your models here.
