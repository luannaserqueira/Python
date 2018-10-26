# Aula 3 ex4

# Crie uma função que faça a conversão de uma medida inicialmente em milhas para m, e outra para o inverso; uma de horas para segundos, e o inverso. Utilize estas funções para resolver novamente o primeiro exercício da semana passada (da corrida). Se uma pessoa demora 30 minutos em 4 milhas, qual velocidade media em km/h ? e o tempo medio por kilometro?

# conversão milha para metro:

def milha_metro(m):
    milha_metro=m*1609.34
    return(m)

# conversão metro para milha:

def metro_milha(M):
    metro_milha=M/1609.34
    return(M)

# conversão horas para segundo:

def horas_seg(h):
    horas_seg=60*h
    return(h)

# conversão de minuto para hora:

def minutos_hora(mn):
    minutos_hora=mn/60
    return(mn)

# conversão m/s para km/h:

def ms_kmh(m_s):
    ms_kmh=m_s*3.6
    return(m_s)

# Problema:

s=horas_seg(minutos_hora(30))
print(s)

ms=milha_metro(4)/s
print(ms)
