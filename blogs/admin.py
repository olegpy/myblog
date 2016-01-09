from django.contrib import admin

from blogs.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    search_fields = ['title']
    list_filter = ['author']
    fieldsets = [('Personal info', {'fields': ['author']}),
                 ('Blog info', {'fields': [
                     'title', 'text']}),
                 ('Date published', {'fields': [
                     'created_date', 'published_date']})
                 ]


admin.site.register(Post, PostAdmin)
