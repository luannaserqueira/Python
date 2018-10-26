# Aula 1 ex3

#  Ache os zeros da função: y=3x^2-4x-10

a=3
b=-4
c=-10

delta=b**2-(4*a*c)
print(delta)

x1=(-b+(math.sqrt(delta)))/2*a
print(x1)

x2=(-b-(math.sqrt(delta)))/2*a
print(x2)

print('Os zeros da função são ',x1,' e ',x2,'')
