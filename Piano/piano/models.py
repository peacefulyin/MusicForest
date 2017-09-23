# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20,default='琴友')
    uname = models.CharField(max_length=20,default='', unique=True)
    upwd = models.CharField(max_length=20,default='')
    email = models.EmailField(default='')
    gender = models.BooleanField(default=True)
    def __str__(self):
        return self.name.encode('utf-8')

class Sheet(models.Model):
    album = models.CharField(max_length=50)
    music = models.CharField(max_length=50)
    page_num = models.IntegerField(default=0)
    def __str__(self):
        return self.music.encode('utf-8')



class Comment(models.Model):
    name = models.CharField(max_length=100)
    pub_time = models.DateTimeField()
    text = models.CharField(max_length=300)
    artical = models.ForeignKey(Sheet)
    def __str__(self):
        return self.name.encode('utf-8')