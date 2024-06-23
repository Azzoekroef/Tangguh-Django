# # admin.py
# # from django import models
# from django.db import models
# from .models import CustomUser
# from django.contrib import admin
# from unfold.admin import ModelAdmin
# from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget


# @admin.register(CustomUser)
# class CustomAdminClass(ModelAdmin):
#     # Display fields in changeform in compressed mode
#     compressed_fields = True  # Default: False

#     # Preprocess content of readonly fields before render
#     readonly_preprocess_fields = {
#         "model_field_name": "html.unescape",
#         "other_field_name": lambda content: content.strip(),
#     }
#     # field = ['username']
#     # list_display = ['username']

#     # Display submit button in filters
#     list_filter_submit = True
#     # Custom actions
#     actions_list = []  # Displayed above the results list
#     actions_row = []  # Displayed in a table row in results list
#     actions_detail = []  # Displayed at the top of for in object detail
#     actions_submit_line = []  # Displayed near save in object detail

#     formfield_overrides = {
#         models.TextField: {
#             "widget": WysiwygWidget,
#         },
#     }