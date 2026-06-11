vendedores = int(input("Informe quantos vendedores fazem parte da equipe: "))
dias = int(input("Informe quantos dias: "))
equipe = 0.0
melhorVendedor = ""
maiorVenda = 0.0
vendaDia = 0.0

for vendedor in range(vendedores):
    nome = input("\nDigite o nome do vendedor: ")
    total = 0.0
    folgas = 0

    for dia in range(dias):
        venda = float(input("Digite o valor vendido no dia: "))
        
        if venda < 0:
            continue 
        
        elif venda == 0:
            folgas += 1
            continue

        total += venda 
        equipe += venda

        if venda > vendaDia:
            vendaDia = venda
        
    print("Valor total vendido por",nome +" : R$",total)
    
    dias_trabalhados = dias - folgas
    if dias_trabalhados > 0:
        media = total / dias_trabalhados
        print("Média diária de vendas: R$", media)

    if total > maiorVenda:
        maiorVenda = total 
        melhorVendedor = nome

print("Total vendido pela equipe: R$", equipe)
print("O melhor vendedor foi: ", melhorVendedor)
print("O maior valor de venda registrado em um único dia foi: R$", vendaDia)