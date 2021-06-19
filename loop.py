# O que o statement else faz em um loop (note que o 'else' está identado com o 'for')?

"O código apresentado, o statement ELSE faz parte do FOR, por estar identado no mesmo distanciamento de margem. Isso representa que, a partir do momento que o FOR não for mais aplicado o ELSE será iterado, mostrando a informação que está em PRINT()."

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
