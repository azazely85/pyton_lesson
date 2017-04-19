s=[]
with open('dataset_3363_5.txt', 'r') as e:
    for line in e:
        s.append(line.strip().split(';'))
for i in range(len(s)):
    del s[i][0]
def среднее (i):
    g = (float(i[0])+float(i[1])+float(i[2]))/3
    return g
for i in s:
    g = среднее(i)
    print(g)
def общее_среднее (s):
    v1 = 0
    v2 = 0
    v3 = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if j == 0:
                v1 += float(s[i][j])
            elif j == 1:
                v2 += float(s[i][j])
            elif j == 2:
                v3 += float(s[i][j])
    return((v1/(len(s)), (v2/(len(s))), (v3/(len(s)))))
g1 = общее_среднее(s)
print(*g1)