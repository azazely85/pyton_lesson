slov = {i + 1: 0 for i in range(11)}
kolvo = slov.copy()
with open("dataset_3380_5.txt", 'r') as a:
    for i in a:
        text = i.strip()
        v = {}
        a = text.split()
        clas = int(a[0])

        kolvo[clas] += 1
        slov[clas] += int(a[2])

for i in slov:
    if slov[i] == 0:
        print(i, "-")
    else:
        print(i, float(slov[i] / kolvo[i]))