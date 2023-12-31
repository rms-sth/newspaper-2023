from django.contrib import admin

from newspaper.models import (
    Category,
    Comment,
    Contact,
    Newsletter,
    Post,
    Tag,
    UserProfile,
)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)


from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(Post, PostAdmin)
