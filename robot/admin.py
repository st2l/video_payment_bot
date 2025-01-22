from django.contrib import admin

from .models import TelegramUser, Video


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'user', 'id']
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ['video', 'title', 'id']


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Video, VideoAdmin)