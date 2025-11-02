

popi = { '1011':3, '1001':2, '1000':0, '1010':0 }
tmp = min(popi.values())

for i in popi:
    print(i)
    if popi[i]==tmp:
        popi.pop(i)
        break

print(popi)