import re
kom = int(input())
d = {}
igr = 0
#input
# 5
# Алания;2;ЦСКА;1
# Алания;3;Спартак;2
# ЦСКА;0;Зенит;2
# Спартак;1;ЦСКА;1
# Зенит;3;Спартак;1
pobed = 0
ni4 = 0
pora = 0
ochkov = 0
for i in range(kom):
    igra = re.split(r';\b', str(input()))
    if igra[0] not in d:
        d[igra[0]] = [int(igr), int(pobed), int(ni4), int(pora), int(ochkov)]
        if igra[1]>igra[3]:
            d[igra[0]] = [igr+1, int(pobed)+1,ni4, pora, int(ochkov)+3]
        if igra[1]==igra[3]:
            d[igra[0]] = [igr+1, pobed, int(ni4)+1, pora, int(ochkov)+1]
        if igra[1]<igra[3]:
            d[igra[0]] = [int(igr)+1, pobed, ni4, int(pora)+1, ochkov]
    elif igra[0] in d:
        if igra[1] > igra[3]:
            d[igra[0]][0]+=1
            d[igra[0]][1]+= 1
            d[igra[0]][4]+= 3
        if igra[1] == igra[3]:
            d[igra[0]][0]+= 1
            d[igra[0]][2] += 1
            d[igra[0]][4] += 1
        if igra[1] < igra[3]:
            d[igra[0]][0]+= 1
            d[igra[0]][3]+= 1
    if igra[2] not in d:
        d[igra[2]] = [int(igr), int(pobed), int(ni4), int(pora), int(ochkov)]
        if igra[1] > igra[3]:
            d[igra[2]] = [igr + 1, pobed, ni4, pora + 1, ochkov]
        if igra[1] == igra[3]:
            d[igra[2]] = [igr + 1, pobed, ni4 + 1, pora, ochkov + 1]
        if igra[1] < igra[3]:
            d[igra[2]] = [igr + 1, pobed+1, ni4, pora, ochkov+3]
    elif igra[2] in d:
        if igra[3] > igra[1]:
            d[igra[2]][0]+=1
            d[igra[2]][1]+= 1
            d[igra[2]][4]+= 3
        if igra[3] == igra[1]:
            d[igra[2]][0]+= 1
            d[igra[2]][2] += 1
            d[igra[2]][4] += 1
        if igra[3] < igra[1]:
            d[igra[2]][0]+= 1
            d[igra[2]][3]+= 1
print(d)
for i in d:
    print(i + ":" + str(d[i][0]) + ' '+str(d[i][1]) + ' '+str(d[i][2]) + ' ' + str(d[i][3]) + ' ' + str(d[i][4]))