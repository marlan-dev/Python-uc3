lista=["Banana","Fruta","Maçã"]
print(lista[2])

lista[2]="Banana"
print(lista)

lista.append("Uva")
print(lista)

lista.insert(0, 'Morango')
print(lista)

lista.remove("Fruta")
print(lista)

del lista[2]
print(lista)

lista.pop(1)
print(lista)