#!/usr/local/bin/python3.5
#_*_ coding:utf-8 _*_

from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def ChristmasTree(h):
    '''创建圣诞树'''
    str_tree = ''
    for n in range(1,h+1):
        spc = 2*h-(2*n-1)
        str_tree = str_tree + '&nbsp;'*(spc//2) + '*'*(2*n-1)+'<br>'
    for i in range(h):
        str_tree = str_tree + '&nbsp;'*(h-1)+'*'+'<br>'
    return str_tree
    
def christmastree_form(request):
    return render(request, 'christmastree_form.html',locals())
    
def christmastree(request):
    if 'high' in request.GET:
        high = request.GET['high']
        tree = ChristmasTree(int(high))
        return render(request, 'chr.html',locals())
    else:
        message = "you submitted an empty form"
    return HttpResponse(message)