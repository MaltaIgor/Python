from pacote import moeda, dado

p = dado.leiadinheiro('digite o preço: R$')



print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10% o valor é {moeda.aumentar(p,10, True)}')
moeda.resumo(p, 80, 35)