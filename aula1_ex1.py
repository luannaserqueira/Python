# Aula 1 - ex1
# Se você fizer uma corrida de 10 quilômetros em 43 minutos e 30 segundos, qual será seu tempo médio por milha? Qual é a sua velocidade média em milhas por hora? (Dica: há 1,61 quilômetros em uma milha).
d_metros=10*1000
t_seg=43*60+30

# Velocidade em metros por segundo:
v_ms=d_metros/t_seg
print(v_ms)

# Velocidade em quilômetros por hora:
v_kmh=v_ms*3.6
print(v_kmh)

# Velocidade em libras por hora:
l=1610
v_lh=v_kmh/l
print(v_lh)

# Tempo por libra:
t_l=(t_seg*l)/d_metros
print(t_l)
