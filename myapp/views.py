# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def hello(request,number):
   return render(request, "myapp/template/hello.html" %number, {})