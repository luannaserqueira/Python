# Aula 8 ex1

# A conjectura de Collatz, diz que "Todos os inteiros positivos irão eventualmente convergir para 1 usando as regras do Collatz". Faça um programa que verifique a conjectura de Collatz para alguns valores. As regras de Collatz são: Dado um número n:


    se n for par, divida-o por 2;
    Se n for ímpar, atualize-o para 3*n + 1


def c(n):
    count=0
    while n!=1:
          count=count+1
          if int(n)%2==0:
             n= n // 2
          else:
             n=3*n+1
          if count%10==0:
             print("Valor de n", n)
          if n==1
             print("Valor de n", n)
     return count

q=counter(100)
print(q)
