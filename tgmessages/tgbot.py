import datetime
from django.conf import settings
import httpx
import json





#tg_bot

token = settings.TG_TOKEN
url = f'https://api.telegram.org/bot{token}/'
method = 'sendMessage'
chat_id_admin = settings.TG_CHAT_ID_ADMIN
chat_id_al = settings.TG_CHAT_ID_AG


def defaultconventer(o):
    if isinstance(o, datetime.date):
        return o.__str__()


def send_order_to_tg(url, method, chat_id, data):
    phone = (str('%2b'+data.get("phone"))).replace(' ','').replace('+','')
    text = f'Полученая новая заявка :%0A Имя:  {data.get("name")} %0A тел:{phone}   %0A Из {data.get("departure")} в {data.get("arrival")} %0A на {data.get("date")}   %0A Проверьте почту ag8035888@yandex.ru'
    return httpx.post(f'{url}{method}?chat_id={chat_id}&text={text}')

