# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Group
from .models import User


# Register your models here.

admin.site.register(Group)
admin.site.register(User)