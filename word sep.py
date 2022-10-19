a = "adit bro i did it... tere sir ke upar se jaega ye ik"
l = []
while True:
    try:
        b = 0
        c = ""
        d = ""
        while c != " ": 
            d += c
            c = a[b]
            b += 1
        l.append(d)
        r = ""
        while True:
            try:
                c = a[b]
                b += 1
                r = r + c
            except:
                break
        a = r
    except:
        break
l.append(a)
print(l)


