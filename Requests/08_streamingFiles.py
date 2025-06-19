import requests
from tqdm import tqdm
url2 = "https://download-cdn.jetbrains.com/python/pycharm-2025.1.2.exe"
#url = "https://cdn.pixabay.com/download/audio/2025/04/15/audio_981caf755e.mp3?filename=reliable-safe-327618.mp3"
r = requests.get(url2, stream=True)
totalExpectedBytes = int(r.headers["Content-Length"])
#print(totalExpectedBytes)
bytesRecieved = 0
progress_bar = tqdm(total=totalExpectedBytes, unit='iB', unit_scale=True)
with open("winrar.exe", 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        #print(f'{bytesRecieved} recieved out of total {totalExpectedBytes}')
        progress_bar.update(128)
        f.write(chunk)
        bytesRecieved += 128
    progress_bar.close()
