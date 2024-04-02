#06: Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
print ("Q6")
salario=1.200
pagar_imposto= salario > 1.200 
print (f" você pagará imposto? {pagar_imposto}")
#07: Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir.
print ("Q7")
a=1
b=2
c=True
d=False
print (a>b and c or d)
a=10 
b=3
c=False
d=False
print (a>b and c or d)
a=5
b=1
c=True
d=True
print (a>b and c or d)
#08: Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: materia1, materia2 e materia3.
print("Q8")
media=7
materia1=8 
materia2= 10
materia3= 3 
resultado= (materia1 + materia2 + materia3)/3
rf= resultado >= 7 
print (f"o seu resultado é esse TRUE aprovado e FALSE reprovado= {rf}")

