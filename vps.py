import socket
import requests
from IPy import IP
import glob, os
import platform
import sys
import threading
import time
import subprocess

token = "5688089249:AAEw0prgzXgCThzmnoCDafzPXhB_6KYSK6g"

# Tarea a ejecutarse cada determinado tiempo.
def timer():
    while True:
        obtener_info()
        time.sleep(3600)   # 1 hora.

def obtener_info():
    ipmachine = obtener_ip()
    my_system = platform.uname()
    text = f"System: {my_system.system}\nNode Name: {my_system.node}\nRelease: {my_system.release}\nVersion: {my_system.version}\nMachine: {my_system.machine}\nProcessor: {my_system.processor}\n{ipmachine}"
    send_message_dev(text)
    print(text)

def obtener_ip():
    text = 'IP del servidor: '
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    text+= s.getsockname()[0]
    return text

def send_message_dev(sms):
    URL = "https://api.telegram.org/bot"+ token +"/sendMessage"
    headers = {
        'Content-Type': 'application/json',
    }
    chat_id = "-1001754146469"
    data = '{"chat_id": "' + chat_id + '","parse_mode": "markdown", "text": "' + sms + '", "disable_notification": false"'+ '"}'
    try:
        requests.post(URL, headers=headers, data=data)
        return 'Mensaje enviado a Telegram'
    except Exception as e:
        return 'Error interno al enviar el mensaje a Telegram'

    #END CODE


# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()