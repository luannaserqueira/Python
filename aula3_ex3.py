# Aula 3 ex3

# Crie uma funcão para calcular o ângulo zenital do sol (da semana passada) tomando como argumento as medidas da altura e o comprimento da sombra.

import math
def theta(x,y):
    theta=math.atan(x/y)
    print(theta)

print(theta(0.5,5))

theta_graus=theta*180/math.pi
print(theta_graus)
