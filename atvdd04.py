#q1Acelciusparafahrenheit
celcius=float(input("Digite a temperatura em graus celcius:"))
calculo=(9*celcius+160)/5
print(f"A temperatura em fahrenheit é: {calculo}")

#Q1bFahrenheitparacelcius
f=float(input("Digite a temperatura em graus fahrenheit:"))
calculo1=((f-32)*5)/9
print(f"A temperatura em fahrenheit é: {calculo1}")

#q1Cvolumelatadeoleo
import math
raio=float(input("digite o valor do raio da lata de óleo:"))
altura=float(input("digite a altura da lata de óleo:"))
calculo2=math.pi*raio**2* altura
print(f"O volume da lata de óleo é: {calculo2} cm³")

#q1dlitrosgastosviagem
tempo=float(input("Digite o tempo gasto na viagem:"))
velo=float(input("Digite a velocidade media:"))
distancia=tempo*velo
litrosusados= distancia/12
print(f"A quantidade de litros de combustiveis gastos foi: {litrosusados} \nA velocidade media é: {velo} \nA distância percorrida foi {distancia}")
 #Q1Evalorprestacaoematraso
valor=float(input("O valor da parcela:"))
taxa=float(input("Digite a taxa diária estabalecida:"))
tempo=int(input("Digite o tempo dias de atraso:"))
prestacao=valor+(valor*(taxa/100)*tempo)
print(f"O valor da prestação é: {prestacao}")
#q1finvertervalores
a=float(input("Digite o numero A"))
b=float(input("Digite o numero B"))
a1=B
b1=a
print(f"O valor de A é {a1}:\nO valor de B é: {b1} ")

adic=val1+val2
ad= val1+val3
ad2= val1+val4
ad3= val2+val3
ad4= val2+val4
ad5= val3+val4

adic1= val1*val2
ad2= val1*val3
ad23= val1*val4
ad24= val2*val3
ad26= val2*val4
ad27= val3*val4

print(f"a soma de {val1} + {val2} é: {adic}\na soma de {val1} + {val3} é: {ad}\na soma de {val1} + {val4} é: {ad2}\na soma de {val2} + {val3} é: {ad3}\na soma de {val2} + {val4} é: {ad4}\na soma de {val3} + {val4} é: {ad5}")
print(f"a multiplicação de {val1} x {val2} é: {adic1}\na multiplicação de {val1} x {val3} é: {ad2}\na multiplicação de {val1} x {val4} é: {ad23}\na multiplicação de {val2} x {val3} é: {ad24}\na multiplicação de {val2} x {val4} é: {ad26}\na multiplicação de {val3} x {val4} é: {ad27}")
