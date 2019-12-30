from django.shortcuts import render

def index(reguest):
    return render(reguest, 'start/index.html')
