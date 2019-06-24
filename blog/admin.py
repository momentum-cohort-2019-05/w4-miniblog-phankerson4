from django.contrib import admin
from blog.models import Author, Blog

# Register your models here.




# Define the admin class
@admin.register(Author)
class Author(admin.ModelAdmin):

    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
#admin.site.register(Author)

# Register the Admin classes for Blog using the decorator



@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title', 'author')
    





