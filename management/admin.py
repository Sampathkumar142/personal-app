from django.contrib import admin
from . import models

# Register your models here.


# admin.site.register(models.level1Work)


# admin.site.register(models.level2Work)

@admin.register(models.level1Work)
class level1workAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


class relatedInformationInline(admin.StackedInline):
    model = models.relatedInformation
    extra= 0



@admin.register(models.level2Work)
class level2WorkAdmin(admin.ModelAdmin):
    inlines = [relatedInformationInline]
    list_display = ['title','parent','startDate','endDate','amount','description','createdAt']
    list_filter = ['parent']
    autocomplete_fields = ['parent']
    list_per_page = 10
    search_fields = ['title']
    ordering = ['-createdAt']


@admin.register(models.relatedInformation)
class relatedInformation(admin.ModelAdmin):
    list_display = ['document','level2Work','createdAt']
    search_fields = ['level2Work']
    list_filter = ['level2Work']
    ordering = ['-createdAt']



class documentInline(admin.StackedInline):
    model = models.RelatedDocument
    extra = 1


@admin.register(models.PersonalDocument)
class PersonalDocumentAdmin(admin.ModelAdmin):
    list_display = ['title','description','created_at']
    inlines = [documentInline]
    search_fields = ['title']
    ordering = ['-created_at']



@admin.register(models.RelatedDocument)
class RelatedDocumentAdmin(admin.ModelAdmin):
    list_display =['title','document','uploaded_at']
    list_filter = ['personaldoc__title']
    ordering = ['-uploaded_at']