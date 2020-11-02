from django.contrib import admin
from .models import DB_Bloger , DB_Tags ,Comment ,ReplayToComment


admin.site.register(DB_Bloger)
admin.site.register(DB_Tags)
admin.site.register(Comment)
admin.site.register(ReplayToComment)