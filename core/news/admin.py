from django.contrib import admin
from .models import News
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
# from .models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('nama','image_news','desk', 'status','category') 
        labels = {
            'status': 'Status Donasi',  # Mengubah label dari 'nama' menjadi 'nama_news'
        }
        # widgets = {
        #     'desk': forms.HiddenInput(),  # Sembunyikan input untuk image_news jika tidak ingin diedit
        # }

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['desk'].widget.attrs['readonly'] = True   # Field yang hanya bisa dilihat (tidak bisa diubah)

        # readonly_fields = ['nama']
        # widgets = {
        #     'image_news': forms.HiddenInput(),
        # }
        # def __init__(self, *args, **kwargs):
        #     super(NewsForm, self).__init__(*args, **kwargs)
        #     self.fields['image_news'].required = False

        # def image_preview(self):
        #     if self.instance and self.instance.image_news:
        #         return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />', self.instance.image_news.url)
        #     return 'No Image'


# class CustomUserChangeForm(UserChangeForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     disabled password hash display field.
#     """
#     class Meta:
#         model = News
#         # exclude = []
#         # exclude = ['is_staff']
#         readonly_fields = ('nama','image_news','desk', 'status','category') 

        # readonly_fields = ['desk']
        # fields = ('nama','image_news','desk', 'status','category') 

        # fields = ["email", "password", "is_active", "bank_name"]


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = CustomUserChangeForm
#     add_form = CustomUserCreationForm
class LokasiFilter(admin.SimpleListFilter):
    title = 'lokasi'
    parameter_name = 'lokasi'

    def lookups(self, request, model_admin):
        # Mengambil daftar unik lokasi dari database
        lokasi_list = News.objects.values_list('lokasi', flat=True).distinct()
        return [(lokasi, lokasi) for lokasi in lokasi_list]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(lokasi=self.value())
        return queryset

# admin.site.register(News, UserAdmin)
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

    

    # Mengatur isi form untuk bidang-bidang tertentu
    # fields = ('nama','image_news','desk', 'status','category','lokasi')  
    # Atur bidang yang ingin ditampilkan di form
    form = NewsForm
    list_filter = ['status']
    # def image_preview(self, obj):
    #     if obj.image_barang:
    #         return mark_safe(f'<img src="{obj.image_barang}" style="max-width: 200px; max-height: 200px;" />')
    #     else:
    #         return 'No Image'

    # image_preview.short_description = 'Image Preview'

    # def status_display(self, obj):
    #     return obj.get_status_display()

    # status_display.short_description = 'Status Donasi'
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

admin.site.register(News, CustomAdminClass)

