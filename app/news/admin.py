from django.contrib import admin

from .models import New


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'date',)

    def get_queryset(self, request):
        return New.objects.defer('content').order_by('id')

admin.site.register(New, NewsAdmin)
