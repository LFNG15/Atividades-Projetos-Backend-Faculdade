import datetime

_TABELA_REVISAO = {
    "Alinhamento de Pneus": (20000, None),
    "Correia Dentada": (60000, None),
    "Correia do Alternador": (None, None),  
    "Correia do Compressor de Ar-condicionado": (None, None),
    "Correia poly-v": (None, None),
    "Filtro de ar": (20000, datetime.date(2024, 3, 1)),
    "Filtro de Cabine": (None, datetime.date(2023, 3, 1)),
    "Filtro de Combustível": (None, datetime.date(2023, 3, 1)),
    "Filtro de óleo": (10000, datetime.date(2024, 3, 1)),
    "Fluido de Transmissão": (100000, datetime.date(2020, 2, 12)),
    "Fluído de Freio": (None, datetime.date(2023, 3, 1)),
    "Limpeza do Ar Condicionado": (None, datetime.date(2023, 1, 1)),
    "Óleo Lubrificante": (15000, None),
    "Pneus": (None, datetime.date(2019, 1, 1)),  
}

def precisa_trocar(item, ultima_revisao, km_atual):
    km_troca, data_troca = _TABELA_REVISAO[item]
    #Para itens que dependem do tempo
    if data_troca and ultima_revisao > data_troca:
        return True
    #Para itens que dependem da quilometragem
    elif km_troca and km_atual > km_troca:
        return True
    else:
        return False

def main():
    ultima_revisao_str = input("Digite a data da última revisão do carro (AAAA-MM-DD): ")
    ultima_revisao = datetime.date.fromisoformat(ultima_revisao_str)

    km_atual = int(input("Digite a quilometragem atual do carro: "))

    for item in _TABELA_REVISAO:
        precisa_trocar_item = precisa_trocar(item, ultima_revisao, km_atual)

        if precisa_trocar_item:
            if item == "Correia Dentada":
                print(f"A correia dentada precisa ser trocada.")
                print("Também é recomendado trocar as correias do alternador, do compressor de ar-condicionado e do poly-v juntos.")
            else:
                print(f"O item '{item}' precisa ser trocado.")

if __name__ == "__main__":
    main()