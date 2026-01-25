from django.contrib import admin
from .models import Post

# add blog models to the administration site
# admin.site.register(Post)

#   Tell the Django administration site that the model is registered in the site using a custom class
#   includes information about how to display the model on the administration site

# Register your models here

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #   allows the dev to set the fields of your model that he or she wants to display on the administration object list page
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    #  Django 5.0 -> facet filters for administration site -> facet counts. They indicate the number of objects
    #   corresponding to each specific filter, making it easier to identity matching objects in the admin changelist view
    show_facets = admin.ShowFacets.ALWAYS