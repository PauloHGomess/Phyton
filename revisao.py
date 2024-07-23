##revisao
print ("Questão 1\n")
#1 questao
num1= int(input("Por obsequio digite o numero 1"))
num2= int (input("por favor digite o numero 2"))
soma= num1+num2
print(f"a soma dos dois numeros é: {soma}")

print ("Questão 2\n")
#2 questao
pi= 3.14;
raio= float(input("Digite o raio"))
area= (pi*raio**2)
print (f"p valor da area é: {area}")

print ("Questão 3\n")
#3 questao
hr= float(input("Digite o valor da hora trabalhada"))
nhr= float(input("Digite a quantidade mensal de horas trabalhadas"))
perc= float(input("qual o percentual de desconto do inss"))
bruto= hr*nhr;
desc= (bruto*perc/100);
liq= bruto-desc;
print(f"o salario liquido é:{liq}")

print ("Questão 4\n")
#4 questao
nome= (input("Digite o seu nome "))
sexo= (input("Digite o sexo"))
print(f" o nome da pessoa é {nome} e o seu sexo {sexo}!")

print ("Questão 5\n")
#5 questao
a= float(input("numero 1"))
b= float(input("numero 2"))
div= a/b
total= div**2;
print(f"o valor é {total}")

print ("Questão 6\n")
#6 questao
a= int(input("digite um numero"))
suc= a+1 
ant=a-1
print(f" o numero é: {a}\n o seu antecessor é: {ant} \n o seu sucessor é: {suc}")

print ("Questão 7\n")
#7 questao
base=float(input("DIGITE O VALOR DA BASE"))
indice=float(input("DIGITE O VALOR DA INDICE"))
raiz= base**(1/indice)
print(f"O valor da raiz é {raiz}")
print ("Questão 8\n")
#8 Questao

pi = 3.14
raio = float(input("Digite o valor do raio:"))
altura = float(input("Digite o valor da altura"))
volume = pi *(raio**2)* altura 
print (f"O valor do volume de uma lata de óleo cilíndrica é: {volume}\n")

print ("Questão 9\n")
#9 Questao

valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros (%): "))
tempo = float(input("Digite o tempo de atraso (meses): "))
prestacao = valor + (valor * (taxa / 100) * tempo)
print(f"Valor da prestação em atraso: {prestacao:}\n")

print ("Questão 10 \n")
#10 Questao


comprimento = float(input("Digite o comprimento da caixa: "))
largura = float(input("Digite a largura da caixa: "))
altura = float(input("Digite a altura da caixa: "))
volume = comprimento * largura * altura
print(f"Volume da caixa retangular: {volume: }\n")


print ("Questão 11\n")
#11 Questao


a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
quadrado_soma = (a + b + c)**2
print(f"Quadrado da soma: {quadrado_soma}\n")

print ("Questão 12\n")
#12 Questao

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
quadrado_soma = (a + b + c)**2
print(f"Quadrado da soma: {quadrado_soma}\n")

print ("Questão 13\n")
#13 Questao

pi = 3.14
raio = float(input("Digite o valor do raio da circunferência: "))
area = pi * raio**2
print(f"Área da circunferência: {area: }\n")


print ("Questão 14\n")
#14 Questao


distancia_km = float(input("Digite a distância percorrida (km): "))
tempo_min = float(input("Digite o tempo gasto (minutos): "))
distancia_m = distancia_km * 1000
tempo_s = tempo_min * 60
velocidade = distancia_m / tempo_s
print(f"Velocidade do projétil: {velocidade:} m/s\n")


print ("Questão 15\n")
#15 Questao

pi = 3.14
raio = float(input("Digite o valor do raio da esfera: "))
volume = (4/3) * pi * raio**3
print(f"Volume da esfera: {volume:}")
