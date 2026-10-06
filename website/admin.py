from django.contrib import admin

from website.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured',)
    list_display = ('title', 'category', 'status', 'is_featured')
    
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
