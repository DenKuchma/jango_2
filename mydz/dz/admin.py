from django.contrib import admin
from .models import Bloger, Publicate, Comment, Like, Disike

admin.site.register(Bloger)
admin.site.register(Publicate)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Disike)

