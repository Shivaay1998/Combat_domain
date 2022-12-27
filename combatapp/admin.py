from django.contrib import admin
from combatapp.models import Entry
# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "profile_img", "email", "contact", "gender", "day","month","year","city","country","documents","passwords"]
admin.site.register(Entry, EntryAdmin)