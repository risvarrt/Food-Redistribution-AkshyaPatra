from django.contrib import admin

from .models import Post,Comment,Slider,Meeting,Feedback


class Meetings(admin.ModelAdmin):
    prepopulated_fields = {'MSlug' : ('title',)}
    
    
admin.site.register(Post,Meetings),
admin.site.register(Comment), 
admin.site.register(Slider), 
admin.site.register(Meeting), 
admin.site.register(Feedback), 
