dnk = input()
l = len(dnk)
i, k = 0, 0
#i- номер символа в строке, k- посчёт повт. символов
while i<l:
    k = 0
    while dnk[i+k] == dnk[i]:
    # пока совпадают символы, повторяем
        k += 1 
    # следующий символ
        if i+k == l:
            break #выход из цикла, если мы вышли из диапозона
    print (dnk[i]+str(k), end='')
    i += k # переход к следующему уникальному символу