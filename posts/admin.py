from django.contrib import admin
from posts.models import User,Post,Comment,Like

#admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)


# Register your models here.
