from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'owner', 'modify_date')
    list_filter   = ('modify_date',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)