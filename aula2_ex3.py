# Aula 2 ex3:

# Suponha que o preço de um livro seja 24.95 reais, porém as livrarias têm desconto de 40%. Os custos de envio são de 3.00 reais para o primeiro livro e 0.75 reais para os livros adicionais. Qual é o custo total da compra de 60 livros?

preco_livro=24.95
desconto=0.4
custo_envio_1livro=3
custo_envio=0.75
n=60

P=preco_livro*60+3+(n-1)*custo_envio
print(P)

p=0.4*P
print(p)

print('O valor da compra com 40% de desconto será de ',p,'.')
