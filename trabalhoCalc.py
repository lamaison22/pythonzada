# import matplotlib.pyplot as plt
import numpy as np

def funcao (x):
    return x**2
def pontosmedios(particoes,n,pontos):
    for i in range (n):
        pontos.append((particoes[i]+particoes[i+1])/2)
    print(pontos)

def calculaArea(valor_particoes,pontos,n):
    total=0
    for i in range (n):
        ci = funcao(pontos[i])
        total += valor_particoes* ci    
    print(total)


intervalo=[]


entrada = input("Digite os números separados por vírgula:\n ")
n = int(input ("Digite o numero de partições \n"))

# Separa os números usando a função split() e converte cada um para inteiro
intervalo = [int(x) for x in entrada.split(',')]
if(intervalo[0]<intervalo[1]):
    aux =intervalo[0]
    intervalo[0]=intervalo[1]
    intervalo[1]=aux
valor_particoes = ((intervalo[1]-intervalo[0])/n)

particoes = [intervalo[0]] * (n+1)

# Adiciona 0.25 ao valor inicial e armazena no particoes
for i in range(1, len(particoes)):
    particoes[i] = particoes[i-1] + valor_particoes

pontos=[]



pontosmedios(particoes,n,pontos)
calculaArea(valor_particoes,pontos,n)
    
print(intervalo)
print(particoes)
 
