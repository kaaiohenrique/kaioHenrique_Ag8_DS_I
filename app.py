# Programa de pesquisa de satisfação TudoWeb
# Autor: Kaio Henrique da Silva

print("Bem-vindo(a) a pesquisa de satisfação TudoWeb!")

# Sequência
for sequencia in range(1, 51):
    print(f"\nAvaliador(a) {sequencia} de 50: ")

# Variáveis
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
excelente = 0
bom = 0
ruim = 0

# Avaliação
opiniao = input("\nPor favor, avalie nosso atendimento com uma escala de 1 a 3, sendo 1 - Excelente, 2 - Bom e 3 - Ruim: ").strip().lower()

match opiniao:
    case "1" | "excelente":
        print(f"{\nprint_avaliacao}")
        excelente += 1
    case "2" | "bom":
        print(f"{\nprint_avaliacao}")
        bom += 1
    case "3" | "ruim":
        print(f"{\nprint_avaliacao}")
        ruim += 1 
    case _:
        print("\nPor favor, selecione uma das 3 opções acima!")

# Contador
print("\nResultado geral da Pesquisa: ")
print(f"Respostas “EXCELENTE”: {excelente}")
print(f"Respostas “RUIM”: {ruim}")
