# Aula 3 ex2

# Crie uma função que calcule e imprima velocidade media de um objeto a partir de uma posição inicial, a final e o tempo transcorrido para um objeto em MRU. Também crie uma funcão que calcule e imprima a velocidade de um objeto a partir da aceleração constante e o tempo (MRUA) (p.ex. queda libre).

# Velocidade média

def v(x0,x,t)
    v=(x-x0)/t
    print(v)

print(v(0,4,2))
print('A velocidade média é ',v(0,4,2),' m/s.')


# Aceleração

def a(t0,t,v):
    a=v/(t-t0)
    print(a)

print(a(0,5,9.8))
print('A aceleração de um corpo em queda livre é de ',a(0,5,9.8),' m/s^2.')
