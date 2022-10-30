
print('________________COMPRA E TROCO___________________')

#Valores
produto1 = int(input('Primeiro produto: '))
produto2 = int(input('Segundo produto: '))
produto3 = int(input('Terceiro produto: '))
produto4 = int(input('Quarto produto: '))
produto5 = int(input('Quinto produto: '))

pagamento = float(input('Digite o valor em reais para pagar: '))

soma_produtos = produto1 + produto2 + produto3 + produto4 + produto5

if pagamento >= soma_produtos:
    troco = pagamento - soma_produtos
    print('O seu troco é de R$ {:.2f}'.format(troco))
else:
    print('Você não possui dinheiro suficiente para comprar os produtos.')