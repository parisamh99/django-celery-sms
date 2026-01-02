# app/tasks.py
from celery import shared_task
from kavenegar import KavenegarAPI, APIException, HTTPException
import os

# اگر میخوای امن باشه، API Key و sender رو از متغیر محیطی بگیر
KAVENEGAR_API_KEY = os.environ.get("KAVENEGAR_API_KEY", "your_api_key_here")
SENDER_NUMBER = os.environ.get("SENDER_NUMBER", "2000660110")

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 10})
def send_sms_task(self, receptor, message=".وب سرویس پیام کوتاه کاوه نگار"):
    """
    ارسال پیام کوتاه با KaaveNegar
    receptor: شماره موبایل گیرنده
    message: متن پیام
    """
    try:
        api = KavenegarAPI(KAVENEGAR_API_KEY)
        params = {
            'sender': SENDER_NUMBER,
            'receptor': receptor,
            'message': message
        }
        response = api.sms_send(params)
        print("KaaveNegar response:", response)
        return response

    except (APIException, HTTPException) as e:
        print("KaaveNegar error:", e)
        raise e  # اگر خطا رخ بده، Celery دوباره تلاش می‌کنه

    