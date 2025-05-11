from django.contrib import admin
from .models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created_date", "published_date") # fazendo assim ele lista todas as colunas no admin !!


# from django.contrib import admin
# from .models import Post

# admin.site.register(Post) esse modo nao permite lista