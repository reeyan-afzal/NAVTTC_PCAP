from django.contrib import admin

from meetings.models import Meeting, Room

admin.site.register(Meeting)
admin.site.register(Room)

# Register your models here.
