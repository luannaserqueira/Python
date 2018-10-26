# Aula 1 ex2
# Desde sua varanda você escuta o som do primeiro fogo artificial do reveillon 3 segundos depois de ver a luz, qual a distância? (o som tem velocidade 343 m/s e a luz 3x10^8 m/s).

t_som=3
t0=0
v_som=343
v_luz=3*10^8

delta_t=t_som-t0
print(delta_t)

d_som=v_som/delta_t
print(d_som)

d_real=v_som*delta_t
print(d_real)

print('Assumindo t0=0, a distância do som é ',d_som,'m e a distância real é ',d_real,'m')
Assumindo t0=0, a distância do som é  114.33333333333333 m e a distância real é  1029 m
