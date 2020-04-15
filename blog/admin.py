from django.contrib import admin

# Register your models here.
from blog.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_per_page = 2
    sorted_by = "date_joined"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', )
    list_per_page = 2
    sorted_by = "date_joined"


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    fields = (('name', 'index'),)


# TODO 多对多的关系怎样处理
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'category', 'get_tag', 'click_count')
    list_display_links = ('title', 'desc', 'category', 'get_tag')
    list_editable = ('click_count',)
    list_filter = ('category',)
    list_per_page = 2
    fieldsets = [
        (None, {'fields': ('title', 'desc', 'content', 'user', 'category', 'tag')}),
        ('高级设置', {'classes': ('collapse',), 'fields': ('click_count', 'is_recommend')})
    ]
    sortable_by = 'click_count'

    def get_tag(self, obj):
        return obj.tag.first().name

    get_tag.short_description = 'tag'

    class Media:
        js = (
            '/static/js/tinymce/static/django_tinymce/jquery-1.9.1.min.js',
            '/static/js/tinymce/static/tiny_mce/tiny_mce.js',
            '/static/js/tinymce/js/tinymce/textareas.js'
        )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'date_publish', 'user', 'article')
    list_display_links = ('content', 'date_publish', 'user', 'article')


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'callback_url', 'date_publish')
    list_display_links = ('title', 'description', 'callback_url', 'date_publish')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url', 'callback_url', 'date_publish')
    list_display_links = ('title', 'description', 'image_url', 'callback_url', 'date_publish')



