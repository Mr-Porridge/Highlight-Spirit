from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from spirit import *


# Create your views here.
@csrf_exempt
def highlight(request):
    elf = spirit(request.POST["code"])
    elf.analyze()
    return HttpResponse(json.dumps(elf.render()))
