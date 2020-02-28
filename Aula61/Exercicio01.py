lista = [5, 6, 7, 8, 9]
k = 999999999999999999999999999999999999999999999999999999
b = len(lista)
a = k % b
for i in range(a):
    ab = lista.pop(-1)
    lista.insert(0, ab)
print(lista)
