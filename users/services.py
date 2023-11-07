import os
import random

import requests
import json
from dotenv import load_dotenv
from config.settings import BASE_DIR

load_dotenv(BASE_DIR / '.env')


def send_sms():
    url = "https://api.exolve.ru/messaging/v1/SendSMS"
    headers = {"Authorization": f"Bearer {os.getenv('MTC_EXOLVE')}"}

    data = {
        "number": os.getenv('MTC_PHONE'),
        "destination": "79121222223",
        "text": 'request.user.password'
    }

    response = requests.post(url, data=json.dumps(data), headers=headers).json()

    print(response)


def generate_otp():
    return random.randint(1000, 9999)
