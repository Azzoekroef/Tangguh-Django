from django.contrib import admin
from .models import Barang
from news.models import News
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class CustomAdminClass(ModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = True

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'tujuan_barang':
            kwargs['queryset'] = News.objects.filter(status=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Mengatur isi form untuk bidang-bidang tertentu
    fields = ('customuser','image_barang','desk', 'category','status','tujuan_barang','point')  # Atur bidang yang ingin ditampilkan di form
    readonly_fields = ['customuser','image_barang', 'desk', 'category']  # Field yang hanya bisa dilihat (tidak bisa diubah)
    list_filter = ['status']
    def image_preview(self, obj):
        if obj.image_barang:
            return mark_safe(f'<img src="{obj.image_barang}" style="max-width: 200px; max-height: 200px;" />')
        else:
            return 'No Image'

    image_preview.short_description = 'Image Preview'

    
    # Atau gunakan fieldsets untuk mengatur bidang dalam grup
    # fieldsets = (
    #     (None, {
    #         'fields': ('nama_barang', 'harga', 'deskripsi')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('status', 'kategori'),
    #     }),
    # )

admin.site.register(Barang, CustomAdminClass)