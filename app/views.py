from django.shortcuts import render
from .tasks import send_sms_task

def send_sms_view(request):
    message = None
    if request.method == "POST":
        phone = request.POST.get("phone")
        send_sms_task.delay(phone)
        message = "پیام در صف celery قرار گرفت"
    return render(request,'send_sms.html',{'message':message})

