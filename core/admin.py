from django.contrib import admin
from . import models
# Register your models here.

class FriendAdmin(admin.ModelAdmin):
    pass
class NotificationAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Friend,FriendAdmin)
admin.site.register(models.Notification,NotificationAdmin)
admin.site.register(models.Post,PostAdmin)
