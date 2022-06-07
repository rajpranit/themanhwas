from django.contrib import admin
from .models import   manhua , manhwa ,AllPost ,Comment ,Categories


admin.site.register(manhua)
admin.site.register(manhwa)
admin.site.register(AllPost)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    fields = ['tag','category','object_id','category_object']
    readonly_fields = ['category_object']
    class Meta:
        model = Categories

admin.site.register(Categories)


# Register your models here.
