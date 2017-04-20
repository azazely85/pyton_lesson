import requests
print (dir(requests))
r=requests.get('http://vidshup.ru')
print(r.text)