from django.contrib import admin
from blog.models import Post
from users.models import Profile

admin.site.register(Post)
admin.site.register(Profile)