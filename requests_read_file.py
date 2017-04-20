import requests
r=requests.get('https://stepic.org/media/attachments/course67/3.6.2/662.txt')
print(r.text.count('\n'))