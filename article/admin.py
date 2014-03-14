from django.contrib import admin

from article.models import Article,Comments

class Article_inline(admin.StackedInline):
	model=Comments
	extra=2

class Article_admin(admin.ModelAdmin):
	fields=['article_title','article_text','article_date']
	inlines=[Article_inline]


admin.site.register(Article,Article_admin)

# Register your models here.
