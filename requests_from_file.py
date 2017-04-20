import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
s = 'https://stepic.org/media/attachments/course67/3.6.3/'
m = r.text.split()
while m[0] != 'We':
    r = requests.get(s+r.text)
    m = r.text.split()
    print(r.text)
