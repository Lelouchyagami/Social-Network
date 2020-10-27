from django.contrib import admin
from .models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__','user']
    search_fields = ['content','user__username','user__email']

admin.site.register(Tweet)