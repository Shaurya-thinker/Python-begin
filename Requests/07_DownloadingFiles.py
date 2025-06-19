import requests

url = "https://cdn.pixabay.com/download/audio/2025/04/15/audio_981caf755e.mp3?filename=reliable-safe-327618.mp3"
r = requests.get(url)
fp = open("winrar.mp3", "wb")
fp.write(r.content)
fp.close()