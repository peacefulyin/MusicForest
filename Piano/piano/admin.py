# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from piano.models import *

admin.site.register(User)
admin.site.register(Sheet)
admin.site.register(Comment)