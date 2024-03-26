from django.contrib import admin
from .models import UserDetail,UserRelative,Celebration,CelebrationParticipants,Leave,Attendance

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(UserRelative)
admin.site.register(Celebration)
admin.site.register(CelebrationParticipants)
# admin.site.register(Leave)
admin.site.register(Attendance)

@admin.register(Leave)
class UserAdmin(admin.ModelAdmin):
    list_display = ['leavetype','notes','dates','reason','user','status']


   