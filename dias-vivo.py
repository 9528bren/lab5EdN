from datetime import datetime

def calcular_dias_vivo(data_nascimento: str) -> int:
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.now()
    dias_vivo = (hoje - nascimento).days
    return dias_vivo

# Programa principal
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias = calcular_dias_vivo(data)
print(f"Você está vivo há {dias} dias.")
