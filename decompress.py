with open('dataset_3363_2.txt', 'r') as dataset:
    a = dataset.readline()
h = ''
s = ''
k = 0
for i in range(len(a)):
    i = k
    if a[k].isdigit() == False:
        h = a[k]
        k += 1
    else:
        n = ''
        k = i
        while a[k].isdigit():
            n += a[k]
            k += 1
            if k>=len(a):
                break
        h1 = ''
        while len(h1)<int(n):
            h1 += h
        s += h1
    if k == len(a):
        break
with open('dataset_3363_3.txt', 'w') as res:
    res.write(s)