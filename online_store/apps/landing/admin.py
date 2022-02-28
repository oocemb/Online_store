from django.contrib import admin
from .models import *

# class SubscriberAdmin (admin.ModelAdmin):
#     list_display = {field.name for field in Course._meta.fields}
#     inlines = [FieldMappingInline]
#     fields = []
#     exclude = ['type']
#     list_filter = ('report_data',)
#     search_fields = ['category','subCategory','suggestKeyword']
#     class Meta:
#         model = Subscriber

admin.site.register(Subscriber)

