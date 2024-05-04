<<<<<<< HEAD
import requests
=======
"""
Бот для выгрузки видео в инстаграм
"""
>>>>>>> 69dc20d (add tg)
from instabot import Bot

# Прокси-настройки
proxy_host = "45.41.171.86"
proxy_port = 6122
proxy_username = "ffaspknt"
proxy_password = "w9z2pl1j5c5h"

proxies = {
    'http': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
}

bot = Bot()
<<<<<<< HEAD
bot.login(username='', password='')

video_path = '/video.mp4'
caption = 'test'

bot.upload_video(video_path, caption=caption, options={'proxy': proxies})
=======
bot.login(username='sh1ryudesu', password='dHvfpmWzMA9UUfUtg8w7')

video_path = '/video.mp4'
description = 'test'

bot.upload_video(video_path, description=description, options={'proxy': proxies})
>>>>>>> 69dc20d (add tg)
