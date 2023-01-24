from django.contrib import admin
from django import forms
from django.db import models
from .models import EnglishWord, RussianWord, Picture

# Register your models here.
@admin.register(EnglishWord)
class EnglishWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'rating', 'updated_at')

@admin.register(RussianWord)
class RussianWordAdmin(admin.ModelAdmin):
    list_display = ('word',)

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'english_word', 'russian_word')
    formfield_overrides = {
        models.FileField: {'widget': forms.ClearableFileInput},
    }
