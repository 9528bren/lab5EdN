def calcular_desconto(preco: float, porcentagem_desconto: float) -> float:
    desconto = preco * (porcentagem_desconto / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)


# Interação com o usuário
preco_produto = float(input("Digite o preço do produto: R$ "))
porcentagem = float(input("Digite o percentual de desconto: "))
preco_com_desconto = calcular_desconto(preco_produto, porcentagem)
print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")