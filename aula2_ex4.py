# Aula 2 ex4:

# Um laser vermelho (com comprimento de onda $\lambda = 632.8$ nm) incide em uma fenda dupla produzindo um padrão de interferência com franjas claras e escuras, em um anteparo situado a uma distância D = 1.98 m da fenda. Calcule a distância $\Delta y$ entre dois máximos consecutivos de interferência. Considere o espaçamento entre as fendas, $d$, como sendo igual a 0.250 mm. <em>Dica: a distância entre dois máximos de interferência consecutivos pode ser aproximada por $\Delta y = \frac{\lambda D}{d}$.

comp_onda=632.8
D=1.98
d=0.250*10**(3)

y=(comp_onda*D)/d
print('A distância entre dois máximos é de ',y,'.')
