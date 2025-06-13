import random

# Dados do jogador
jogador = {
    "nome": "Herói",
    "vida": 100,
    "ataque": 10,
    "defesa": 5,
    "itens": ["Espada", "Escudo"],
    "dinheiro": 0,
    "reino": 1
}

# Lista de inimigos
inimigos = [
    {"nome": "Goblin", "vida": 30, "ataque": 5},
    {"nome": "Esqueleto", "vida": 40, "ataque": 7},
    {"nome": "Orc", "vida": 50, "ataque": 10}
]

# Função de batalha
def batalhar(inimigo):
    print(f"\nVocê encontrou um {inimigo['nome']}!")
    while inimigo["vida"] > 0 and jogador["vida"] > 0:
        dano_jogador = jogador["ataque"] - random.randint(0, 3)
        dano_inimigo = inimigo["ataque"] - jogador["defesa"]

        inimigo["vida"] -= max(dano_jogador, 0)
        jogador["vida"] -= max(dano_inimigo, 0)

        print(f"Você causou {max(dano_jogador, 0)} de dano.")
        print(f"O {inimigo['nome']} causou {max(dano_inimigo, 0)} de dano.")
        print(f"Sua vida: {jogador['vida']}, Vida do inimigo: {inimigo['vida']}\n")

    if jogador["vida"] > 0:
        ganho = random.randint(5, 20)
        jogador["dinheiro"] += ganho
        print(f"Você venceu! Ganhou {ganho} de dinheiro.")
    else:
        print("Você foi derrotado! Fim de jogo.")
        exit()

# Função para explorar reinos
def explorar():
    print(f"\nExplorando o Reino {jogador['reino']}...")
    chance = random.randint(1, 100)
    if chance <= 60:
        inimigo = random.choice(inimigos)
        batalhar(inimigo)
    else:
        print("Você não encontrou inimigos desta vez.")

# Função para trocar de reino
def trocar_reino():
    print("\nPara qual reino deseja ir? (1, 2 ou 3)")
    escolha = input(">> ")
    if escolha in ["1", "2", "3"]:
        jogador["reino"] = int(escolha)
        print(f"Você viajou para o Reino {escolha}!")
    else:
        print("Reino inválido!")

# Menu principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Explorar")
        print("2. Ver status")
        print("3. Trocar de reino")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            explorar()
        elif opcao == "2":
            print(f"\nNome: {jogador['nome']}")
            print(f"Vida: {jogador['vida']}")
            print(f"Itens: {', '.join(jogador['itens'])}")
            print(f"Dinheiro: {jogador['dinheiro']}")
            print(f"Reino atual: {jogador['reino']}")
        elif opcao == "3":
            trocar_reino()
        elif opcao == "4":
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida!")

# Início do jogo
print("Bem-vindo ao RPG dos 3 Reinos!")
menu()
