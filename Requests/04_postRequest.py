import requests
r = requests.post('https://httpbin.org/post?a=b', data={'Shaurya': 'value'})
print(r.text)