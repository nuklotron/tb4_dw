import os
import random
import secrets
import string
import requests
import json
from dotenv import load_dotenv
from config.settings import BASE_DIR
import re

load_dotenv(BASE_DIR / '.env')


def send_sms(username, passcode):
    """
    Method sending SMS, service - dev.exolve.ru
    MTC_EXOLVE - API key
    MTC_PHONE - rented phone number
    """
    url = "https://api.exolve.ru/messaging/v1/SendSMS"
    headers = {"Authorization": f"Bearer {os.getenv('MTC_EXOLVE')}"}
    data = {
        "number": os.getenv('MTC_PHONE'),
        "destination": f"{username}",
        "text": f"{passcode}"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers).json()

    print(response)


def generate_passcode():
    """
    Method generating random passcode for authenticate
    """
    return random.randint(1000, 9999)


def generate_invite():
    """
    Method generating invite code for user
    """
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password


def is_valid_phone(number):
    """
    Method checks if the phone number is correct
    """
    return bool(re.match('^[7]\d{10}$', number))
