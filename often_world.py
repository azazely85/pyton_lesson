dicdata = {}
with open('dataset_3363_4.txt') as dataset:
    data = dataset.read().strip().lower()
data = data.split()
setdata = set(data)
for i in setdata:
    if data.count(i) in dicdata:
        dicdata[data.count(i)].append(i)
    else:
        dicdata[data.count(i)] = [i]
if len(dicdata[max(list(dicdata.keys()))]) > 1:
    word = min(dicdata[max(list(dicdata.keys()))])
else:
    word = dicdata[max(list(dicdata.keys()))]
out = ''.join(word)
print(out, max(list(dicdata.keys())))