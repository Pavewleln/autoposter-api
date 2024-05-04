<<<<<<< HEAD
=======
"""
Файл для выгрузки видео в тикток
"""
import os
>>>>>>> 69dc20d (add tg)
from tiktok_uploader.upload import upload_videos
from tiktok_uploader.auth import AuthBackend

proxy_host = "45.41.171.86"
proxy_port = "6122"
proxy_username = "ffaspknt"
proxy_password = "w9z2pl1j5c5h"
<<<<<<< HEAD
=======

>>>>>>> 69dc20d (add tg)
proxy = {
    'user': proxy_username,
    'pass': proxy_password,
    'host': proxy_host,
    'port': proxy_port,
}

videos = [
    {
<<<<<<< HEAD
        'video': '../video/video1.mp4',
=======
        'video': 'video/video1.mp4',
>>>>>>> 69dc20d (add tg)
        'description': 'Video 1 is about ...'
    }
]

<<<<<<< HEAD
auth = AuthBackend(cookies='../config/cookies.txt')
failed_videos = upload_videos(videos=videos, auth=auth, proxy=proxy)

for video in failed_videos:
    print(f'{video['video']} with description "{video['description']}" failed')
=======
cookies_path = os.path.join(os.getcwd(), 'config', 'cookies.txt')
auth = AuthBackend(cookies=cookies_path)
failed_videos = upload_videos(videos=videos, auth=auth, proxy=proxy)

for video in failed_videos:
    print(f'{video['video']} with description "{video['description']}" failed')

>>>>>>> 69dc20d (add tg)
