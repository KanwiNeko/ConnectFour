import random


class Player:
    def __init__(self, iden):
        self.name = str(input(f"Hola jugador {str(iden+1)}, porfavor indica tu nombre: "))
        self.Token = None
        self.iden = iden


def tokencall(name):
    token = None
    while not(token == "X" or token == "O"):
        token = str(input(f"Hola {name}, porfavor escoge una ficha entre 'X' y 'O': "))
    return token


rows, cols = (6, 7)
grid = [["•" for i in range(cols)] for j in range(rows)]

player = [None, None]

for i in range(2):
    player[i] = Player(i)
player[0].Token = tokencall(player[0].name)

if player[0].Token == "X":
    player[1].Token = "O"
elif player[0].Token == "O":
    player[1].Token = "X"

print(f"{player[1].name}, vas a jugar con la ficha [{str(player[1].Token)}] \n")
print("Lanzando una moneda al aire para determinar quién inicia la partida...")
firstplayer = random.randint(0, 1)
print(f"la partida la inicia {player[firstplayer].name} \n")


def printboard():
    def printlines():
        print("+", end="")
        for i in range(len(grid[0])):
            print("-", end="")
        print("+")

    print(" 1234567 ")
    printlines()
    for i in range(len(grid)):
        print("|", end="")
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print("|")
    printlines()


printboard()
end = input()