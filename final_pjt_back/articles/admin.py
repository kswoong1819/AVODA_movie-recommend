from django.contrib import admin
from .models import Article, Comment_article
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment_article)
