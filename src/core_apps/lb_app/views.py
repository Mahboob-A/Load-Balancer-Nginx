from django.shortcuts import render

from django.http.response import JsonResponse

import socket 

from datetime import datetime 


def demo_view(request):
    now = datetime.now()
    host = socket.gethostname()
    return JsonResponse({"status": "OK", "time": now, "host": host}, status=200)



