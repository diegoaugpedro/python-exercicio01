from functools import reduce
import random as rd

numero = rd.randint(0, 50)
print(numero)

numero = rd.choice(range(0, 50, 2))
print(numero)

size = len([1, 2, 3, 4, 5])
print(size)

nome = "DIEGO"
print(nome)
print(nome[3:6])
print(nome[:5])
print(nome[2:])
print(nome.lower())
print(nome.strip('I'))
print(nome.split('G'))
print(nome.find('G'))
print(nome.replace('G', 'I'))

try:
    x = 1 / 0
except:
    print('Não é possível realizar a divisão!')

sujeito = "Diego"
verbo = "é"
predicado = "Analista de Sistemas"
mensagem = f"{sujeito} {verbo} {predicado}."
print(mensagem)

def multiplicaPorCinco(x):
    return x * 5

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

multiplosDeCinco = [i*2 for i in range(1, 50)]
print(multiplosDeCinco)

multiplosDeDois = map(multiplicaPorCinco, (range(1, 50)))
print(list(multiplosDeDois))

somaDeIntervalos = reduce(soma, range(0, 50))
print(somaDeIntervalos)

dicionario = dict()
dicionario = {
    'd': 1,
    'i': 2,
    'e': 3,
    'g': 4,
    'o': 5
}
print(dicionario)
