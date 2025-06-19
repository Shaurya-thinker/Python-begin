import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://assets.nst.com.my/images/articles/BOTSimagen_NSTfield_image_socialmedia.var_1653879910.jpg")
i = Image.open(BytesIO(r.content))
fp = open("img.jpg", "wb")
i.save(fp)
fp.close()