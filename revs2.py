#vetores
'''#usando for:
L=[1,2,3]
for i in L:
    print(i)'''

'''#ex07
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i,e in enumerate(a):
    print(i,e)
    if i% 2==0:
        b.append (e * 5)
    else:
        b.append (e + 5)
print(a)
print(b)'''
    
'''#ex08
A = []
for i in range(5):
    A.append(int(input(f"Digite o elemento {i+1} do vetor A: ")))

soma_impares = sum(x for x in A if x % 2 != 0)
print("Soma dos elementos ímpares:", soma_impares)'''

'''#ex09
nomes = []
for i in range(10):
    nomes.append(input(f"Digite o nome {i+1}: "))

print("Nomes lidos:")
for nome in nomes:
    print(nome)'''
'''#10
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(8)]
B = [x * 3 for x in A]
print("Vetor B:", B)'''
'''#11
A = [float(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(20)]
B = [float(input(f"Digite o elemento {i+1} do vetor B: "))for i in range(20)]
C = [A[i] - B[i] for i in range(20)]
print("Vetor C:", C)'''
'''#12
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(15)]
B = [x**2 for x in A]
print("Vetor A:", A)
print("Vetor B:", B)'''
'''#13
import math

A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(15)]
B = [math.factorial(x) for x in A]

print("Vetor A:", A)
print("Vetor B:", B)
'''
'''#14
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(15)]
B = [int(input(f"Digite o elemento {i+1} do vetor B: "))for i in range(15)]
C = A + B
print("Vetor C:", C)'''
#15
A = [float(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
B = A[::-1]
print("Vetor A:", A)
print("Vetor B:", B)
'''#16
A = [float(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(5)]
B = [float(input(f"Digite o elemento {i+1} do vetor B: "))for i in range(5)]
C = [float(input(f"Digite o elemento {i+1} do vetor C: "))for i in range(5)]
D = A + B + C
print("Vetor D:", D)'''
'''#17
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
B = [sum(range(1, x + 1)) for x in A]
print("Vetor B:", B)'''
'''#18
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
B = [-x for x in A]
print("Vetor A:", A)
print("Vetor B:", B)'''
'''#19
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
B = [x / 2 for x in A]
print("Vetor A:", A)
print("Vetor B:", B)'''
'''#20
n = int(input("Digite um número para calcular a tabuada: "))
A = [n * i for i in range(1, 11)]
print("Tabuada de", n, ":", A)'''
'''#21
temp = [float(input(f"Digite a temperatura {i+1} em Celsius: "))for i in range(10)]
menor = min(temp)
maior = max(temp)
media = sum(temp) / len(temp)
print("Menor temperatura:", menor)
print("Maior temperatura:", maior)
print("Média das temperaturas:", media)'''
'''#22
A = [float(input(f"Digite a temperatura {i+1} em Celsius: "))for i in range(5)]
B = [(x * 9/5) + 32 for x in A]
print("Vetor A (Celsius):", A)
print("Vetor B (Fahrenheit):", B)'''
'''#23
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
B = [x * 2 if x % 2 != 0 else x for x in A]
print("Vetor B:", B)'''
'''#24
A = [float(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
B = [x / 2 if i % 2 == 0 else x * 1.5
for i, x in enumerate(A)]
print("Vetor B:", B)'''
'''#25
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(6)]
B = [int(input(f"Digite o elemento {i+1} do vetor B: "))for i in range(6)]
C = [A[i] for i in range(6) if i % 2 != 0] + [B[i]for i in range(6) if i % 2 != 0]
D = [A[i] for i in range(6) if i % 2 == 0] + [B[i]for i in range(6) if i % 2 == 0]
print("Vetor C (índices ímpares):", C)
print("Vetor D (índices pares):", D)'''
'''#26
A = []
B = []

while len(A) < 6:
    valor = int(input(f"Digite um valor par para o vetor A ({len(A)+1}/6): "))
    if valor % 2 == 0:
        A.append(valor)
    else:
        print("Valor inválido! Apenas pares são aceitos.")

while len(B) < 6:
    valor = int(input(f"Digite um valor ímpar para o vetor B ({len(B)+1}/6): "))
    if valor % 2 != 0:
        B.append(valor)
    else:
        print("Valor inválido! Apenas ímpares são aceitos.")

C = A + B
print("Vetor C:", C)'''
'''#27
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
pares = sum(1 for x in A if x % 2 == 0)
impares = sum(1 for x in A if x % 2 != 0)
print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)'''
'''#28
A = [int(input(f"Digite o elemento {i+1} do vetor A: "))for i in range(10)]
B = [int(input(f"Digite o elemento {i+1} do vetor B: "))for i in range(10)]
C = [(A[i] + B[i])**2
     for i in range(10)]
print("Vetor C:", C)'''
'''#29
vetor1 = []
vetor2 = []
pares = 0
impares = 0
total_elementos = 10

print("Digite os elementos do primeiro vetor:")
for i in range(total_elementos):
    num = int(input(f"Elemento {i + 1}: "))
    vetor1.append(num)

print("\nDigite os elementos do segundo vetor:")
for i in range(total_elementos):
    num = int(input(f"Elemento {i + 1}: "))
    vetor2.append(num)

vetor_fusao = vetor1 + vetor2
for num in vetor_fusao:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

percentual_pares = (pares / (total_elementos * 2)) * 100
percentual_impares = (impares / (total_elementos * 2)) * 100

print(f"\nTotal de elementos pares: {pares}")
print(f"Total de elementos ímpares: {impares}")
print(f"Percentual de elementos pares: {percentual_pares:.2f}%")
print(f"Percentual de elementos ímpares: {percentual_impares:.2f}%")'''