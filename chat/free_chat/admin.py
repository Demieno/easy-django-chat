from django.contrib import admin

# Register your models here.
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model = Message
        fields = '__all__'


admin.site.register(Message, MessageAdmin)
