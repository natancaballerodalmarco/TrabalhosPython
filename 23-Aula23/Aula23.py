# Aula 23 - 10-12-2019
# For

# numero_inicial = int(input('Digite o número para começar a somar: '))
# numero_final = int(input('Digite o número para parar de somar: '))
# total = 0
# for numero in range (numero_inicial, numero_final+1):
#     total += numero

# print(f'Total: {total}')




texto = 'Alelek lek lek lek. Qual é o mais inteligete. O menos.'

print(texto.split('.'))

def nosso_split(txt,sep):
    result = []
    count = 0
    last_sep = 0
    for char in txt:
        if char == sep:
            result.append( txt[last_sep:count] )
            last_sep = count + 1
        count +=1
    if last_sep < len(texto)-1:
        result.append(txt[last_sep:])
    return result

print(nosso_split(texto, '.'))
