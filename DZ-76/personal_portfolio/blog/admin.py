from django.contrib import admin
from  .models import Blog

# что бы она была видна в админ панеле

admin.site.register(Blog)
